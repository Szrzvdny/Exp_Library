# *_* coding=utf-8 *_*
# Author:Szrzvdny
import urllib
import hashlib

class dzscuz_focus_flashxss(object):

    def __init__(self,url):
        self.result = {
            'url':url,
            'cms':'dzscuz_focus_flashxss',
            'vuln_title':'esccms_MoeIndex_sqli',
            'vuln_level':1,
            'vuln_type':6,
            'vuln_author':'Szrzvdny',
            'vuln_source':'null',
            'description':'文件中focus.swf存在flashxss',
        }
    def verify(self):
        headers = {
            'User-anget':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        }
        flash_md5 = "c16a7c6143f098472e52dd13de85527f"
        payload = "/static/image/common/focus.swf"
        vulnurl = self.result['url'] + payload
        try:
            req = urllib.request.urlopen(vulnurl)
            data = req.read()
            md5_value = hashlib.md5(data).hexdigest()
            if md5_value in flash_md5:
                self.result['payload'] = self.result['url'] + payload
                return self.result
            else:
                pass
        except:
            pass

    def __exploit(self):
        pass

if __name__ == '__main__':
    verify = dzscuz_focus_flashxss("http://127.0.0.1/")
    res = verify.verify()
    print(res)
    print(__file__)