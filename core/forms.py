from django.forms import ModelForm
from .models import AdminTable

class LoginForm(ModelForm):
    class Meta:
        model = AdminTable
        fields = '__all__'