from django.contrib import admin
from django.urls import path, include
admin.site.site_header = 'Welcome to my world'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("crudapp.urls")),
]
