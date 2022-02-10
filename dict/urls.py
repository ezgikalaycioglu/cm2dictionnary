from . import views #from current location import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.urls import URLPattern
from django.urls import include



urlpatterns = [
    path('',views.translator_view, name='translator_view'),
    path('all_terms',views.display_allterms, name='display_allterms_view'),
    path('search', views.search_allterms, name='search_allterms_view'),
    path('contact', views.contact_view, name='contact_view'),
    path('abbr', views.display_allabbrs, name='abbr_view'),
    path('searchabbr', views.search_allabbrs, name='search_abbr_view' )
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
