from bs4 import BeautifulSoup
import requests
import time

# https://www.yellowpages.com.au/


def save_result(line, filename):

    result = str(line)

    try:
        file = open(filename,'at')
    except IOError as e:
        print('error opening file')
    else:
        with file:
            file.write(result + '\n')
            file.close()


urls = [
  "https://www.yellowpages.com.au/search/listings?locationClue=&lat=&lon="
  ]

categories = [
  'Restaurants',
  'Doctors',
  'Dentists',
  'Mechanics',
  'Plumbers',
  'Hairdressers',
  'Solicitors',
  'Beauty+Salons',
  'Builders',
  'Florists',
  'Pharmacies'
]

cookies = {'JSESSIONID': 'CC782A7912E4579DF4B77D353F09886C',
           'yellow-guid': '97a533b7-46fa-4de0-9ca0-fefbe10f26d4',
           '_qst_s': '2',
           '_qsst_s': '1522827815818',
           's_fid': '2DBEED4D060E56D8-39301792CC9BD4D9',
           's_cc': 'true',
           'aam_uuid': '89170050751432820370829039961917661793'
           }

headers = {
    'Host': 'www.yellowpages.com.au',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

for category in categories:

    pageNumber = 0
    while True:
        time.sleep(3)

        pageNumber += 1

        payload = {'clue': category,
                   'eventType': 'pagination',
                   'pageNumber': pageNumber,
                   'referredBy': 'www.yellowpages.com.au'}

        rsps = requests.get(url=urls[0], cookies=cookies, headers=headers, params=payload)

        print(rsps.url)
        soup = BeautifulSoup(rsps.text, 'html.parser')

        soup.find_all("a", attrs={"class": "contact contact-main contact-email "})

        for i in soup.find_all("a", attrs={"class": "contact contact-main contact-email "}):
            save_result(i.get('data-email'), str(category + '.txt'))

        i = soup.find("a", attrs={"class": "pagination navigation", "data-page": pageNumber + 1})
        print("Category -", category, "  Page -", pageNumber)

        if i:
            if i.string == 'Next »':
                continue
    break




