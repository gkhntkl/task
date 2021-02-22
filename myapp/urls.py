

from django.urls import path
from .views import *

urlpatterns = [
    path('query/', GetQueryAPIView.as_view()),
    path('input/', PostQueryAPIView.as_view()),
]
