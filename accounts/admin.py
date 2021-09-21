from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Accounts
# Register your models here.

class AccountAdmin(UserAdmin):
  list_display = ('email', 'date_joined', 'last_login')
  search_fields = ('email')
  readonly_fields = ('id', 'date_joined', 'last_login' 'is_admin')

  filter_horizontal = ()
  list_filter =()
  fieldsets = ()

admin.site.register(Accounts, AccountAdmin)