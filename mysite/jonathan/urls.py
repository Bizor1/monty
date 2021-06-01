from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    url(r'^$', views.HomePageView.as_view(), name='home'), # Notice the URL has been named
    url(r'^about/$', views.AboutPageView.as_view(), name='about'),
    url(r'^contact/$', views.ContactPageView.as_view(), name='contact'),
    url(r'^gallery/$', views.GalleryPageView.as_view(), name='gallery'),
    url(r'^our-history/$', views.OurHistoryPageView.as_view(), name='our-history'),
    url(r'^our-services/$', views.OurHistoryPageView.as_view(), name='our-services'),
    url(r'^premium/$', views.PremiumPageView.as_view(), name='premium'),
    url(r'^404notfound/$', views.PremiumPageView.as_view(), name='404notfound'),
]