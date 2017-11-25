
from django.conf.urls import url
from django.contrib import admin
from app import views

urlpatterns = [
    url(r'^help/', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
]
