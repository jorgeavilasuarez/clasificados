from bs4 import BeautifulSoup
import requests
from . constants import(SUBCATEGORY_SELECTOR, CATEGORY_SELECTOR,
                        BOX_SELECTOR, BASE_URL, HEADERS, NAME, URL,
                        SUB_CATEGORIES, ARTICLES, HREF, DESCRIPTION,
                        PRICE, IMAGE_URL, LOCATION, SRC, HTML_PARSER,
                        ARTICLE_BOX_SELECTOR, ARTICLE_PRICE_SELECTOR,
                        ARTICLE_TITLE_SELECTOR, ARTICLE_DESCRIPTION_SELECTOR,
                        ARTICLE_LOCATION_SELECTOR, ARTICLE_IMG_SELECTOR)


def get_content_from_scraper(url=BASE_URL):
    """
    Obtiene la informacion del scraper
    """
    content_list = []
    session = requests.Session()
    session.headers = HEADERS
    page = session.get(url)
    soup = BeautifulSoup(page.content, HTML_PARSER)
    box_category_list = soup.select(BOX_SELECTOR)
    for category in box_category_list:
        category_obj = category.select_one(CATEGORY_SELECTOR)
        category_name = category_obj.text
        category_link = category_obj.attrs.get(HREF)
        sub_categories = [(sub_categorie.text, sub_categorie.attrs.get(HREF))
                          for sub_categorie in category.select(SUBCATEGORY_SELECTOR)]
        category_item = {
            NAME: category_name,
            URL: category_link,
            SUB_CATEGORIES: [],
            ARTICLES: []}
        content_list.append(category_item)
        category_item[ARTICLES] = get_articles(
            session,
            f'{url}{category_link}')
        for sub_category_name, sub_category_link in sub_categories:
            category_item[SUB_CATEGORIES].append({
                NAME: sub_category_name,
                URL: sub_category_link})

    return content_list


def get_articles(session, url):
    """"
    Obtiene los articulos del escraper
    """
    articles_list = []
    page = session.get(url)
    soup = BeautifulSoup(page.content, HTML_PARSER)
    for article_html in soup.select(ARTICLE_BOX_SELECTOR):
        price = article_html.select_one(ARTICLE_PRICE_SELECTOR)
        title = article_html.select_one(ARTICLE_TITLE_SELECTOR)
        description = article_html.select_one(ARTICLE_DESCRIPTION_SELECTOR)
        location = article_html.select_one(ARTICLE_LOCATION_SELECTOR)
        img = article_html.select_one(ARTICLE_IMG_SELECTOR)
        articles_list.append({
            NAME: title.text if not title is None else str(),
            DESCRIPTION: description.text if not description is None else str(),
            LOCATION: location.text if not location is None else str(),
            PRICE: price.text if not price is None else str(),
            IMAGE_URL: img.attrs.get(SRC) if not img is None else str(),
        })

    return articles_list
