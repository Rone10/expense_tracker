from django import forms
from .models import Expense


input_class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-green-600 sm:text-sm sm:leading-6"
class ExpenseForm(forms.ModelForm):
    
    class Meta:
        model = Expense
        fields = ['name', 'amount', 'category', ]
        widgets = {
            # 'date': forms.DateInput(attrs={'type': 'date'})
            'name': forms.TextInput(attrs={'class': input_class, 'placeholder': 'Name of Expense'}),
            'amount': forms.NumberInput(attrs={'class': input_class, 'placeholder': 'Enter Amount'}),
            # 'category': forms.TextInput(attrs={'class': input_class, 'placeholder': 'e.g. Food, Rent, etc.'}),
            'category': forms.Select(attrs={'class': input_class, 'placeholder': 'e.g. Food, Rent, etc.'}),
        }
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = False
        self.fields['amount'].label = False
        self.fields['category'].label = False


   