from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index_myapp'),
    path('entery/<int:pk>', views.details, name='details_myapp'),
    path('entery/add', views.add, name='add_myapp'),
    path('entery/delete/<int:pk>', views.delete, name='delete_myapp'),
]