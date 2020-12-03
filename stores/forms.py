from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Store


class StoreCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Store
        fields = UserCreationForm.Meta.fields + (
            'email', 'inn', 'year_open',
        )


class StoreChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Store
        fields = UserChangeForm.Meta.fields
