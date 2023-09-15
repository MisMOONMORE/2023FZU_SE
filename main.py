import re
import urllib.request,urllib.error
import bs4
import time
import os

baseUrl = "https://www.luogu.com.cn/problem/P"
savePath = "D:\\Programms My\\SWE\\Problem\\"
minn = 1001
maxn = 1010

def main():
    print("计划爬取到P{}".format(maxn))
    for i in range(minn,maxn+1):
        print("正在爬取P{}...".format(i),end="")

        # 延时
        time.sleep(10)

        html = getHTML(baseUrl + str(i))
        if html == "error":
            print("爬取失败，可能是不存在该题或无权查看")
        else:

            # 延时
            time.sleep(5)
            problemMD = getMD(html)

            print("爬取成功！正在保存...",end="")
            saveData(problemMD,"P"+str(i)+".md")
            print("保存成功!")
    print("爬取完毕")

def getHTML(url):
    headers = {
        "user-agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 85.0.4183.121 Safari / 537.36",
        "cookie": "__client_id=d670d45cce0e21ad3e7f30f352487ddb8028277b; _uid=1016745"
    }
    request = urllib.request.Request(url = url,headers = headers)
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8')
    if str(html).find("Exception") == -1:
        return html
    else:
        return "error"


def getMD(html):
    bs = bs4.BeautifulSoup(html,"html.parser")
    core = bs.select("article")[0]
    title = bs.select("title")[0].text.strip()
    md = "# " + title
    md = str(core)
    md = re.sub("<h1>","# ",md)
    md = re.sub("<h2>","## ",md)
    md = re.sub("<h3>","#### ",md)
    md = re.sub("</?[a-zA-Z]+[^<>]*>","",md)
    return md

def saveData(data, i):
    filename = "P" + str(i) + " - " + data + ".md"

    cfilename = os.path.join(savePath, filename)
    file = open(cfilename,"w",encoding="utf-8")
    for d in data:
        file.writelines(d)
    file.close()

if __name__ == '__main__':
    main()