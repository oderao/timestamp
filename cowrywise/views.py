from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,render_to_response
from django.forms.models import model_to_dict

# Create your views here.
from django.http import HttpResponse,JsonResponse
from .serializers import TimeStampSerializer
from .models import TimeStamp
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
import string,random


def generate_uuid():

	import string,random

	key = string.ascii_lowercase + string.digits
	uuid = ""
	for i in range(30):
		uuid += random.choice(key)

	return uuid

def generate_timestamp():
	from datetime import datetime

	now = datetime.now().strftime("%d-%m-%Y %H:%M:%S.%s")
	return now



def timestamp_list(request):
	"""
	List all timestamps
	"""
	import json
	if request.method == 'GET':
		data = {'timestamp':generate_timestamp()}
		serializer = TimeStampSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
		list_of_time_stamps = TimeStamp.objects.all().order_by('-timestamp')
		serializer = TimeStampSerializer(list_of_time_stamps, many=True)
		if serializer.data:
			old_dict = json.loads(json.dumps(serializer.data))
			final_data = []
			for i in old_dict:
				final_data.append({
					i['timestamp']:generate_uuid()
					})
		
			return JsonResponse(final_data, safe=False)
		return JsonResponse({},safe=False)


