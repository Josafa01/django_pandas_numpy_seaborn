from django import forms


class LoginForm(forms.Form):
    nome = forms.CharField(max_length=220)
    senha = forms.CharField(max_length=220, widget=forms.PasswordInput)

    def clean(self):
        data = self.cleaned_data

        nome = data.get('username')
        senha = data.get('password')

        return data
