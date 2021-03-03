from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Complete

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length = 150)
    last_name = forms.CharField(max_length = 150)
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class NewForm(forms.ModelForm):

    class Meta:
        model = Complete
        fields = ['user','address','bio','avatar']

        widgets = {
            'user':forms.TextInput(attrs={'class':'form-control','value':'','id':'user','type':'hidden'}),
            'bio':forms.Textarea(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'})
        }
    
class UpdateForm(UserChangeForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length = 150)
    last_name = forms.CharField(max_length = 150)
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
    