from rest_framework.generics import ListAPIView
from api.models import NewsDetail
from api.API.serializers import NewsDetailSerializer

class NewsDetailView(ListAPIView):
    queryset = NewsDetail.objects.all()
    serializer_class = NewsDetailSerializer