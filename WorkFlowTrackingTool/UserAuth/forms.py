from django import forms

class RegisterForm(forms.Form):
    
    username = forms.CharField(max_length=150,label='Username')
    e_mail = forms.CharField(max_length=150,label='e-mail')
    password = forms.CharField(max_length=30,label='Password',widget=forms.PasswordInput)
    password_match = forms.CharField(max_length=30,label='Password Again',widget=forms.PasswordInput)
    
    def clean(self):
        username = self.cleaned_data.get('username')
        e_mail = self.cleaned_data.get('e_mail')
        password = self.cleaned_data.get('password')
        password_match = self.cleaned_data.get('password_match')
        
        if password != password_match:
            raise forms.ValidationError('Passwords not match!')
        
        values = {
            "username" : username,
            "password" : password,
            "e_mail" : e_mail
        }
        return values

class LoginForm(forms.Form):

    username = forms.CharField(max_length=150,label='Username')
    password = forms.CharField(max_length=30, label='Password', widget=forms.PasswordInput)
    