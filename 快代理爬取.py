import requests
from lxml import etree

a = int(input("打印几页？"))

for n in range(1,a+1):
    url = 'https://free.kuaidaili.com/free/inha/{}/'.format(n)
    head = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    response = requests.get(url=url, headers=head)

    html = etree.HTML(response.text)
    # print(html.xpath("//div[@id='list']//td[position()<3]/text()"))
    # print(html.xpath("//div[@id='list']//td[1]/text()|//div[@id='list']//td[2]/text()"))
    hosts = html.xpath("//div[@id='list']//td[1]/text()")
    prots =html.xpath("//div[@id='list']//td[2]/text()")
    with open("../project_02/ip.text", 'a')as f:
        for host,prot in zip(hosts,prots):
            proxy = host + ":" + prot
            f.write(proxy+'\n')
            print(proxy)
    n+=1
for host, prot in zip(hosts, prots):
    proxy = host + ":" + prot
    print(proxy)
f.close()







