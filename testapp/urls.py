from django.urls import path
from . import views

app_name = 'testapp'

urlpatterns = [
    path('', views.homepage),
    path('database/', views.database_update, name="database_update"),
    path('database/clear-database/', views.clear_database_but_images, name="clear_database"),
    path('database/clear-database-images/', views.clear_database_images, name="clear_database_images")
]