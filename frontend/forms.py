from collections.abc import Mapping
from typing import Any
from django import forms
from django.forms.utils import ErrorList
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class LoginForm(forms.Form):
    email = forms.CharField(
        label='Email',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'wider-input'}))
    password = forms.CharField(label='Password', 
                               widget=forms.PasswordInput(attrs={'class':'wider-input'})
                               )
    


class WriteName(forms.Form):
    first_name = forms.CharField(label = 'First Name', max_length=100)
    fam_name = forms.CharField(label='Surename', max_length = 100)

class ExampleForm(forms.Form):
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = "id_exampleform"
        self.helper.form_class = "blueForms"
        self.helper.form_method = "post"
        self.helper.form_action = "submit_cred"
        
        self.helper.add_input(Submit('submit', "Submit"))
    
    username = forms.CharField(
        label='Username',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'wider-input'}))
    password = forms.CharField(label='Password', 
                               widget=forms.PasswordInput(attrs={'class':'wider-input'})
                               )