from django import forms
from .models import Clients


class ClientsForm(forms.ModelForm):

    class Meta:
        model = Clients
        fields = ["account_number", "first_name", "last_name", "middle_name",
                  "date_birth", "inn", "status", "manager"]