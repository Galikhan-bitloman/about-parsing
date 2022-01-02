import requests
from bs4 import BeautifulSoup as bs
from string import whitespace

""" divide into two def where first parse only number second only amount price to insert db cause 
i have little trouble with it"""


def get_number_from_site(n):
    data_list = []
    for i in range(1, n):
        url_temp = 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?pageNumber=' + str(i)
        r = requests.get(url_temp)
        soup = bs(r.text, "html.parser")
        number = soup.find_all('div', class_="registry-entry__header-mid__number")

        for j in number:
            get_links = j.a['href']
            get_number_from_links = get_links.split('=')[-1]
            data_list.append(get_number_from_links)

    return data_list


def get_amountprice_from_site(n):
    data_list1 = []
    for i in range(1, n):
        url_temp = 'https://zakupki.gov.ru/epz/order/extendedsearch/results.html?pageNumber=' + str(i)
        r = requests.get(url_temp)

        soup = bs(r.text, "html.parser")
        amount = soup.find_all('div', class_="price-block__value")

        for i in amount:
            get_amount = i.text
            get_clean_amount = get_amount.replace(u'\xa0', '').replace(u'\xa0', '').replace(u'\r\n',
                                                                                            '')  # replace(u'₽                        ', '₽')
            get_clean_amount.translate(whitespace)
            data_list1.append(get_clean_amount)

    return data_list1



