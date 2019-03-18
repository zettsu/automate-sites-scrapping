import requests
import xmltodict
import json
from bs4 import BeautifulSoup

chambers = 'https://chambers.com/sitemap/index'
lexology = 'https://www.lexology.com/firms/sitemap.xml'
xml = requests.get(lexology).content
content_dict = xmltodict.parse(xml)

urls = []
for i in content_dict['urlset']['url']:
    urls.append(i['loc'])
#for url in urls:
print(urls[0])
content = requests.get(urls[0]).content
b4s = BeautifulSoup(content, 'html.parser')
profile = b4s.find('div', attrs = {'class':'profile-details'} )
profile_info = b4s.find('div', attrs={'class':'profileText RhsContent'}).find_all('p')

social_networks = b4s.find('ul', attrs={'class':'SocialLinks'}).find_all('a')

for social in social_networks:
    print(social['class'][0])
    print(requests.get(social['href']).url)



url_site =profile.find('a', attrs={'class', 'contributor-logo'})['href']
#print(profile.find('a', attrs={'class': 'contributor-logo'}))
#print(profile.find_all('a', class_='contributor-logo'))