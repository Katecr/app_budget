from django.urls import path

from .views import *


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('list/', list, name='list'),
    path('report_excel/', ReporteExcelView.as_view(), name='report_excel'),
]