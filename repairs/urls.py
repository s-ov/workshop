from django.urls import path

from repairs.views import CreateRepair, RepairList, DetailRepair


app_name = 'repairs'

urlpatterns = [
    path('', RepairList.as_view(), name='list'),
    path('create/', CreateRepair.as_view(), name='create'),
    path('detail/<int:repair_id>', DetailRepair.as_view(), name='detail'),
]
