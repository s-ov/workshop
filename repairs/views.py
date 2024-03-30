from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.views.generic import ListView, FormView
from django.views import View
from django import forms

from repairs.mixins import RepairMixin
from repairs.forms.customer import CustomerForm
from repairs.forms.technician import TechnicianForm
from repairs.forms.master import MasterForm
from repairs.forms.worker import WorkerForm
from repairs.models import Status, Repair
from users.models import Role


class RepairList(RepairMixin, ListView):
    """"List of repairs"""
    template_name = 'repair_list.html'
    model = Repair
    paginate_by = 5


    def get_queryset(self):
        _filter = self._get_repair_filter(self.request.user)
        return Repair.objects.filter(**_filter)


class CreateRepair(FormView):
    template_name = 'create_repair.html'
    form_class = CustomerForm
    success_url = "/repairs/"

    def form_valid(self, form):
        repair = form.save()
        repair.users.add(self.request.user)
        return super().form_valid(form)
    

class DetailRepair(RepairMixin, View):
    """"Repair detail"""
    template_name = 'detail.html'

    def _get_form(self, repair, data=None) -> forms.ModelForm:
        """Return form according to user role"""
        user_form = {
            Role.CUSTOMER: None, 
            Role.TECHNICIAN: TechnicianForm(data=data, instance=repair, initial={'status': 'CONFIRMED'}),
            Role.MASTER: MasterForm(data=data, instance=repair),
            Role.WORKER: WorkerForm(data=data, instance=repair),
            }
        return user_form.get(self.request.user.role)

    def post(self, request, repair_id):
        _filter = self._get_repair_filter(self.request.user)
        repair = get_object_or_404(Repair, pk=repair_id, **_filter)
        form = self._get_form(repair, data=request.POST)
        if form.is_valid():
            # users = form.cleaned_data['users']
            users = list(repair.users.all())
            form.save()
            repair.users.add(request.user, *users)
        context = {'repair': repair, 'form': form,}
        return render(request, self.template_name, context)

    def get(self, request, repair_id):
        _filter = self._get_repair_filter(self.request.user)
        repair = get_object_or_404(Repair, pk=repair_id, **_filter)
        context = {'repair': repair, 'form': self._get_form(repair),}
        return render(request, self.template_name, context)
