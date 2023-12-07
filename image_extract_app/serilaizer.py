from rest_framework import serializers
from .models import *


class UploadPdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pdfs
        fields = '__all__'
