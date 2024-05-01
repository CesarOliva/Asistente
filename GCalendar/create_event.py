from datetime import datetime
from GCalendar import calendar_setup
import time

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
    title = input("Titulo del evento: ")
    return title


def take_event_description():
    description = input("Descripción del evento: ")
    return description

def take_start_date():
    start_date = input("¿En qué fecha y hora será el evento?")
    start_date = start_date.replace(' a las ', ' de ')
    start_date = start_date.replace(' del ', ' de ')
    start_date = start_date.split(' de ')
    for month in months:
        if start_date[1] in months:
            month = months[start_date[1]]
    new_date = f'{start_date[2]}-{month}-{start_date[0]} {start_date[3]}'
    date_isoformat = datetime.fromisoformat(new_date).isoformat()
    return date_isoformat
  
def take_end_date():
    end_date = input("¿En qué fecha y hora terminará el evento?")
    end_date = end_date.replace(' a las ', ' de ')
    end_date = end_date.replace(' del ', ' de ')
    end_date = end_date.split(' de ')
    for month in months:
        if end_date[1] in months:
            month = months[end_date[1]]
    new_date = f'{end_date[2]}-{month}-{end_date[0]} {end_date[3]}'
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
    event_result = service.events().insert(calendarId='primary',
        body={
            "summary": event_title,
            "description": event_desc,
            "start": {"dateTime": start_date, "timeZone": 'America/Monterrey'},
            "end": {"dateTime": end_date, "timeZone": 'America/Monterrey'},
        }
    ).execute()
