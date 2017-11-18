from bs4 import BeautifulSoup
from lxml.html.soupparser import fromstring

url = open("responce_example.html", "r", encoding='utf-8')

soup = BeautifulSoup(url, "html.parser")
# soup = soup.prettify()

# for days in soup.find_all("i", "fare-finder__calendar__days__day__date"):
#     print(days.get_text())

for prices in soup.find_all("div", "fare-finder__calendar__days__day__container"):
    print(prices.get_text())
# price = soup.find_all("li", "fare-finder__calendar__days__day")
# price = soup.find_all("p", "fare-finder__calendar__days__day__label fare-finder__calendar__days__day__label--price-tiny")
#
# pricelist = str(price)
#
# list = pricelist.split(',')

# list = ""
# for p in pricelist:
#
#     if p == ',':
#         list = list + list.join('\n')
#     else:
#         list = list + list.join(p)

# list1 = list.xpath('//p[@class="fare-finder__calendar__days__day__label fare-finder__calendar__days__day__label--price-tiny"]/text()')

# print(days)



# print(str(days).split(","))
# print(str(price).split(","))

# print(str(price))