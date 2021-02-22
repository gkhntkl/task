from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction

from .models import MyApp

class GetQueryAPIView(APIView):


    def get(self, request):

        if 'key' in request.data:
            key = request.data['key']
            data = MyApp.objects.filter(key=key).first()
            count = 0
            if data:
                count = data.count

            response = {
                'key':request.data['key'],
                'count':count
            }
            return Response(response,status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)



class PostQueryAPIView(APIView):

    @transaction.atomic
    def post(self, request):

        if 'key' in request.data:
            key = request.data['key']
            data = MyApp.objects.filter(key=key).first()
            if data:
                data.count = data.count + 1
                data.save()
            else:
                data = MyApp.objects.create(key=key,count=1)


            return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

