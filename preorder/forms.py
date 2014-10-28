from django.forms import ModelForm
from preorder.models import Customer

class CustomerForm(ModelForm):
    class Meta:
        model = Customer