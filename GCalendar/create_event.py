from datetime import datetime
from GCalendar import calendar_setup
import time
from GCalendar import asistent

months = {
    "enero": "01",
    "febrero": "02",
    "marzo": "03",
    "abril": "04",
    "mayo": "05",
    "junio": "06",
    "julio": "07",
    "agosto": "08",
    "septiembre": "09",
    "octubre": "10",
    "noviembre": "11",
    "diciembre": "12"
}

def take_event_title():
    asistent.talk("Nombre del evento", "title.mp3")
    title = asistent.listen()
    return title

def take_event_description():
    asistent.talk("Descripción", "desc.mp3")
    description = asistent.listen()
    if "nada" in description:
        description = ""
    return description

def take_start_date():
    asistent.talk("Fecha y hora de inicio", "start.mp3")
    start_date = asistent.listen()
    start_date = start_date.replace(' a las ', ' de ')
    start_date = start_date.replace(' del ', ' de ')
    start_date = start_date.split(' de ')
    hour = start_date[2].strip()
    day = start_date[0].strip()
    if hour[0]!='0' and len(hour) <5:
        hour= '0'+hour
    if day[0]!='0' and len(day)<2:
        day='0'+day
    for month in months:
        if start_date[1] in months:
            month = months[start_date[1]]
    new_date = f'2024-{month}-{start_date[0]} {start_date[2]}'
    date_isoformat = datetime.fromisoformat(new_date).isoformat()
    return date_isoformat
  
def take_end_date():
    asistent.talk("Fecha y hora de fin", "end.mp3")
    end_date = asistent.listen()
    end_date = end_date.replace(' a las ', ' de ')
    end_date = end_date.replace(' del ', ' de ')
    end_date = end_date.split(' de ')
    hour = end_date[2].strip()
    day = end_date[0].strip()
    if hour[0]!='0' and len(hour) <5:
        hour= '0'+hour
    if day[0]!='0' and len(day)<2:
        day='0'+day
    for month in months:
        if end_date[1] in months:
            month = months[end_date[1]]
    new_date = f'2024-{month}-{end_date[0]} {end_date[0]}'
    date_isoformat = datetime.fromisoformat(new_date).isoformat()
    return date_isoformat

def create_event():
    event_title = take_event_title()
    time.sleep(0.5)
    event_desc = take_event_description()
    time.sleep(0.5)
    start_date = take_start_date()
    end_date = take_end_date()
    service = calendar_setup.get_calendar_services()
    service.events().insert(calendarId='primary',
        body={
            "summary": event_title,
            "description": event_desc,
            "start": {"dateTime": start_date, "timeZone": 'America/Monterrey'},
            "end": {"dateTime": end_date, "timeZone": 'America/Monterrey'},
        }
    ).execute()
