from django import forms
from .models import Medicine, MedicineCategory, Dispensing, StockMovement

class MedicineCategoryForm(forms.ModelForm):
    class Meta:
        model = MedicineCategory
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        exclude = ['created_at', 'updated_at']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
        }

class DispensingForm(forms.ModelForm):
    class Meta:
        model = Dispensing
        exclude = ['total_price', 'dispensed_at', 'unit_price']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 2}),
        }

class StockMovementForm(forms.ModelForm):
    class Meta:
        model = StockMovement
        exclude = ['medicine', 'created_at']
        widgets = {
            'reason': forms.Textarea(attrs={'rows': 2}),
        }
