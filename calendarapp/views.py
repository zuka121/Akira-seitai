from django.shortcuts import render
from .models import Event, Notice
import calendar
from datetime import datetime, timedelta
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RequestForm


import matplotlib.pyplot as plt
import numpy as np
import japanize_matplotlib
import io
import urllib, base64

import matplotlib
matplotlib.use('Agg')

def home_view(request):
    notices = Notice.objects.all().order_by('-date')
    return render(request, 'calendarapp/home.html', {'notices': notices})



def detail_view(request):
    return render(request, 'calendarapp/detail.html')



def treatment_view(request):
    return render(request, 'calendarapp/treatment.html')



def calendar_view(request, year=None, month=None):
    if year is None or month is None:
        today = datetime.today()
        year = today.year
        month = today.month
    else:
        year = int(year)
        month = int(month)

    cal = calendar.Calendar()
    month_days = cal.monthdayscalendar(year, month)

    cal_html = '<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
    cal_html +='<caption>{}年{}月</caption>\n'.format(year, month)
    cal_html += '<tr>' + ''.join('<th width="100px">{}</th>'.format(day) for day in calendar.day_name[:7]) + '</tr>\n'

    for week in month_days:
        cal_html += '<tr>'
        for day in week:
            if day != 0:
                cal_html += '<td><a href="/week/{}/{}/{}/">{}</a></td>'.format(year, month, day, day)
            else:
                cal_html += '<td></td>'
        cal_html += '</tr>\n'
    cal_html += '</table>\n'

    events = Event.objects.filter(
        start_time__year=year,
        start_time__month=month
    )

    prev_month = month - 1 if month > 1 else 12
    prev_year = year if month > 1 else year - 1
    next_month = month + 1 if month < 12 else 1
    next_year = year if month < 12 else year + 1

    context = {
        'calendar': cal_html,
        'events': events,
        'prev_year': prev_year,
        'prev_month': prev_month,
        'next_year': next_year,
        'next_month': next_month,
    }
    return render(request, 'calendarapp/calendar.html', context)

def week_view(request, year, month, day):
    selected_date = datetime(year, month, day)
    selected_date = timezone.make_aware(selected_date)

    start_of_week = selected_date - timedelta(days=selected_date.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    events = Event.objects.filter(
        start_time__gte=start_of_week,
        start_time__lte=end_of_week
    )

    # イベント情報を一つのリストにまとめる
    event_data = []
    

    for event in events:
        day_number = 6 - event.start_time.weekday()  # 月曜を6、日曜を0に変換
        event_info = {
            'title': event.title,
            'start_time': event.start_time.hour + event.start_time.minute / 60,
            'weekday': day_number,
            'time':event.end_time.hour + event.end_time.minute / 60 - event.start_time.hour + event.start_time.minute / 60,
            
        }
        event_data.append(event_info)


    def draw_grid(data):
       fig, ax = plt.subplots(figsize=(10, 5))
    
       # 方眼を描画
       ax.set_xticks([0,1,2,3,4,5,6,7,8,9,10,11])
       ax.set_xticklabels(["9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"])

       ax.set_yticks(np.arange(0, 7, 1))
    
       ax.grid(True)


       # 一週間の月と日付情報を格納する配列
       week_dates = []
 
       # start_of_weekからend_of_weekまでの日付をループ
       current_date = start_of_week
       while current_date <= end_of_week:
          # 月と日付を配列に追加
          month_day = current_date.strftime("%m/%d")
          week_dates.insert(0, month_day)
          # 次の日に進む
          current_date += timedelta(days=1)
              
        

       # y軸ラベルに日付を追加
       positions = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
       labels = ["(日)", "(土)", "(金)", "(木)", "(水)", "(火)", "(月)"]

       for pos, label in zip(positions, labels):
          ax.text(-0.1, pos, label, ha='right', va='center', fontsize=12)

       for pos, label in zip(positions, week_dates):
          ax.text(-0.5, pos, label, ha='right', va='center', fontsize=12)




       # 各イベントの四角形を描画
       for event in data:
            rect = plt.Rectangle((event['start_time']+0.02, event['weekday'] + 0.2), event['time']-0.04, 0.6, edgecolor='black', facecolor='skyblue', linewidth=1)
            ax.add_patch(rect)
            ax.text(event['start_time'] + 0.2, event['weekday'] + 0.5, event['title'], ha='left', va='center', fontsize=10)

       # グラフの表示範囲を設定
       ax.set_xlim(0,11) 
       ax.set_ylim(0, 7)
    
       plt.tick_params(labelleft=False, left=False, bottom=False)
       
    #グラフを作成
    draw_grid(event_data)


    # 画像をバッファに保存
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    image_png = buf.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buf.close()

    context = {
        'events': event_data,
        'start_of_week': start_of_week,
        'end_of_week': end_of_week,
        'table_image': graph,  # 画像データをコンテキストに追加
    }

    return render(request, 'calendarapp/week.html', context)



def request_create_view(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('request_success')  # 保存後のリダイレクト先を設定
    else:
        form = RequestForm()

    return render(request, 'calendarapp/request_form.html', {'form': form})



def request_success_view(request):
    return render(request, 'calendarapp/request_success.html')



def profile_view(request):
    return render(request, 'calendarapp/profile.html')


def faq_view(request):
    return render(request, 'calendarapp/faq.html')

def contact(request):
    return render(request, 'calendarapp/contact.html')

def moca(request):
    return render(request, 'calendarapp/moca.html')



def notice_detail(request, pk):
    notice = get_object_or_404(Notice, pk=pk)  # 特定のお知らせを取得
    return render(request, 'calendarapp/notice_detail.html', {'notice': notice})


