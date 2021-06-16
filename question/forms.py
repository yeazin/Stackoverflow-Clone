from django import forms
from django.db.models import fields
from django.forms import ModelChoiceField, ModelForm,fields,widgets
from .models import Question, Tags, Answer, Comment

class QuestionForms(ModelForm):
    
    class Meta:
        model  = Question
        fields =['title','tags','detail']
    
    widgets ={
        'title':forms.TextInput(attrs={'class':'js-post-title-field','id':'title','placeholder':'e.g. Is there an R function for finding the index of an element in a vector?'}),
        'tags':forms.MultipleChoiceField(choices=Tags)
        
    }