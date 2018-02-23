from django import forms

from models import User

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('name', 'username', 'password')

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('password and confirm_password don\'t match.')