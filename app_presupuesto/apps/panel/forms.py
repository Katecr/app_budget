from django import forms

from .models import *

class BudgetForm(forms.ModelForm):


    class Meta:
        model = FormBudget
        fields = '__all__'
        widgets = {
            'salary_year': forms.NumberInput(
                attrs={
                'class':'form-control',
                'required': True,
                }
            ),
            'cesantias': forms.NumberInput(
                attrs={
                'class':'form-control',
                'required': True,
                }
            ),
            'prima': forms.NumberInput(
                attrs={
                'class':'form-control',
                'required': True,
                }
            ),
            'int_cesantias': forms.NumberInput(
                attrs={
                'class':'form-control',
                'required': True,
                }
            ),
            'vacaciones': forms.NumberInput(
                attrs={
                'class':'form-control',
                'required': True,
                }
            ),
            'total_prest': forms.NumberInput(
                attrs={
                'class':'form-control',
                'required': True,
                }
            ),
            'salud': forms.NumberInput(
                attrs={
                'class':'form-control',
                'required': True,
                }
            ),
            'pension': forms.NumberInput(
                attrs={
                'class':'form-control',
                'required': True,
                }
            ),
            'arl': forms.NumberInput(
                attrs={
                'class':'form-control',
                'required': True,
                }
            ),
            'comfama': forms.NumberInput(
                attrs={
                'class':'form-control',
                'required': True,
                }
            ),
            'sena': forms.NumberInput(
                attrs={
                'class':'form-control',
                'required': True,
                }
            ),
            'icbf': forms.NumberInput(
                attrs={
                'class':'form-control',
                'required': True,
                }
            ),
            'total_aportes': forms.NumberInput(
                attrs={
                'class':'form-control',
                'required': True,
                }
            ),
            'typebudget_id': forms.Select(
                attrs={
                'class':'form-select',
                'required': True,
                }
            ),
        }
