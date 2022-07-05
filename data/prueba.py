# importanto librerias
import pandas as pd
import numpy as np

# leyendo el csv

informacion=pd.read_csv('datosBien.csv')

# mostrando los 5 primeros informacion
print(informacion.head(5))

# seleccionando los sentimientos generados para la etapa inicial de cada variable que seran los generos
infoTerror = informacion[informacion['genero'].str.contains('terror')]
# todo : YA QUE EXTRAJE DEL DATA FRAME ORIGINAL todas las respuestas que me relacionan el la columna de terror debo crear un nuevo frame que solo me indique para terror cual fue el dato mas repetido osea la moda por cada columna
modaTerror=infoTerror.mode().dropna()
"""------------- crando aventura -----------------"""
infoAventura= informacion[informacion['genero'].str.contains('aventura')]
modaAventura=infoAventura.mode().dropna()
"""-------------- creanfo accion ------------------"""
infoAccion= informacion[informacion['genero'].str.contains('accion')]
modaAccion=infoAccion.mode().dropna()
"""-------------- creanfo modaDrama ------------------"""
infoDrama= informacion[informacion['genero'].str.contains('drama')]
modaDrama=infoDrama.mode().dropna()
"""------------------ uniendo los dataframe ----------"""
modaGlobal=pd.concat([modaTerror,modaDrama,modaAccion,modaAventura],ignore_index=True)
"""------------ con la nueva forma de presentarme la infor macion puedo observar la manejare para cerar graficas------------"""

