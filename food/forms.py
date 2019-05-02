from django import forms
from .models import Post, Post1, Post2, Post3, Post4, Post5, Post6, Post7, Post8, Post9, Post10, Post11, Post12, Post13, Post14, Post15, Post16, Post17, Post18, Post19
from django.contrib.auth.models import User


class Postform(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Post
        fields = ['content']


class Post1form(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Post1
        fields = ['content']


class Post2form(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Post2
        fields = ['content']


class Post3form(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Post3
        fields = ['content']


class Post4form(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Post4
        fields = ['content']


class Post5form(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Post5
        fields = ['content']


class Post6form(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Post6
        fields = ['content']


class Post7form(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Post7
        fields = ['content']


class Post8form(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Post8
        fields = ['content']


class Post9form(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Post9
        fields = ['content']


class Post10form(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Post10
        fields = ['content']


class Post11form(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Post11
        fields = ['content']


class Post12form(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Post12
        fields = ['content']


class Post13form(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Post13
        fields = ['content']


class Post14form(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Post14
        fields = ['content']


class Post15form(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Post15
        fields = ['content']


class Post16form(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Post16
        fields = ['content']


class Post17form(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Post17
        fields = ['content']


class Post18form(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Post18
        fields = ['content']


class Post19form(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Post19
        fields = ['content']














