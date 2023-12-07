from django.urls import path
from .views import *

urlpatterns = [
    path('Extract/',UploadPdf.as_view()),
    path('openai/',Openai.as_view()),
]