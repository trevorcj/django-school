from django import forms
from .models import *

class CourseRegistrationForm(forms.Form):
  name = forms.CharField(required=True)
  email = forms.EmailField(required=True)
  course = forms.ModelChoiceField(queryset=None, empty_label="Select A Course", required=True)

  def __init__(self, *args, **kwargs):
    super(CourseRegistrationForm, self).__init__(*args, **kwargs)
    courses = ReleaseCoure.objects.all() 
    self.fields['course'].queryset = courses
    
    
  def clean_email(self):
    email = self.cleaned_data.get('email')
    if Participant.objects.filter(email=email).exists():
        raise forms.ValidationError("This email is already registered.")
    return email
      

class ContactForm(forms.Form):
  name = forms.CharField(max_length=200)
  email = forms.EmailField(max_length=1000)
  subject = forms.CharField(max_length=100)
  message = forms.CharField(widget=forms.Textarea)


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ['email']
