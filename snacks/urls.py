from django.urls import path
from .views import SnacksList, SnackDetail, PostsList ,PostDetail

urlpatterns = [
    path('', SnacksList.as_view(), name='snacks_list'),
    path('<int:pk>/', SnackDetail.as_view(), name='snack_detail'),
    path('post/', PostsList.as_view(), name='posts_list'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
]