from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views

app_name = 'catalog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'signup', views.signup, name='signup'),
    url(r'botm', views.BookOfTheMonthView.as_view(), name='botm')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)