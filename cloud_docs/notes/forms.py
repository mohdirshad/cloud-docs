from django import forms
from  notes.models import Note

class Noteform(forms.ModelForm):
    class Meta: 
	model = Note
	exclude = ('user',)


