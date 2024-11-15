from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),  # トップページ
    path('calendar/', views.schedule_grid, name='calendar'),  
    path('detail/', views.detail_view, name='detail'),
    path('treatment/', views.treatment_view, name='treatment'),
    path('<int:year>/<int:month>/', views.calendar_view, name='calendar'),
    path('week/<int:year>/<int:month>/<int:day>/', views.week_view, name='week_view'),
    path('request/new/', views.request_create_view, name='request_create'),
    path('request/success/', views.request_success_view, name='request_success'),
    path('profile/', views.profile_view, name='profile'),
    path('notice-all/', views.notice_all, name='notice_all'),
    path('notices/<int:pk>/', views.notice_detail, name='notice_detail'),
    path('faq/', views.faq_view, name='faq'),
    path('contact/', views.contact, name='contact'),
    path('moca/', views.moca, name='moca'),    
]
