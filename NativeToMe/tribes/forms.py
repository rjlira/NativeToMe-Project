from django import forms
from .models import Tribe

"""Create tribe Form"""
class createTribeForm(forms.Form):
    fields = ['tribeName', 'location', 'privacyMode', 'description']
    tribeName = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length=100)
    location = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length=50)
    choices = [('Public', 'Public'), ('Private', 'Private')]
    privacyMode = forms.ChoiceField(choices=choices)
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

    """Search for a tribe"""
class searchTribeForm(forms.Form):
    searchField = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100)


class editTribeForm(forms.Form):
    fields = ['tribeName','description']
    tribeName = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length=100 )
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

class createTribePostForm(forms.Form):
    fields = ['title', 'description']
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    #image = forms.ImageField(widget=forms.ImageField)

class requestToJoin(forms.Form):
    fields = ['message']
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))