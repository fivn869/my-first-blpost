from .models import Profile, Poost
from django import forms
from django.forms import fields
from django.forms.widgets import Textarea

class FileForm(forms.ModelForm):

    class Meta:
        model = Profile

        fields = ['description','occupy']

        widgets = {
            'description':forms.TextInput(
                attrs={'placeholder':'please input your introduction'}
            ),
            'occupy':forms.TextInput(
                attrs={'placeholder':'what is your occupy'}
            )
        }

        error_messages = {
            'description':{'required':'could not be blank'},
        }


class poost(forms.Form):

    title = fields.CharField(
                             max_length=20,
                             min_length=4,
                             required=True,
                             label='title',
                             widget=forms.TextInput(attrs={'placeholder':'no more than 20'}),
        error_messages={'min_length':'more than 4', 'max_length':'less than 20'},
                             )

    post = fields.CharField(
                            max_length=258,
                            required=True,
                            label='post',
                            widget=forms.widgets.Textarea(attrs={'placeholder':'give us your idea'}),
        error_messages={'required':'must more than 258'},
                            )


    def clean(self):

        title = self.cleaned_data.get('title','')
        content = self.cleaned_data.get('post','')
        print("processing clean")
        if not title:
            raise forms.ValidationError('title could not be null')