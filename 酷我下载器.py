from functools import partial
import subprocess
# 指定utf-8编码 执行逆向
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs
import requests
import os

class kuwo:
    def Spider(self):
        headers = {
            "Secret": "c89ecb0720ebba95b4e92ed585a71159b7d3f1902e4ea7d9867a877dec71275d01731686",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        }
        cookies = {
            "Hm_lvt_cdb524f42f0ce19b169a8071123a4797": "1701493705",
            "_ga": "GA1.2.377037746.1701493706",
            "_gid": "GA1.2.175253767.1701493706",
            "Hm_lpvt_cdb524f42f0ce19b169a8071123a4797": "1701503148",
            "_gat": "1",
            "_ga_ETPBRPM9ML": "GS1.2.1701503086.2.1.1701503151.60.0.0",
            "Hm_Iuvt_cdb524f42f0cer9b268e4v7y735ewrq2324": "KJ8CeGmxRerNWx7piwmBiSmkFrRpH8D2"
        }
        url = "http://www.kuwo.cn/api/v1/www/music/playUrl"
        try:
            response = requests.get(url, headers=headers, cookies=cookies, verify=False)
            self.ck = response.cookies.get_dict()['Hm_Iuvt_cdb524f42f0cer9b268e4v7y735ewrq2324']
            self.secret = execjs.compile(open('cookie.js', 'r', encoding='utf-8').read()).call('h', self.ck)
        except Exception as e:
            print(e)

    def get_singer(self, keyword, num):
        try:
            headers = {
                "Accept": "application/json, text/plain, */*",
                "Accept-Language": "zh,zh-CN;q=0.9,ru;q=0.8",
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "Pragma": "no-cache",
                "Referer": "https://www.kuwo.cn/",
                "Secret": self.secret,
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                "origin": "https://www.kuwo.cn/"
            }
            cookies = {
                "Hm_Iuvt_cdb524f42f0cer9b268e4v7y734w5esq24": self.ck
            }
            url = "http://www.kuwo.cn/api/www/search/searchMusicBykeyWord"
            params = {
                "key": str(keyword),
                "pn": '1',
                "rn": str(num),
                "httpsStatus": "1",
                "plat": "web_www",
                "from": ""
            }
            response = requests.get(url, headers=headers, cookies=cookies, params=params, verify=False)
            count = 1
            mids = []
            names = []
            for i in response.json()['data']['list']:
                singer = i['artist'].replace('&nbsp;', '')
                name = i['name'].replace('&nbsp;', '')
                mid = i['rid']
                mids.append(str(mid))
                names.append(name)
                print(count, ": ", singer, "        =====================         ", name)
                count += 1
            song = int(input('请输入你要请的歌曲的序号(-1即可退出程序)：'))
            if song == -1:
                quit()
            return mids[song - 1], names[song - 1]
        except Exception as e:
            print(e)

    def get_link(self, keyword, num):
        try:
            mid, name = self.get_singer(keyword, num)
            headers = {
                "Secret": self.secret,
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            }
            cookies = {
                "Hm_Iuvt_cdb524f42f0cer9b268e4v7y734w5esq24": self.ck
            }
            url = "http://www.kuwo.cn/api/v1/www/music/playUrl"
            params = {
                "mid": mid,
                "type": "video",
                "httpsStatus": "1",
                "plat": "web_www",
                "from": ""
            }
            response = requests.get(url, headers=headers, cookies=cookies, params=params, verify=False)
            if 'mp3' in response.text:
                print(response.json()['data']['url'].split('?')[0])
                u3 = response.json()['data']['url'].split('?')[0]
                res4 = requests.get(u3)

                if not os.path.exists('music'):
                    os.mkdir('music')
                with open('music\\' + name + '.mp3', "wb") as file:
                    file.write(res4.content)
            elif "付费" in response.text and "mp3" not in response.text:
                params = {
                    "mid": mid,
                    "type": "mv",
                    "httpsStatus": "1",
                    "reqId": "1e6c37e0-3df3-11ee-a31f-094ba5b6aa81",
                    "plat": "web_www",
                    "from": ""
                }
                response = requests.get(url, headers=headers, cookies=cookies, params=params, verify=False)
                if 'mp4' in response.text:
                    print(response.json()['data']['url'].split('?')[0])
                    u4 = response.json()['data']['url'].split('?')[0]
                    res4 = requests.get(u4)
                    if not os.path.exists('video'):
                        os.mkdir('video')
                    with open('video\\' + name + '.mp4', "wb") as file:
                        file.write(res4.content)
                else:
                    print('该歌曲网页端没有收录，请请前往APP端收听')
            else:
                print('该歌曲网页端没有收录，请请前往APP端收听')
        except Exception as e:
            print(e)


if __name__ == '__main__':
    while True:
        keyword = input('请输入歌手或者歌曲的名称：')
        if keyword == '-1':
            break
        num = input('请输入下载的歌曲数量：')
        kw = kuwo()
        kw.Spider()
        kw.get_link(keyword, num)
