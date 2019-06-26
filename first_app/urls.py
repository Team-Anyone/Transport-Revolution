from django.conf.urls import url
from first_app import views

app_name= 'first_app'

urlpatterns=[
        url(r'^$',views.homepage,name='homepage'),
        url(r'^description/$',views.description,name='description'),
        url(r'^case_study/$',views.case_study,name='case_study'),
]
