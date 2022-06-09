from django.urls import path, re_path

from app import views

urlpatterns = [
    re_path(r'about/(?P<p_key>\d+)/', views.about, name='about'),
    re_path(r'about/contact', views.contact, name='contact'),
    path(r'', views.home, name='home'),
    path(r'search/', views.SearchHomePageView.as_view(), name='search'),
]
