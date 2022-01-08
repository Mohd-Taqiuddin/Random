from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_event/', views.addEvent, name='add_event'),
    # path('sign_in/', views.sign_in, name='sign_in'),

]