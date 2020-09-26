from dal_admin_filters import AutocompleteFilter

class UserFilter(AutocompleteFilter):
	title = 'User'
	field_name = 'user'
	autocomplete_url = 'user-autocomplete'