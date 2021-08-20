from django import forms

class CantactForm(forms.Form):
    full_name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs=
            {"type": "text",
             "placeholder": 'نام شما',
             }
        ))

    email = forms.CharField(
        max_length=300,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs=
            {"type": "email",
             "placeholder": 'آدرس ایمیل شما',
             }
        ))

    subject = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs=
            {"type": "text",
             "placeholder": 'موضوع پیام',
             }
        ))

    message = forms.CharField(
        required=True,
        label="",
        widget=forms.Textarea(
            attrs=
            {"type": "text",
             "placeholder": 'متن پیام',
             }
        ))