from django.contrib import admin
from django.urls import include,path
from first_app import views

admin.site.site_header = "Daksh Admin"
admin.site.site_title = "Daksh Admin Portal"
admin.site.index_title = "Welcome to Daksh Portal"

urlpatterns = [
    path('', views.index, name = 'index' ),
    path('about/', views.about, name = 'about' ),
    path('services/', views.services, name = 'services' ),
    path('contacts/', views.contacts, name='contacts'),
    path('help/', views.help, name='help'),
]
