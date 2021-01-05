from django.urls import path
from . import views
from .serm import *


urlpatterns = [
    path('report/<int:person_id>/', save_data_for_report),
    path('report/<int:person_id>/second_faza/', create_report_table),
    path('report/<int:person_id>/distribute/', views.url_list, name='url_list.html'),
    path('', views.person_list, name='person_list'),
    path('report/<int:person_id>/drop_status', drop_status)
]
