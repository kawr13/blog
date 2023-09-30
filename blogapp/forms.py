from django import forms
from .models import Post, Tag, Comments


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    text = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
    }))
    presents = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
    }))
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        required=False
    )
    is_published = forms.BooleanField(required=False)

    class Meta:
        model = Post
        fields = ['title', 'text', 'tags']


class CommentsForm(forms.ModelForm):
    authors = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Name',

    }), required=False)


    comments = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Comments',
    }), required=False)

    class Meta:
        model = Comments
        fields = ['authors', 'comments']