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
