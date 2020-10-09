from django import forms
"""Create edit profile form"""
class editProfileForm(forms.Form):
    fields = ['school', 'hobbies', 'location', 'bio', 'likes', 'dislikes', 'image']
    school = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length=100 )
    hobbies = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100)
    location = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length=50)
    bio = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    #test#
    likes = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length=100)
    dislikes = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length=100)
    #test#
    image = forms.ImageField()
    



