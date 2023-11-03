from django.urls import path
from . import views


urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.BookListView.as_view(), name='index'),
    # path('api/', views.BookListAPIView.as_view())
]




