from .models import PrinterFile, Colors
from django import forms
from phone_field import PhoneField


class EmailForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    phone_number = PhoneField()
    email = forms.EmailField(max_length=200,
                             widget=forms.TextInput(attrs={'class': "form-control", 'id': "clientemail"}))
    #member = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control", 'placeholder': "Yes or No"}))
    creator = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control"}))
    dimensions = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control", 'placeholder': "MAX: X:7 Y:7 Z:7"}))
    # color = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    special_requests = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    message = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))

    COLOR_CHOICES = []
    for items in Colors.objects.all():
        COLOR_CHOICES.append((items.name, (items.name + items.price)))

    color = forms.MultipleChoiceField(
        required=False,
        widget=forms.Select(attrs={'class': "form-control"}),
        choices=COLOR_CHOICES,
    )

    MEMBER_CHOICES = [('NO', 'NO (Members get a discount)')]
    MEMBER_CHOICES.append(('YES','YES (Eligible for discount)'))
    member = forms.MultipleChoiceField(
        required=True,
        widget=forms.Select(attrs={'class': "form-control"}),
        choices=MEMBER_CHOICES,
    )

    class Meta:
        model = PrinterFile
        fields = ('first_name', 'last_name', 'phone_number', 'email', 'member', 'creator', 'dimensions', 'color', 'special_requests', 'message', 'document')

