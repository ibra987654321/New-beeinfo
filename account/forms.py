from django import forms
from .ldap import LoginAD


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Пользователь'}))
    password = forms.CharField(widget=forms.PasswordInput(render_value=True, attrs={'placeholder': 'Пароль'}))

    def clean(self):
        data = super().clean()
        try:
            username = data.get("username")
            password = data.get("password")

            if username.endswith("@beeline.kg"):
                username = username.replace("@beeline.kg", "")
                data['username'] = username

            ad = LoginAD(username, password)

            if ad.get('displayName'):
                data['first_name'], data['last_name'] = ad.get_full_name()
                data['mail'] = ad.get('mail')
                return data
            raise forms.ValidationError('Неправильное имя пользователя или пароль')
            
        except AttributeError: # if data is None
            raise forms.ValidationError('Заполните поля')
        except BaseException as e:
            raise e
