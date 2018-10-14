from django.forms import ModelForm
from django.core.validators import RegexValidator

from .models import (
    User,
    Speaker
)


class UserForm(ModelForm):

    class Meta:
        model = User
        fields = [
            'username',
            'FirstName',
            'LastName',
            'email',
            'mobile'
        ]

    # username = forms.CharField(label='Username', max_length=32)
    # first_name = forms.CharField(label='First Name', max_length=50)
    # last_name = forms.CharField(label='Last Name', max_length=50)
    # email = forms.EmailField(label='Email', max_length=100)
    # mobile_no_validator = RegexValidator(regex=r'\d{10}', message="Phone number must be 10 digits only!!")
    # mobile = forms.CharField(label='Mobile Number', validators=[mobile_no_validator], max_length=10)


class SpeakerForm(ModelForm):

    class Meta:
        model = Speaker
        fields = [
            'username',
            'FirstName',
            'LastName',
            'email',
            'mobile',
            'EmergencyContactName',
            'EmergencyContactNumber',
            'GitHub',
            'Twitter',
            'LinkedIn'
        ]

    # EmergencyContactName = forms.CharField(max_length=100, label='Emergency Contact')
    # EmergencyContactNumber = forms.CharField(validators=[UserForm.mobile_no_validator], max_length=10, label='Emergency Contact Number')
    # GitHub = forms.CharField(max_length=200)
    # Twitter = forms.CharField(max_length=200, required=False)
    # LinkedIn = forms.CharField(max_length=200, required=False)
