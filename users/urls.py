from django.urls import path
from .views import BlogUserApiView


urlpatterns = [
    path('signup', BlogUserApiView.as_view(), name='create-user'),
]