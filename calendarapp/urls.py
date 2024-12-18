from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('calendar/', views.create_view, name='calendar'),  
    path('detail/', views.detail_view, name='detail'),
    path('treatment/', views.treatment_view, name='treatment'),
    path('week/<int:year>/<int:month>/<int:day>/', views.week_view, name='week_view'),
    path('profile/', views.profile_view, name='profile'),
    path('notice-all/', views.notice_all, name='notice_all'),
    path('notices/<int:pk>/', views.notice_detail, name='notice_detail'),
    path('faq/', views.faq_view, name='faq'),
    path('contact/', views.contact, name='contact'),
    path('contact/form/', views.contact_form, name='contact_form'),
    path('contact/form/success/', views.contact_success, name='contact_success'),
    path('moca/', views.moca, name='moca'),  
    path('syuttyou/', views.syuttyou_view, name='syuttyou'), 
    path('confirm/', views.confirm_view, name='confirm_view'),  # 確認画面
    path('request_success/', views.request_success, name='request_success'),  
]
