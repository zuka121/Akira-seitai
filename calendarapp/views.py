from django.shortcuts import render
from .models import Event
import calendar
from datetime import datetime

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

    # HTMLカレンダーをカスタマイズ
    cal_html = '<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'

    cal_html += '<caption>{}年{}月</caption>'.format(year, month)
     
    cal_html += '<tr>' + ''.join('<th>{}</th>'.format(day) for day in calendar.day_name[:7]) + '</tr>\n'

    for week in month_days:
        cal_html += '<tr>'
        for day in week:
            if day != 0:
                cal_html += '<td><a href="/{}/{}/{}/">{}</a></td>'.format(year, month, day, day)
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

def day_view(request, year, month, day):
    events = Event.objects.filter(
        start_time__year=year,
        start_time__month=month,
        start_time__day=day
    )
    
    context = {
        'events': events,
        'date': datetime(year, month, day),
    }
    return render(request, 'calendarapp/day.html', context)
