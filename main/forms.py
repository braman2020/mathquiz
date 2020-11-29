from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from main.models import mquiz


class StartQuizForm(forms.Form):

    how_many_questions = forms.IntegerField(help_text="How many questions do you want (default=5) ?")

    def clean_renewal_date(self):
        data = self.cleaned_data['how_many_questions']

        # Check if a date is not in the past.
        if data < 0:
            raise ValidationError(_('Invalid number. Enter a number more than 0'))

        # Check if a date is in the allowed range (+4 weeks from today).
        if data > 10 :
            raise ValidationError(_('Invalid number. Enter a number greater than 10'))

        # Remember to always return the cleaned data.
        return data

class QuestionForm(forms.Form):
    def __init__(self,selection):
       self.selection = selection
       self.options = forms.ChoiceField(choices=selection,widget=forms.RadioSelect)

class CreateQuizForm(forms.ModelForm):

   def __init__(self, *args, **kwargs):
       super(forms.ModelForm, self).__init__(*args, **kwargs)
       # This is a way to override the labels on the html. Default is the
       # column name itself. But wee need it descriptive.
       self.fields['qdesc'].label = 'Question description'
       self.fields['qop1'].label = 'Option 1'
       self.fields['qop2'].label = 'Option 2'
       self.fields['qop3'].label = 'Option 3'
       self.fields['qop4'].label = 'Option 4'
       self.fields['qop5'].label = 'Option 5'
       self.fields['qans'].label = 'Correct option'
       self.fields['qhint'].label = 'Hint'
       self.fields['qsol'].label = 'Solution description'
       self.fields['qimage'].label = 'Select Image to Upload'
       self.fields['qhimg'].label = 'Select Image to Upload'
       self.fields['qsimg'].label = 'Select Image to Upload'

   class Meta(object):
      model = mquiz
      fields = ['qdesc','qop1','qop2','qop3','qop4','qop5',
                'qans','qhint','qsol','qimage','qhimg','qsimg']
      widgets = {
       'qdesc' : forms.Textarea(attrs={'class': 'form-control', 'rows':'5'} ),
       'qop1'  : forms.Textarea(attrs={'class': 'form-control', 'rows':'3'} ),
       'qop2'  : forms.Textarea(attrs={'class': 'form-control', 'rows':'3'} ),
       'qop3'  : forms.Textarea(attrs={'class': 'form-control', 'rows':'3'} ),
       'qop4'  : forms.Textarea(attrs={'class': 'form-control', 'rows':'3'} ),
       'qop5'  : forms.Textarea(attrs={'class': 'form-control', 'rows':'3'} ),
       'qhint' : forms.Textarea(attrs={'class': 'form-control', 'rows':'3'} ),
       'qsol'  : forms.Textarea(attrs={'class': 'form-control', 'rows':'3'} ),
       'qimage': forms.ClearableFileInput(),
       'qhimg': forms.ClearableFileInput(),
       'qsimg': forms.ClearableFileInput(),

      }
