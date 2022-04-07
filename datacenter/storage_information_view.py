from ctypes import BigEndianStructure
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def format_duration(duration):
    return str(duration)



def storage_information_view(request):
    active_visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in active_visits:
        duration = format_duration(visit.get_duration())
        who_entered = visit.passcard.owner_name
        entered_at = visit.entered_at
        is_strange = visit.is_visit_long()
        non_closed_visits.append(
            {
                'who_entered': who_entered,
                'entered_at': entered_at,
                'duration': duration,
                'is_strange': is_strange,
            },
        )
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
