from django import forms

from .models import Application, Comment


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('name', 'email', 'subject', 'message')

        widgets = {
            'name': forms.TextInput(attrs={
                "class": "form-control",
                "id": "name",
                "placeholder": "Your Name",
                "required": "required",
                "data-validation-required-message": "Please enter your name"
            }),
            'email': forms.EmailInput(attrs={
                "class": "form-control",
                "id": "email",
                "placeholder": "Your Email",
                "required": "required",
                "data-validation-required-message": "Please enter your email"
            }),
            'subject': forms.TextInput(attrs={
                "class": "form-control",
                "id": "subject",
                "placeholder": "Subject",
                "required": "required",
                "data-validation-required-message": "Please enter a subject"
            }),
            'message': forms.Textarea(attrs={
                "class": "form-control",
                "id": "message",
                "placeholder": "Message",
                "required": "required",
                "data-validation-required-message": "Please enter your message"
            })

        }

    def save(self):
        application = Application.objects.create(
            name=self.cleaned_data['name'],
            email=self.cleaned_data['email'],
            subject=self.cleaned_data['subject'],
            message=self.cleaned_data['message']
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['create_at', 'post']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email'}),
            'website': forms.TextInput(attrs={'placeholder': 'website'}),
            'message': forms.Textarea(attrs={'placeholder': 'message'})
        }