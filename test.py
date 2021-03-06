import requests
import lxml.html

r = requests.get("https://coinmarketcal.com/")
html = r.text
root = lxml.html.fromstring(html)

time_of_event = root.xpath(
    "/html/body/main/div[3]/section[1]/div[2]/div[3]/article[1]/div/h5[1]/strong")
print(time_of_event[0].text.strip())
# strip()で出力結果の前後の空白を抜け出し
title_of_event = root.xpath(
    "/html/body/main/div[3]/section[1]/div[2]/div[3]/article[1]/div/h5[2]/strong")
print(title_of_event[0].text.strip())
sort_of_event = root.xpath(
    "/html/body/main/div[3]/section[1]/div[2]/div[3]/article[1]/div/h5[3]")
print(sort_of_event[0].text.strip())
content_of_event = root.xpath(
    "/html/body/main/div[3]/section[1]/div[2]/div[3]/article[1]/div/div[1]/p[2]")
print(content_of_event[0].text.strip())
