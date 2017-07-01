from django.conf.urls import  url
from . import views

urlpatterns =[
    url('^$',views.index,name='index'),
    url('^about/$',views.about,name='about'),
    url('^contact/$',views.contact,name='about'),
    url('^social/$',views.social,name='social'),
    url('^git/$',views.git,name='git'),
]