from django import forms
from django.contrib.auth.models import User
from gro_app.models import UserProfile, GroceryItem

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone_number','address')

class GroceryItemForm(forms.ModelForm):
    TYPE_SELECT = (('bought', 'bought'),('left', 'left'),('available','available'),)
    flag = forms.CharField(widget=forms.RadioSelect(choices=TYPE_SELECT))
    class Meta:
        model = GroceryItem
        fields = ('item_name','flag','quantity','date',)