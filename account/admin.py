from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import User
from account.forms import UserForm, SignUpForm

class AccountAdmin(UserAdmin):
	add_form = SignUpForm
	form = UserForm
	list_display = (
		'username', 
		'first_name', 
		'last_name', 
		'email', 
		'date_joined', 
		'last_login', 
		'is_active',
		'is_admin',
		'is_superuser')
	search_fields = ('username', 'email', 'first_name', 'last_name')
	readonly_fields = ('date_joined', 'last_login', 'id')

	list_filter = ()
	fieldsets = ()
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('first_name', 'last_name', 'email', 'username', 'password1', 'password2',)
		}),
	)

admin.site.register(User, AccountAdmin)