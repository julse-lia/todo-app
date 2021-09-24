from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('text',)
    
    text = forms.CharField(max_length=200, label= '',
                        widget= forms.TextInput
                        (attrs={'class': 'form-control',
                        'placeholder':'Enter some text here . . .'}))
