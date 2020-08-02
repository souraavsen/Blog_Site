from django.urls import path
from . import views



urlpatterns = [
    path(r'', views.articles_list, name="list"),  # Called 'views.articles_list'
    path(r'create/', views.create_article, name="create"),
    path('<slug:article_name>/', views.articles_detailes, name="detail"),
]
