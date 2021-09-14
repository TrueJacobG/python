from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label="Type your title here", widget=forms.TextInput(
        attrs={'placeholder': 'Type your title here'}))

    class Meta:
        model = Product
        fields = ["title", "description", "price"]

    # def clean_<name_of_form_field>
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not "CFE" in title:
            raise forms.ValidationError("THIS IS NOT VALID TITLE")

        return title


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
