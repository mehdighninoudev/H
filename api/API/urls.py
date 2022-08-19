from django.urls import path 
from api.API.views import NewsDetailView

urlpatterns = [
    path('news', NewsDetailView.as_view())
]