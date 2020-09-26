from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView

from account.models import User
from account.api.serializer import (
	RegistrationSerializer, 
	LoginSerializer,
	 UserSerializer
)
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

@api_view(['POST',])
def registration_view(request):

	serializer = RegistrationSerializer(data = request.data)
	data = {}
	if serializer.is_valid():
		user = serializer.save()
		data['error'] = False
		data['message'] = "Successfully registered new user"
		data['username'] = user.username
		data['token'] = Token.objects.get(user=user).key
		data['email'] = user.email
		return Response(data=data, status=status.HTTP_200_OK)
	else:
		data = serializer.errors
		return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

class ObtainAuthTokenView(APIView):

	authentication_classes = []
	permission_classes = []

	def post(self, request, format="json"):
		context = {}

		# Only form data is available in request.POST
		username = request.POST.get('username')
		password = request.POST.get('password')
		account = authenticate(username=username, password=password)
		if account:
			serializer = LoginSerializer(account)
			try:
				token = Token.objects.get(user=account)
			except Token.DoesNotExist:
				token = Token.objects.create(user=account)
			serializer.data['token'] = token.key
		else:
			context['error'] = True
			context['message'] = 'Invalid credentials'
			return Response(context)
		return Response(serializer.data)

		
class ApiUserListView(ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	pagination_class = None