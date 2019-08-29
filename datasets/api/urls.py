
from django.urls import path
from .views import DataView, FileView

urlpatterns = [
    path('files/', FileView.as_view()),
    path('data/', DataView.as_view()),
    
]
