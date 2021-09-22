from django import forms

from .models import Photo


class PhotoModelForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = [
            "title",
            "description",
            "isPremium"
        ]

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title.lower() == "error":
            raise forms.ValidationError("This is not a valid title")
        return title
