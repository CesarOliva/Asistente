from datetime import datetime, timedelta
from calendar import get_calendar_service
import time

def take_event_title():
    pass

def create_event():
    calendar_service = get_calendar_service()

    event_result = calendar_service.events().insert(calendarId='primary',
        body={
            "summary": "Titulo del evento",
            "description": "Descripcion del evento",
            "start":{
                "datetime": "Fecha de Inicio",
                "timezone": "America/Monterrey"
            },
            "end":{
                "datetime": "Fecha de Fin",
                "timezone": "America/Monterrey"
            }
        }    
    ).execute()
