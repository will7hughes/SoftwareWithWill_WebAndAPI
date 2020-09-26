from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status

def home_view(request):
	
	response = render(request, "personal/home.html")
	return response

def does_not_exist_reponse(model):
	data = {}
	data["response"] = "" + model + " does not exist"
	return Response(
		status=status.HTTP_404_NOT_FOUND, 
		data=data
	)