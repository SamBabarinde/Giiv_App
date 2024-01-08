from django import forms
from core.models import Item


INPUT_CLASS = "w-full flex-1 appearance-none border-blue-300 bg-white px-4 py-2 text-base text-gray-700 placeholder-gray-400 focus:outline-none"

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("category", "title", 'details', 'location')
       
        widgets = {
            "category": forms.Select(attrs={
                'class': INPUT_CLASS
            }), 
            
            "title": forms.TextInput(attrs={
                'class': INPUT_CLASS
            }),
            
            "details": forms.Textarea(attrs={
                'class': INPUT_CLASS
            }), 
            
            "location": forms.TextInput(attrs={
                'class': INPUT_CLASS
            }), 
            
        }
        