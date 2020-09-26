from rest_framework import serializers

from account.models import User
from rest_framework.authtoken.models import Token


class RegistrationSerializer(serializers.ModelSerializer):

	confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

	class Meta:
		model = User
		fields = ['username', 'email', 'password', 'confirm_password']
		extra_kwargs = {
			'password': {'write_only': True}
		}

	def save(self):
		user = User(
			username = self.validated_data['username'],
			email = self.validated_data['email'],
		)
		password = self.validated_data['password']
		confirm_password = self.validated_data['confirm_password']

		if password != confirm_password:
			raise serializers.ValidationError({'password': 'Passwords must match'})
		user.set_password(password)
		user.save()

		return user


class LoginSerializer(serializers.ModelSerializer):
	api_key = serializers.SerializerMethodField('get_token')

	class Meta:
		model = User
		fields = ['id', 'username', 'email', 'api_key', 'is_active', 'is_admin', 'is_superuser', 'updated_date']

	def get_token(self, user):
		token = Token.objects.get(user=user)
		return token.key


class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ['id', 'username', 'email', 'is_active', 'is_admin', 'is_superuser', 'updated_date']