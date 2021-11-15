from .models.category import Category
from .models.subcategory import Subcategory
from .models.articleItem import ArticleItem
from .constants import ARTICLES, URL, NAME, DESCRIPTION, PRICE, LOCATION, IMAGE_URL, SUB_CATEGORIES


def save_data_to_database(content_list):
    """
    Guarda la informacion en la base de datos
    """
    Category.objects.all().delete()
    Subcategory.objects.all().delete()
    ArticleItem.objects.all().delete()
    for category in content_list:
        categorydb = Category.objects.create(
            name=category.get(NAME),
            url=category.get(URL))
        categorydb.save()
        for article in category.get(ARTICLES):
            ArticleItem.objects.create(category=categorydb,
                                       name=article.get(NAME),
                                       description=article.get(DESCRIPTION),
                                       price=article.get(PRICE),
                                       location=article.get(LOCATION),
                                       image_url=article.get(IMAGE_URL)).save()
        for subcategory in category.get(SUB_CATEGORIES):
            Subcategory.objects.create(
                category=categorydb,
                name=subcategory.get(NAME),
                url=subcategory.get(URL)).save()
