from django import forms
from django.db.models import fields
from django.forms import ModelChoiceField, ModelForm,fields,widgets
from .models import Question, Tags, Answer, Comment

class QuestionForms(ModelForm):
    
    class Meta:
        model  = Question
        fields =['title','tags','detail']
    
    widgets ={
        'title':forms.TextInput(attrs={'class':'form-control','id':'title','placeholder':'Question Title here'}),
        'tags':forms.MultipleChoiceField(choices=Tags)
        
    }