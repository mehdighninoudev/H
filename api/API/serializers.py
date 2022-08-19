from rest_framework import serializers 
from api.models import NewsDetail 

class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsDetail 
        fields = "__all__"