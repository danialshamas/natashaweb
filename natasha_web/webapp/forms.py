from django import forms

class ContactForm(forms.Form):
    your_name = forms.CharField(max_length=100,label='Your Name')
    your_email = forms.EmailField(label='Your Email')
    message = forms.CharField(label='Your Message',widget = forms.Textarea)
