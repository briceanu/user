from .serializer import BlogUserSerializer
from rest_framework.generics import CreateAPIView 
from django.contrib.auth.models import User



class BlogUserApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = BlogUserSerializer





 


