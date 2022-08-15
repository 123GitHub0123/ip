import requests
from lxml import etree
import re

url = 'https://www.89ip.cn/'
header = {

}
response = requests.get(url=url,headers=header)
html = response.text
html1 = etree.HTML(response.text)
pattern = re.compile(r'\d{0,3}\.\d{0,3}\.\d{0,3}\.\d{0,3}')
ip = pattern.findall(html)
prot = str(html1.xpath("//div[@class='layui-form']/table/tbody/tr/td[2]/text()"))
patter = re.compile(r'[0-9]+')
prots =patter.findall(prot)
with open("../project_02/89ip.text", 'w')as f:
    for ip, prots in zip(ip, prots):
        proxy = ip + ":" + prots
        print(proxy)
        f.write(proxy+'\n')
    f.close()
