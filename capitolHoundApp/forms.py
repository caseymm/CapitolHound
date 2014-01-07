from haystack.forms import SearchForm
from django.forms import ModelForm
from models import UserProfile, SaveThisSearch
from django.contrib.auth.models import User
from django import forms

class NotesSearchForm(SearchForm):

    def no_query_found(self):
        return self.searchqueryset.all()

class UserForm(ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['topics']

class SaveThisSearchForm(ModelForm):
    class Meta:
        model = SaveThisSearch
        fields = ['saved_searches']

#class SaveThisSearchForm(forms.Form):
#    saved_searches = forms.CharField(max_length=1000)
