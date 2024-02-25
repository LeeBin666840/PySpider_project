# 加载和执行js代码
from functools import partial
import subprocess
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")

# 在它上面写上固定的一段话. 否则会有乱码缠身. 很难解决
import execjs  # python执行js代码的模块. pip install execjs
import requests

session = requests.session()

# 加载第一个cookie
session.get("*******")


f = open("生成.js", mode="r", encoding="utf-8")
code = f.read()

# 加载代码
js = execjs.compile(code)

headers = js.call("fn", {})

img_resp = session.get("*****", headers=headers)
print(img_resp.text)

# ddddocr(免费)
# 图鉴(花钱)

# 验证码字符串
verify_code = "xxxx"

url = "*****"

form_data = {
    "username": "18811131111",
    "password": "11111111",
    "code": verify_code,
    "hdn_refer": ""
}

headers = js.call("fn", form_data)

default_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}
# 把生成好的带有signature的头的信息更新到default_headers
default_headers.update(headers)

resp = session.post(url, data=form_data, headers=default_headers)
# 返回的东西对不对
print(resp.text)
