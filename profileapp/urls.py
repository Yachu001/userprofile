from django.urls import path
from .views import list_userprofile,detail_userprofile
urlpatterns=[
    path('',list_userprofile.as_view(),name='list'),
    path('detail/<int:pk>/',detail_userprofile.as_view(),name='detail'),
]