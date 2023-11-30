from django.forms import ModelForm
from django import forms
from .models import NewsPost

class NewsPostForm(ModelForm):

    class Meta:
        model = NewsPost
        fields = ['category', 'title', 'comment', 'image1','image2']

class NewContactForm(forms.Form):
    name = forms.CharField(label='お名前')
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='件名')
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = \
        'お名前を入力してね'
        self.fields['name'].widget.attrs['class'] = 'form-control'

        self.fields['email'].widget.attrs['placeholder'] = \
        'メールアドレスを入力してね'
        self.fields['email'].widget.attrs['class'] = 'form-control'

        self.fields['title'].widget.attrs['placeholder'] = \
        'タイトルを入力してね'
        self.fields['title'].widget.attrs['class'] = 'form-control'

        self.fields['message'].widget.attrs['placeholder'] = \
        'メッセージを入力してね'
        self.fields['message'].widget.attrs['class'] = 'form-control'