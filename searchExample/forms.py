from haystack.forms import SearchForm
from django.forms import ModelForm
from models import UserProfile
from django.contrib.auth.models import User

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
