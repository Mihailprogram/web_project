from django.forms import ModelForm

from .models import Comment, Post, Group


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['title', 'slug', 'description']


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["text", "group", 'image']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
