from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('report', views.ReportView.as_view(), name='report'),
	path('submit_report', views.submit_report, name='submit_report'),
]