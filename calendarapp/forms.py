from django import forms
from .models import Request, Contact



class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['name', 'start_time', 'end_time', 'treatment_location', 'phone_number', 'email', 'email_confirm', 'comment']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'お名前を入力してください'}),
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-input'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-input'}),
            'treatment_location': forms.Select(attrs={'class': 'form-input'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-input', 'placeholder': '電話番号を入力してください'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'メールアドレスを入力してください'}),
            'email_confirm': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'メールアドレスを再度入力してください'}),
            'comment': forms.Textarea(attrs={'class': 'form-input', 'placeholder': '症状について、できるだけ詳細にお書きください'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['gender', 'age', 'message']
        widgets = {
            'gender': forms.Select(attrs={'class': 'form-select'}),  # 性別選択
            'age': forms.Select(attrs={'class': 'form-select'}),     # 年齢選択
            'message': forms.Textarea(attrs={'placeholder': 'お気軽に入力してください'}),
        }

