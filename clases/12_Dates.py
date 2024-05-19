#Fechas
from datetime import datetime


#primero definir la fecha
now = datetime.now()
"""

print(now)
#print(now.day)
#print(now.minute)
#print(now.year)

tp = now.timestamp()
print(tp)
"""

#introducior una fecha
fecha_cumple = datetime(1982,7,12)
print(f"fecha_cumple: {fecha_cumple}")

from datetime import date
fecha_aleatoria = date(2000,7,12)
print(f"Fecha_aletoria: {fecha_aleatoria}")

from datetime import timedelta
resultado = now - fecha_cumple

print(resultado)

