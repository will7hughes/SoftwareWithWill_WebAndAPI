from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from account.models import User

from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator

username_validator = UnicodeUsernameValidator()

class UserAuthenticationForm(forms.ModelForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username', 'password')

	def clean(self):
		if self.is_valid():
			username = self.cleaned_data['username']
			password = self.cleaned_data['password']
			if not authenticate(username=username, password=password):
				raise forms.ValidationError("Invalid login")

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_admin', 'is_superuser']



class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=12, min_length=4, required=True, help_text='Required: First Name',
								widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
	last_name = forms.CharField(max_length=12, min_length=4, required=True, help_text='Required: Last Name',
								widget=(forms.TextInput(attrs={'class': 'form-control'})))
	email = forms.EmailField(max_length=50, help_text='Required. Inform a valid email address.',
								widget=(forms.TextInput(attrs={'class': 'form-control'})))
	password1 = forms.CharField(label=_('Password'), widget=(forms.PasswordInput(attrs={'class': 'form-control'})),
								help_text=password_validation.password_validators_help_text_html())
	password2 = forms.CharField(label=_('Password Confirmation'), widget=forms.PasswordInput(attrs={'class': 'form-control'}),
								help_text=_('Just Enter the same password, for confirmation'))
	username = forms.CharField(
		label=_('Username'),
		max_length=150,
		help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
		validators=[username_validator],
		error_messages={'unique': _("A user with that username already exists.")},
		widget=forms.TextInput(attrs={'class': 'form-control'})
	)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

class UserCreateForm(UserCreationForm):
	email = forms.EmailField(required = True)

	class Meta(UserCreationForm):
		model = User
		fields = ('username', 'email', 'password', 'password2',)

	def clean_password2(self):
		password = self.cleaned_data.get("password")
		password2 = self.cleaned_data.get("password2")
		if password and password2 and password != password2:
			raise forms.ValidationError(
				self.error_messages['password_mismatch'],
				code='password_mismatch',
			)
			return password2

	def save(self, commit=True):
		user=super(UserCreationForm, self).save(commit=False)
		user.set_password(self.clean_password2())
		# user.insurance_id = self.cleaned_data["insurance_id"]
		# user.insurance_provider = self.cleaned_data["insurance_provider"]
		if commit:
			user.save()
		return user