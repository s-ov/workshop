from django import forms

from repairs.models import Repair, PlacesToWork, RepairType, Status


class TechnicianForm(forms.ModelForm):
    """Form for work with order for technician"""
    description = forms.CharField(
        label='Опис поломки', 
        widget=forms.Textarea(attrs={'class': 'form-control','rows': 5, 'cols': 40})
    )
    time_to_work = forms.DateTimeField(
        label='Час початку ремонту', 
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'})
    )
    places_to_work = forms.ModelChoiceField(
        label='Місце роботи',
        widget=forms.Select(attrs={'class': 'form-control'}),
        queryset=PlacesToWork.objects.all(),               
    )
    repair_type = forms.ModelChoiceField(
        label='Тип ремонту',
        widget=forms.Select(attrs={'class': 'form-control'}),
        queryset=RepairType.objects.all(),
    )
    status = forms.ChoiceField(
        label='Статус',
        widget=forms.Select(attrs={'class': 'form-control',}),
        choices=[
            item for item in Status.choices if item[0] == Status.CONFIRMED
        ]
    )
    
    class Meta:
        model = Repair
        fields = (
            'description',
            'time_to_work',
            'places_to_work',
            'repair_type',
            'status',
            )
