from datetime import datetime

from django.db.models import Count
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from egg_report.models import Cage, Report


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'cage_num'

    def get_queryset(self):
        return Cage.objects.all()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['left'] = [i for i in ctx['object_list'] if i.position == 'L']
        ctx['right'] = [i for i in ctx['object_list'] if i.position == 'R']
        return ctx


class ReportView(generic.ListView):
    template_name = 'report.html'
    context_object_name = 'report'

    def get_queryset(self):
        return Report.objects.all()

    def get_today_report(self):
        today = self.get_queryset().filter(
            date=datetime.now().date(),
            is_lay_egg=True).count()
        return today

    def get_report_by_date(self):
        q = self.get_queryset().filter(is_lay_egg=True)\
            .values('date').annotate(c=Count('id')).order_by('-date')[:7]
        return q

    def get_report_by_cage(self):
        q = self.get_queryset() \
            .filter(is_lay_egg=True) \
            .values('cage_num_id', 'cage_num__number', 'cage_num__position') \
            .annotate(c=Count('id')) \
            .order_by('cage_num__position', '-c')

        return q

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(ReportView, self).get_context_data()
        ctx['today'] = self.get_today_report()
        ctx['by_date'] = self.get_report_by_date()
        ctx['by_cage'] = self.get_report_by_cage()
        return ctx


def submit_report(request):
    data = [int(i) for i in dict(request.POST).get('report')]
    date = request.POST.get('input_date', datetime.now().date())
    cage_list = Cage.objects.all().values_list('id', flat=True)
    bulk_report = []

    # import pdb;pdb.set_trace()
    for cage in cage_list:
        egg = True if cage in data else False
        bulk_report.append(
            Report(
                cage_num_id=cage,
                is_lay_egg=egg,
                date=datetime.strptime(date, '%Y-%M-%d')
            )
        )

    Report.objects.bulk_create(bulk_report)
    return HttpResponseRedirect(reverse('polls:report'))
