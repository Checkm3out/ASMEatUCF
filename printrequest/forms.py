from .models import PrinterFile
from django import forms


class EmailForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control"}))
    last_name = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control"}))
    phone_number = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control"}))
    email = forms.EmailField(max_length=200,
                             widget=forms.TextInput(attrs={'class': "form-control", 'id': "clientemail"}))
    member = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control"}))
    creator = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control"}))
    dimensions = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control"}))
    color = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control"}))
    special_requests = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    message = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))


    class Meta:
        model = PrinterFile
        fields = ('first_name', 'last_name', 'phone_number', 'email', 'member', 'creator', 'dimensions', 'color', 'special_requests', 'message', 'document')

