import requests
import re

url = 'https://www.89ip.cn/'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77'
}
response = requests.get(url=url, headers=header)
html = response.text#获取89ip代理的html页面
x = re.sub('\s+', '', html).strip()#处理html页面的空字符
patter1 = re.compile(r'<td>(\d{0,3}\.\d{0,3}\.\d{0,3}\.\d{0,3})</td>')#正则匹配ip
patter2 = re.compile(r'<td>([0-9]+)</td>')#正则匹配<td>标签的端口
ip = patter1.findall(x)
prot = patter2.findall(x)
# print(ip)
# print(prot)
with open("../project_02/89ip.csv", 'w', encoding='utf-8') as f:#使用utf8格式写入文档
    for ip, prot in zip(ip, prot):#同时读取两个数组数据
        proxy = ip + ":" + prot#组合
        print(proxy)
        f.write(proxy + '\n')
f.close()
