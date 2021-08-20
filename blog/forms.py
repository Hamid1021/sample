from django import forms

class CommentForm(forms.Form):
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

    message = forms.CharField(
        required=True,
        label="",
        widget=forms.Textarea(
            attrs=
            {"type": "text",
             "placeholder": 'نظر شما',
             }
        ))