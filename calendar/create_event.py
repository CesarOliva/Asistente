from datetime import datetime, timedelta
from calendar import get_calendar_service
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
    description=input("Descripcion del evento: ")
    return description

def take_start_date():
    global start_date, month
    start_date = input("Fecha de inicio")
    start_date = start_date.replace(' de ', ' ')
    start_date = start_date.replace(' a las ', ' ')
    start_date = start_date.split(' ')
    for month in months:
        if start_date[1] in months:
            month = months[start_date[1]]
    new_date = f"2024-{month}-{start_date[0]} {start_date[2]}"
    date_iso_format = datetime.fromisoformat(new_date).isoformat()
    return date_iso_format

def take_end_date():
    new_date = f"2024-{month}-{start_date[0]} 23:59"
    date_iso_format = datetime.fromisoformat(new_date).isoformat()
    return date_iso_format

def create_event():
    event_title = take_event_title()
    time.sleep(1)
    event_desc = take_event_description()
    time.sleep(1)
    event_start_date =take_start_date()
    time.sleep(1)
    event_end_date = take_end_date()
    time.sleep(1)
    calendar_service = get_calendar_service()
    event_result = calendar_service.events().insert(calendarId='primary',
        body={
            "summary": event_title,
            "description": event_desc,
            "start":{
                "datetime": event_start_date,
                "timezone": "America/Monterrey"
            },
            "end":{
                "datetime": event_end_date,
                "timezone": "America/Monterrey"
            }
        }    
    ).execute()

    