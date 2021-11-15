from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _
from . category import Category


class Subcategory(models.Model):
    """
    Almacena las subcategorias
    """
    class Meta:
        verbose_name = _('Sub Categoria')
        verbose_name_plural = _('Sub Categorias')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name=_("Nombre"))
    url = models.CharField(null=True, blank=True,
                           max_length=200, verbose_name=_("Url"), default=None)

    def __str__(self):
        return '%s' % (self.name,)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')


admin.site.register(Subcategory, SubCategoryAdmin)
