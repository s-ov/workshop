from django import forms

from repairs.models import Repair, Status


class WorkerForm(forms.ModelForm):
    """Form for work with order for worker"""
    status = forms.ChoiceField(
        label='Статус',
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=[
            item for item in Status.choices if item[0] in ('PROGRESS', 'TEST')
        ]
    )

    class Meta:
        model = Repair
        fields = ('status',)
