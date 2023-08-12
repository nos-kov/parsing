import requests
from bs4 import BeautifulSoup
import fake_headers
import re


header_gen = fake_headers.Headers(browser='chrome', os='win')

result = []

response = requests.get('https://spb.hh.ru/search/vacancy?text=python&area=1&area=2', headers=header_gen.generate())
html_response = response.text

soup = BeautifulSoup(html_response, 'lxml')
tag_main = soup.find('div', id='a11y-main-content')

job_list = tag_main.find_all('div', class_='serp-item')

for job in job_list:

    href = job.find('a', class_='serp-item__title')
    refer = href["href"]
    job_name = href.text
    #try:
    salary = job.find('span', class_='bloko-header-section-2')
    salary_name = salary.text
        #test = salary_name.decode("utf-8")
#    test = salary_name.encode('ascii')
    #re.sub('u', '', salary_name)
    #except:
    salary_name = 'not specified'
    result.append({
        'href': refer,
        'job': job_name,
        'salary': salary_name

    })

print(result)