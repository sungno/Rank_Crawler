from django.conf.urls import url, include
from django.urls import path

from . import views

urlpatterns = [

    path('chart_bar', views.chart_bar, name="chart_bar"),
    path('chart_line', views.chart_line, name="chart_line"),
    path('chart', views.chart, name="chart"),
]
