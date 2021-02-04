from datetime import datetime

from django.db.models import Count, Sum, Q, Case, When
from django.db.models.functions import ExtractWeek
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
        today = self.get_queryset() \
            .filter(date=datetime.now().date(), egg__gte=1).aggregate(s=Sum('egg'))
        return today['s']

    def get_report_by_date(self):
        q = self.get_queryset().filter(egg__gte=1) \
                .values('date').annotate(c=Sum('egg')).order_by('-date')[:7]
        return q

    def get_report_by_week(self):
        q = self.get_queryset().filter(egg__gte=1) \
            .annotate(week=ExtractWeek('date')) \
            .values('week').annotate(c=Sum('egg')).order_by('-week')
        return q

    def get_report_by_cage(self):
        rpt = self.get_queryset() \
            .values('cage_num_id', 'cage_num__number', 'cage_num__position') \
            .annotate(c=Sum('egg')) \
            .order_by('cage_num__position', '-c')
        rpt = {i['cage_num_id']: i['c'] for i in rpt}

        cage = Cage.objects.all()
        for c in cage:
            setattr(c, 'c', rpt.get(c.id, 0))

        return sorted(cage, key=lambda x: (x.position, x.c), reverse=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(ReportView, self).get_context_data()
        ctx['today'] = self.get_today_report()

        by_date = self.get_report_by_date()
        ctx['by_date'] = by_date
        by_date = sorted(by_date, key=lambda x: x['date'])
        ctx['by_date_list'] = [i['date'].strftime("%d/%m/%Y") for i in by_date]
        ctx['by_date_count'] = [i['c'] for i in by_date]

        ctx['by_week'] = self.get_report_by_week()

        ctx['by_cage'] = self.get_report_by_cage()
        f = lambda x: 'Ki' if x.position is 'L' else 'Ka'
        ctx['by_cage_list'] = [f"{i.number} {f(i)}" for i in self.get_report_by_cage() if i.c != 0]
        ctx['by_cage_count'] = [i.c for i in self.get_report_by_cage() if i.c != 0]
        return ctx


def submit_report(request):
    report_left = dict(request.POST).get('reportLeft')
    report_right = dict(request.POST).get('reportRight')
    if None in [report_left, report_right]:
        return HttpResponseRedirect(reverse('egg_report:report'))

    date = request.POST.get('input_date', datetime.now().date())
    last_report = Report.objects.filter(date=datetime.strptime(date, '%Y-%m-%d'))
    if last_report.count() > 0:
        last_report.delete()

    bulk_report = []
    report_left = report_left[0].split(',')
    report_right = report_right[0].split(',')
    left_cage = Cage.objects.filter(position='L')
    right_cage = Cage.objects.filter(position='R')

    for cage_id, egg in enumerate(report_left):
        if int(egg) != 0:
            bulk_report.append(
                Report(
                    cage_num=left_cage[cage_id],
                    egg=int(egg),
                    date=datetime.strptime(date, '%Y-%m-%d')
                )
            )
    for cage_id, egg in enumerate(report_right):
        if int(egg) != 0:
            bulk_report.append(
                Report(
                    cage_num=right_cage[cage_id],
                    egg=int(egg),
                    date=datetime.strptime(date, '%Y-%m-%d')
                )
            )

    Report.objects.bulk_create(bulk_report)

    return HttpResponseRedirect(reverse('egg_report:report'))
