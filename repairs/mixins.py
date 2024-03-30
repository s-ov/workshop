from users.models import Role
from repairs.models import Status



class RepairMixin:

    @staticmethod
    def _get_repair_filter(user) -> dict:
        """Return repair order list corresponding to user status"""
        repair_filters = {
            Role.CUSTOMER: {
                'users': user,
            },
            Role.TECHNICIAN: {
                'status__in': [Status.CREATED, Status.VERIFICATION],
            },
            Role.MASTER: {
                'status__in': [Status.CONFIRMED, Status.TEST],
            },
            Role.WORKER: {
                'status__in': [Status.RE_REPAIR, Status.READY_TO_WORK, Status.PROGRESS], 
            },
            
        }
        return repair_filters.get(user.role)
