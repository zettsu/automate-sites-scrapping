import requests as requests
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import JSON, TEXT
import json
import requests
import xmltodict
from flask_migrate import Migrate

from bs4 import BeautifulSoup

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Sakura23!@localhost:5432/app'

db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)


class Lexology(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    profile_info = db.Column(TEXT)
    social = db.Column(JSON)


@app.route("/")
def load():
    lexology = 'https://www.lexology.com/firms/sitemap.xml'
    xml = requests.get(lexology, headers={'Connection':'close'}).content
    requests.session().close()
    content_dict = xmltodict.parse(xml)
    urls = []

    for i in content_dict['urlset']['url']:
        urls.append(i['loc'])

    for url in urls:
        id = url
        content = requests.get(urls[0], headers={'Connection':'close'}).content
        requests.session().close()

        b4s = BeautifulSoup(content, 'html.parser')
        profile = b4s.find('div', attrs={'class': 'profile-details'})
        profile_info = b4s.find('div', attrs={'class': 'profileText RhsContent'}).find_all('p')

        social_networks = b4s.find('ul', attrs={'class': 'SocialLinks'}).find_all('a')

        josn_social = {}
        for social in social_networks:
            url_site = requests.get(social['href'] , headers={'Connection':'close'}).url
            josn_social[social['class'][0]] = url_site
            requests.session().close()

        url_site = profile.find('a', attrs={'class', 'contributor-logo'})['href']
        lex = Lexology()
        lex.id = str(id)
        lex.profile_info = str(profile_info)
        lex.social = json.dumps(josn_social, ensure_ascii=False)
        db.session.add(lex)
        db.session.commit()

    return 'suceess'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
