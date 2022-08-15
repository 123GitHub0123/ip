import requests
import  csv

with open(r'ip.text', encoding='utf-8')as f:
    reader = csv.reader(f)
    for row in reader:
        for ip in row:
            proxies = {'http': ip,
                       'https': ip
                       }
            url = "http://www.baidu.com/"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
            }
            try:
                response = requests.get(url, headers=headers, proxies=proxies, timeout=5)
                print(response.text)
            except Exception as e:
                print(f"请求失败，代理IP无效！{e}")
            else:
                with open(r'有效ip.csv','a')as f1:
                    f1.write(ip+'\n')
                    f1.close()
                print(f"请求成功，代理IP有效！{proxies}")
f.close()