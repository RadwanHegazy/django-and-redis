from django.shortcuts import  HttpResponse
from rest_framework import decorators
from rest_framework.response import Response
from .models import NameModel
from .serializers import NameSerizlizer
from django.core.cache import cache


@decorators.api_view(['GET'])
def names (request)  :
    
    
    # getting data from cache
    if cache.get('names') == None :
        names = NameModel.objects.all()
        ser = NameSerizlizer(names,many=True)
        cache.set('names',ser.data)
        print('data comes from db')
        data = names
    else :
        data = cache.get('names')  
        print('data comes from redis caching')

    ser = NameSerizlizer(data,many=True)
    return Response(ser.data)