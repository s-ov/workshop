from django import forms
from django.contrib.auth import get_user_model

from repairs.models import Repair, Parts, Status
from users.models import Role

User = get_user_model()


class MasterForm(forms.ModelForm):
    """Form for work with order for master"""
    parts = forms.ModelMultipleChoiceField(
        label='Деталі',
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        queryset=Parts.objects.all(),
    )

    users = forms.ModelMultipleChoiceField(
        label='Workers',
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        queryset=User.objects.filter(role=Role.WORKER),
    )
    status = forms.ChoiceField(
        label='Статус',
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=[
            item for item in Status.choices if item[0] in ('READY_TO_WORK', 'RE_REPAIR', 'VERIFICATION')
        ]
    )

    class Meta:
        model = Repair
        fields = ('parts', 'users', 'status')
