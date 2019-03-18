from flask import Flask, jsonify
import requests
import xmltodict
from models import Lexology, db

from bs4 import BeautifulSoup

POSTGRES = {
    'user': 'postgres',
    'pw': 'Sakura23!',
    'db': 'app',
    'host': 'localhost',
    'port': '5432',
}

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db.init_app(app)

@app.route("/")
def load():
    #chambers = 'https://chambers.com/sitemap/index'
    #lexology = 'https://www.lexology.com/firms/sitemap.xml'
    #xml = requests.get(lexology).content
    #content_dict = xmltodict.parse(xml)
    #urls = []
    #for i in content_dict['urlset']['url']:
    #    urls.append(i['loc'])
    #for url in urls:
    #print(urls[0])
    #content = requests.get(urls[0]).content
    #b4s = BeautifulSoup(content, 'html.parser')
    profile = b4s.find_all('div', class_='profile-details')
    #lex = Lexology()
    #lex.id = 1
    #lex.name = 'pepe'
    #db.session.add(lex)
    #db.session.commit()
    return ''


if __name__ == "__main__":
    app.run(host='0.0.0.0')
