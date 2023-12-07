from django.shortcuts import render
from .serilaizer import UploadPdfSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from .sample import *
from rest_framework.response import Response
from rest_framework import status
import base64
from .openai import *
import concurrent.futures
import os


class UploadPdf(CreateAPIView):
    serializer_class = UploadPdfSerializer
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        try:
            output = []
            files = request.FILES.getlist('files')
            with concurrent.futures.ThreadPoolExecutor() as executor:
                for file in files:
                    data = {"pdf":file}
                    serializers = UploadPdfSerializer(data=data)
                    if serializers.is_valid():
                        path_instance = serializers.save()
                        executor.submit(pdf_text_extract, path_instance.pdf.path,path_instance.id)
                        os.remove(path_instance.pdf.path)
            return Response({'status_code': status.HTTP_200_OK,
                             'status': 'success',
                             })
        except Exception as e:
            return Response({'status_code': status.HTTP_400_BAD_REQUEST,
                             'status': 'failure',
                             'message': str(e)})


class Openai(CreateAPIView):
    serializer_class = UploadPdfSerializer
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        try:
            output = []
            files = request.FILES.getlist('files')
            with concurrent.futures.ThreadPoolExecutor() as executor:
                for file in files:
                    data = {"pdf":file}
                    serializers = UploadPdfSerializer(data=data)
                    if serializers.is_valid():
                        path_instance = serializers.save()
                        result = executor.submit(get_text, path_instance.pdf.path)
                        output.append(result.result())
                        os.remove(path_instance.pdf.path)
            return Response({'status_code': status.HTTP_200_OK,
                             'status': 'success',
                             'result':output})
        except Exception as e:
            return Response({'status_code': status.HTTP_400_BAD_REQUEST,
                             'status': 'failure',
                             'message': str(e)})






