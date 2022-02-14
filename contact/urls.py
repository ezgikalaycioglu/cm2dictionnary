from . import views #from current location import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.contact_view, name='contact_view'),
    #path('success',views.SuccessView, name='contact_success_view')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
