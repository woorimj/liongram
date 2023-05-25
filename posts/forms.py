from random import choices
from sre_constants import CATEGORY
from django import forms
from django.core.exceptions import ValidationError
from .models import Post

#class PostBaseForm(forms.Form):
#     CATEGORY_CHOICES = [
#          (1, '일반'),
#          (2, '계정'),
#     ]
#     image = forms.ImageField(label='이미지')
#     content = forms.CharField(label='내용', widget=forms.Textarea, required=True)
#     category = forms.ChoiceField(label='카테고리', choices=CATEGORY_CHOICES)

class PostBaseForm(forms.ModelForm):
      class Meta:
          model = Post
          fields = '__all__'

class PostCreateForm(PostBaseForm):
     class Meta(PostBaseForm.Meta):
          fields = ['image', 'content']
     
     # 유효성검사
     def clean_content(self):
          data = self.cleaned_data['content']
          if "비속어" == data:
               raise ValidationError("비속어는 사용하실 수 없습니다.")
          return data
    

class PostUpdateForm(PostBaseForm):
     class Meta(PostBaseForm.Meta):
          fields = ['image', 'content']


class PostDetailForm(PostBaseForm):
     def __init__(self, *args, **kwargs):
          super().__init__(self, *args, **kwargs)
          for key in self.fields:
               self.fields[key].widget.attrs['disabled'] = True 