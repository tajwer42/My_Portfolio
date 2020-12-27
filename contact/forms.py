from .models import ContactFeedback
from django import forms

class ContactFeedbackForm(forms.ModelForm):
    class Meta:
        model = ContactFeedback
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        ### define custom css widget attributes ###
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control','placeholder':'Your Name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control','placeholder':'Your Email'})
        self.fields['subject'].widget.attrs.update({'class': 'form-control','placeholder':'Subject'})
        self.fields['message'].widget.attrs.update({'class': 'form-control','placeholder':'Message','cols':'30','rows':'7'})
