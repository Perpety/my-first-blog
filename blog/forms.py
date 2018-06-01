<<<<<<< HEAD
from django import forms

from .models import Post

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'text',)
=======
from django import forms

from .models import Post

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'text',)
		
>>>>>>> a956e3f5d8707afb2fb7939aa59f402ad8377fcd
