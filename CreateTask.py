#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import os
import io
import sys
import sendhtml
import time
import datetime
import json
from pprint import pprint
import certifi
import urllib3

default_encoding = 'utf-8'

if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

def createTask():
    url = "https://api.trello.com/1/cards?key=04eb8a17d3a804e6114ff1b06255f89c&token=8188d4cb7da431830c2b60fd9fc62cd4c89925ae3afe0774dd2746a9a18090f5"
    postDataList = json.load(io.open('taskList.json','r+', encoding='utf-8'))

    for dic in postDataList:
        # result = requests.post(url=url,data=dic,verify=False)

        encoded_data = json.dumps(dic).encode('utf-8')
        http = urllib3.PoolManager(cert_reqs = 'CERT_REQUIRED',ca_certs = certifi.where())
        result = http.request(method="POST",url=url,body=encoded_data,headers={'Content-Type': 'application/json'})

        if result.status == 200:
            print("创建成功！")
        else:
            print("创建失败")


if __name__ == '__main__':createTask()
