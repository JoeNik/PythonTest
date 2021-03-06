from datetime import datetime
import json
import urllib.request
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
import time
import os
import ssl

#Mac下关闭ssl验证，不然会报错
#ssl._create_default_https_context = ssl._create_unverified_context

global myurl
myurl = "https://oapi.dingtalk.com/robot/send?access_token=b63c5a144e9102029af7ef052c20150503441101f54dbb1c81a47285d56105d9"

def send_request(url, datas):
    #传入url和内容发送请求
    # 构建一下请求头部
    header = {
    "Content-Type": "application/json",
    "Charset": "UTF-8"
    }
    sendData = json.dumps(datas) # 将字典类型数据转化为json格式
    sendDatas = sendData.encode("utf-8") # python3的Request要求data为byte类型
    # 发送请求
    request = urllib.request.Request(url=url, data=sendDatas, headers=header)
    # 将请求发回的数据构建成为文件格式
    opener = urllib.request.urlopen(request)
    # 打印返回的结果
    print(opener.read())


def get_ddmodel_datas(type):
    # 返回钉钉模型数据，1:文本；2:markdown所有人；3:markdown带图片，@接收人；4:link类型
    if type == 1:
        my_data = {
            "msgtype": "text",
            "text": {
                "content": " "
            },
            "at": {
                "atMobiles": [
                    "18046056247"
                ],
                "isAtAll": False
            }
        }
    elif type == 2:
        my_data = {
            "msgtype": "markdown",
            "markdown": {"title": " ",
                         "text": " "
                         },
            "at": {
                "isAtAll": True
            }
        }
    elif type == 3:
        my_data = {
            "msgtype": "markdown",
            "markdown": {"title": " ",
                         "text": " "
                         },
            "at": {
                "atMobiles": [
                    "18046056247"
                ],
                "isAtAll": False
            }
        }
    elif type == 4:
        my_data = {
            "msgtype": "link",
            "link": {
                "text": " ",
                "title": " ",
                "picUrl": "",
                "messageUrl": " "
            }
        }
    return my_data

def get_mysqldatas(sql):
    # 一个传入sql导出数据的函数，实例为MySQL需要先安装pymysql库，cmd窗口命令：pip install pymysql
    # 跟数据库建立连接
    conn = pms.connect(host='服务器地址', user='用户名', passwd='密码', database='数据库', port=3306, charset="utf8")
    # 使用 cursor() 方法创建一个游标对象
    cur = conn.cursor()
    # 使用 execute() 方法执行 SQL
    cur.execute(sql)

    # 获取所需要的数据
    datas = cur.fetchall()

    # 关闭连接
    cur.close()
    # 返回所需的数据
    return datas



def main():
    print('Main! The time is: %s' % datetime.now())
    #按照钉钉给的数据格式设计请求内容 链接https://open-doc.dingtalk.com/docs/doc.htm?spm=a219a.7629140.0.0.p7hJKp&treeId=257&articleId=105735&docType=1
    #调用钉钉机器人全局变量myurl
    global myurl

    # 1.Text类型群发消息
    # 合并标题和数据
    My_content = "hello,  @18046056247 这是一个测试消息"
    my_data = get_ddmodel_datas(1)
    # 把文本内容写入请求格式中
    my_data["text"]["content"] = My_content
    send_request(myurl, my_data)

    # 3.Markdown（带图片@对象）
    my_data = get_ddmodel_datas(3)
    my_data["markdown"]["title"] = "系统预警"
    my_data["markdown"][
        "text"] = "![screenshot](http://i01.lw.aliimg.com/media/lALPBbCc1ZhJGIvNAkzNBLA_1200_588.png)\n " # "#### 系统预警内容  \n > @188XXXXXXXX \n\n > ![screenshot](http://i01.lw.aliimg.com/media/lALPBbCc1ZhJGIvNAkzNBLA_1200_588.png)\n  > ###### 20点00分发布 [详情](http://www.baidu.cn/)"
    send_request(myurl, my_data)

    # 4.Link类型群发消息
    my_data = get_ddmodel_datas(4)
    my_data["link"]["text"] = "群机器人是钉钉群的高级扩展功能。群机器人可以将第三方服务的信息聚合到群聊中，实现自动化的信息同步。 "
    my_data["link"]["title"] = "自定义机器人协议"
    my_data["link"][
        "messageUrl"] = "https://open-doc.dingtalk.com/docs/doc.htm?spm=a219a.7629140.0.0.Rqyvqo&treeId=257&articleId=105735&docType=1"
    send_request(myurl, my_data)


if __name__ == "__main__":
    # 定时执行任务，需要先安装apscheduler库，cmd窗口命令：pip install apscheduler
    # 随脚本执行
    # scheduler = BlockingScheduler()
    # 后台执行
    scheduler = BackgroundScheduler()

    # 每隔20秒执行一次
    scheduler.add_job(main, 'interval', seconds=20)
    '''
    ***定时执行示例***
    #固定时间执行一次
    #sched.add_job(main, 'cron', year=2018, month=9, day=28, hour=15, minute=40, second=30)
    #表示2017年3月22日17时19分07秒执行该程序
    scheduler.add_job(my_job, 'cron', year=2017,month = 03,day = 22,hour = 17,minute = 19,second = 07)

    #表示任务在6,7,8,11,12月份的第三个星期五的00:00,01:00,02:00,03:00 执行该程序
    scheduler.add_job(my_job, 'cron', month='6-8,11-12', day='3rd fri', hour='0-3')

    #表示从星期一到星期五5:30（AM）直到2014-05-30 00:00:00
    scheduler.add_job(my_job(), 'cron', day_of_week='mon-fri', hour=5, minute=30,end_date='2014-05-30')

    #表示每5秒执行该程序一次，相当于interval 间隔调度中seconds = 5
    scheduler.add_job(my_job, 'cron',second = '*/5')
    '''
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
    try:
        # 其他任务是独立的线程执行
        while True:
            pass
            # time.sleep(60)
            # print('进程正在执行!')
    except (KeyboardInterrupt, SystemExit):
        # 终止任务
        scheduler.shutdown()
        print('Exit The Job!')

