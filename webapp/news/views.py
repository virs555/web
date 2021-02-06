from flask import Blueprint, render_template, current_app

from webapp.weather import weather_by_city
from webapp.news.models import News

blueprint = Blueprint('news', __name__)

@blueprint.route('/')
def index():
    page_title = 'Новости Python'
    weather = weather_by_city(current_app.config['WEATHER_DEFAULT_CITY'])
    news_list = News.query.order_by(News.published.desc()).all()
    return render_template('news/index.html', title=page_title, weather=weather, news_list=news_list)