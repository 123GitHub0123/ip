import requests
from lxml import etree

url = 'https://proxy.seofangfa.com/'
header =  {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
response = requests.get(url=url, headers=header)
html = etree.HTML(response.text)
ip = html.xpath("//div[@class='table-responsive']/table[1]/tbody//tr/td[1]/text()")
prots= html.xpath("//div[@class='table-responsive']/table[1]/tbody//tr/td[2]/text()")
for ip,prots in zip(ip,prots):
    proxy =ip+":"+prots
    print(proxy)

