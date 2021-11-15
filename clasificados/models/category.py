from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html


class Category(models.Model):
    """
    Almacena las categorias
    """
    class Meta:
        verbose_name = _('Categoria')
        verbose_name_plural = _('Categorias')
    name = models.CharField(max_length=200, verbose_name=_("Nombre"))
    url = models.CharField(null=True, blank=True,
                           max_length=200, verbose_name=_("Url"), default=None)

    def __str__(self):
        return '%s' % (self.name,)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Category, CategoryAdmin)
