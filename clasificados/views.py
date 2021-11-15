from . import utils, repository
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from . models.articleItem import ArticleItem


def update_scraper(request):    
    try:
        content_list = utils.get_content_from_scraper()
        repository.save_data_to_database(content_list)
        messages.add_message(request, messages.INFO,
                             _('Información actualizado correctamente.'))
    except:
        messages.add_message(request, messages.ERROR,
                             _('No se pudo actualizar la información.'))
    return HttpResponseRedirect(reverse(f'admin:clasificados_{ArticleItem.__name__.lower()}_changelist'))
