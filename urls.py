from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name="home"),
    path("merge",views.new,name="merge"),
    path("about",views.about,name="about"),
    path("ser",views.services,name="services"),
    path("cont",views.contacts,name="contacts"),
    path("checkbox",views.checkbox,name="checkbox"),
    path("import_file",views.import_file,name="import_file"),
    path('merge_csv/', views.merge_datasets, name='merge_csv'),
    path('download_merged_dataset/', views.download_merged_dataset, name='download_merged_dataset'),
]

