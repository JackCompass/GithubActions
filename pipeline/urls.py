from django.urls import path
from pipeline import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('viewlist', views.list, name = 'viewlist'),
	path('person', views.person, name = 'person'),
]
