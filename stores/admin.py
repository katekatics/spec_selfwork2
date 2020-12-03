from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import StoreChangeForm, StoreCreationForm
from .models import Store


class StoreAdmin(UserAdmin):
    add_form = StoreCreationForm
    form = StoreChangeForm
    model = Store
    list_display = [
        'username', 'email', 'inn', 'year_open',
    ]


admin.site.register(Store, StoreAdmin)
