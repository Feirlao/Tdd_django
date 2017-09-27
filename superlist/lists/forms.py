from django import forms
from lists.models import Item
<<<<<<< HEAD
#class ItemForm(forms.Form):
      #item_text=forms.CharField(



class ItemForm(forms.models.ModelForm):
    class Meta:
        model = Item
        fields = ('text',)
        widgets = {
            'text': forms.fields.TextInput(attrs={
                  'placeholder': 'Enter a to-do item',
                  'class': 'form-control input-lg',
                }),
        }
=======
EMPTY_LIST_ERROR = "you can not have an empty list item"
class ItemForm(forms.models.ModelForm):
    class Meta:
         model = Item

         fields = ('text',)
         widgets = {
             'text': forms.fields.TextInput(attrs={
                 'placeholder': 'Enter a to-do item',
                 'class': 'form-control input-lg',
             }),
         }
         error_messages = {'text': {'required':EMPTY_LIST_ERROR}}
>>>>>>> 48d9e8a2392dbc0e1260850d78108dfbebbfb2dc
