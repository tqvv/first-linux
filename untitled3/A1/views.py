from django.shortcuts import render
from .models import Stream
from django.core import  serializers
from django.http import  HttpResponse,JsonResponse



# Create your views here
def get_ss(request):
#  ss=Stream.objects.all()
    ss=Stream.objects.filter(play='Y')
    response_data={}
    try:
        if(ss):
            response_data['result']='success'
            response_data['data']=serializers.serialize('json',ss)
        else:
            response_data['result'] = 'error'
            response_data['data'] = serializers.serialize('json', ss)
    except:
        response_data['result'] = 'exception'
        response_data['data'] =  'exception'
    return HttpResponse(JsonResponse(response_data),content_type='application/json')