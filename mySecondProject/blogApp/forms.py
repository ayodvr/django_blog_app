from django import forms
from blogApp.models import Post
from blogApp.models import Comment

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['author','title','text','featured_image']
    
        widgets = {
            'author': forms.TextInput(attrs={'class':'form-control','value':'', 'id':'author','type':'hidden'}),
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}),
            'text':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Message'})
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['title','name','body']
        
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}),
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'body':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Comment'})
        }