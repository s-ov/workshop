from django import forms

from repairs.models import Repair, Locomotive


class CustomerForm(forms.ModelForm):
    description = forms.CharField(label='Опис поломки', widget=forms.Textarea(attrs={'class': 'form-control','rows': 5, 'cols': 40}))
    locomotive = forms.ModelChoiceField(label='Виберіть локомотив', 
                                        queryset=Locomotive.objects.all(), 
                                        widget=forms.Select())
    
    class Meta:
        model = Repair
        fields = ('description', 'locomotive')
