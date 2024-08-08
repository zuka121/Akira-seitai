from django.shortcuts import render
from .models import Event
import calendar
from datetime import datetime, timedelta

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
    cal_html += '<tr>' + ''.join('<th>{}</th>'.format(day) for day in calendar.day_name[:7]) + '</tr>\n'

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
    start_of_week = selected_date - timedelta(days=selected_date.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    events = Event.objects.filter(
        start_time__gte=start_of_week,
        start_time__lte=end_of_week
    )

    context = {
        'events': events,
        'start_of_week': start_of_week,
        'end_of_week': end_of_week,
    }
    return render(request, 'calendarapp/week.html', context)
