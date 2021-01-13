from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from egg_report.models import CageNum, Report


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'cage_num'

    def get_queryset(self):
        return CageNum.objects.all()


class ReportView(generic.ListView):
    template_name = 'report.html'
    context_object_name = 'report'

    def get_queryset(self):
        return Report.objects.all()


def submit_report(request):
    data = [int(i) for i in dict(request.POST).get('report')]
    cage_list = CageNum.objects.all().values_list('id',flat=True)
    bulk_report = []
    print(cage_list)
    print(data)
    for cage in cage_list:
        print(cage)
        egg = True if cage in data else False
        bulk_report.append(
            Report(
                cage_num_id=cage,
                is_lay_egg=egg
            )
        )

    Report.objects.bulk_create(bulk_report)
    return HttpResponseRedirect(reverse('polls:report'))