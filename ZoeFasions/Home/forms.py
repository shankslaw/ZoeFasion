from django.forms import ModelForm
from . models import product

class ProductForm(ModelForm):
    class Meta :
        model = product
        fields = '__all__'