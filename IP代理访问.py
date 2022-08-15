import requests

url = "http://httpbin.org/get"
url_ip = 'http://http1.9vps.com/getip.asp?username=18142510250&pwd=13cbd2a4313bb4f06e0bd441fe452e7b&geshi=1&fenge=1&fengefu=&Contenttype=1&getnum=1&setcity=&operate=all'
responses = requests.get(url=url_ip)
ip = responses.text
print(ip)
proxy = {
    'http':ip,
    'https':ip
}
response = requests.get(url=url, proxies=proxy)
print(response.text)
