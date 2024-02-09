from django import forms

class PostcreateForm(forms.Form):
    title = forms.CharField(
        label="Post Title",
        max_length=100,
        min_length=5,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    content = forms.CharField(
        label="Post Content",
        widget=forms.Textarea(
            attrs={
                "class": "form-control"
            }
        ),
        required=True,
    )

from post.models import Post
class PostModelForm(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'

