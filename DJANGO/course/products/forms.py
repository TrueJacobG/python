from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title", "description", "price"]


class RawProductForm(forms.Form):
    title = forms.CharField(label="Type your title here", widget=forms.TextInput(
        attrs={'placeholder': 'Type your title here'}))
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(attrs={
                                      "class": "new-class",
                                      "placeholder": "Type your description here",
                                      "rows": "20",
                                      "cols": "20",
                                  }),
                                  )
    price = forms.DecimalField(initial=100)
