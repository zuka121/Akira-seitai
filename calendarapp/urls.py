from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),  # トップページ
    path('calendar/', views.calendar_view, name='calendar'),  
    path('<int:year>/<int:month>/', views.calendar_view, name='calendar'),
    path('week/<int:year>/<int:month>/<int:day>/', views.week_view, name='week_view'),
]
