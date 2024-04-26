from django import forms
from .models import Post, CustomUser
from django_ckeditor_5.widgets import CKEditor5Widget
# For reg user
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

from .apps import user_registered


class RegUserForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Email')
    password1 = forms.CharField(
            label='Pass',
            widget=forms.PasswordInput,
            help_text=password_validation.password_validators_help_text_html()
        )
    password2 = forms.CharField(
            label = 'Pass again',
            widget = forms.PasswordInput,
            help_text = 'Please, enter your password again.'
        )

    def clean_password1(self):
        password1 = self.cleaned_data['password']
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError(
                    "Password mismatch",
                    code='password_mismatch'
                )
            }
            raise ValidationError(errors)

    def seve(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = False
        user.is_activated = False
        if commit:
            user.save()
        user_registered.send(RegUserForm, instance=user)
        return user

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            # 'first_name',
            # 'last_name',
            # 'send_messages'
            )


class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["text"].required = False

    class Meta:
        model = Post
        # fields = ['title', 'text']
        fields = '__all__'
        #options
        widgets = {
            "text": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends"
            )
        }
