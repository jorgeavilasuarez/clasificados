from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from . category import Category


class ArticleItem(models.Model):
    """
    Almacena los articulos
    """
    class Meta:
        verbose_name = _('Articulo')
        verbose_name_plural = _('Articulos')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name=_("Nombre"))
    description = models.TextField()
    price = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    image_url = models.CharField(max_length=1000)

    @admin.display(description=_("Imagen"))
    def img_thumb(self):
        return format_html(
            '<img src={}></img>',
            self.image_url
        )

    def __str__(self):
        return '%s' % (self.name,)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', "description",
                    'price', 'location', 'img_thumb')
    list_filter = ('category', 'name')


admin.site.register(ArticleItem, ArticleAdmin)
