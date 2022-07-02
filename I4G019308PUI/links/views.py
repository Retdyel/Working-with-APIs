from rest_framework import generics
from .serializers import LinkSerializer
from .models import Link


# Create your views here.
class PostListAPI(generics.ListAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
    
class PostCreateAPI(generics.CreateAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
    
class PostDetailAPI(generics.RetrieveAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer
    
class PostUpdateAPI(generics.UpdateAPIView):
    queryset = Link.object.filter(active=True)
    serializer_class = LinkSerializer
    
class PostDeleteAPI(generics.DestroyAPIView):
    queryset= Link.objects.filter(active=True)
    serializer_class = LinkSerializer