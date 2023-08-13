import requests
from bs4 import BeautifulSoup
import fake_headers
import json

keywords = ['Django', 'Flask', 'django', 'flask']
result = []

header_gen = fake_headers.Headers(browser='chrome', os='win')

response = requests.get('https://spb.hh.ru/search/vacancy?'
                        'area=1&area=2&search_field=name&search'
                        '_field=company_name&search_field=description&enable_'
                        'snippets=true&text=python&L_save_area=true',
                        headers=header_gen.generate())
html_response = response.text

soup = BeautifulSoup(html_response, 'lxml')
tag_main = soup.find('div', id='a11y-main-content')

job_list = tag_main.find_all('div', class_='serp-item')

for job in job_list:

    href = job.find('a', class_='serp-item__title')
    refer = href["href"]
    job_name = href.text
    try:
        salary = job.find('span', class_='bloko-header-section-2')
        salary_name = salary.text
    
    except:
        salary_name = 'not specified'
    
    job_descr = job.find('div', class_='g-user-content')
    divs = job_descr.find_all('div', class_='bloko-text')
    div_text = ''
    for div in divs:
        
        div_text += div.text

    company = job.find('a', class_='bloko-link bloko-link_kind-tertiary')    

    for element in keywords:
        if element in div_text:

            result.append({
                'href': refer,
                'job': job_name,
                'salary': salary_name,
                'descr': div_text,
                'company': company.text

            })
            break

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=4)