from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'egg_report'

urlpatterns = [
	# path('', views.IndexView.as_view(), name='index'),
	path('', views.IndexView.as_view(), name='test'),
	path('report', views.ReportView.as_view(), name='report'),
	path('submit_report', views.submit_report, name='submit_report'),
	url('export', views.export_report_xls, name='export_csv'),
]