import datetime
import requests
import lxml.html

months = ["January", "Febuary", "March", "April", "May",
          "June", "July", "August", "September", "October", "November", "December"]

# データベース用リスト
time_list = []
title_list = []
sort_list = []
content_list = []

r = requests.get("https://coinmarketcal.com/")
html = r.text
root = lxml.html.fromstring(html)

events = root.cssselect('.content-box')

for event in events:
    time_of_event = (event.xpath("div/h5[1]/strong"))[0].text.strip()
    title_list.append((event.xpath("div/h5[2]/strong"))[0].text.strip())
    sort_list.append((event.xpath("div/h5[3]"))[0].text.strip())
    content_list.append((event.xpath("div/div[1]/p[2]"))[0].text.strip())

    # DATE型に変換
    splited_text = time_of_event.split()
    for i, month in enumerate(months):
        if splited_text[1].find(month) != -1:
            time_date_type = datetime.date(2018, i + 1, int(splited_text[0]))
            strtime = time_date_type.strftime('%Y-%m-%d')
            time_list.append(strtime)
            break
