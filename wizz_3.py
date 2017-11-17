import win32com.client
from time import sleep
from bs4 import BeautifulSoup


def download_url_with_ie(url):
    ie = win32com.client.Dispatch("InternetExplorer.Application")
    ie.Visible = 0
    ie.Navigate(url)

    if ie.Busy:
        sleep(5)

    text = ie.Document.body.innerHTML
    ie.Quit()
    # page = html.fromstring(text.content)
    # page = text.xpath('//li[@title="fare-finder__calendar__monthly-prices__item"]/text()')
    soup = BeautifulSoup(text, "html.parser")
    for prices in soup.find_all("div", "fare-finder__calendar__days__day__container"):
        print(prices.get_text())


download_url_with_ie('https://wizzair.com/en-gb/flights/timetable/IEV/LCA#/0/0/2017-11/2017-12')
download_url_with_ie('https://wizzair.com/en-gb/flights/timetable/IEV/LCA#/0/0/2017-12/2017-12')