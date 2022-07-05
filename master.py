# importanto librerias
import pandas as pd
import numpy as np

# leyendo el csv
datos = pd.read_csv('data/datosBien.csv')

# mostrando los 5 primeros datos
print(datos.head(5))

# seleccionando los sentimientos generados para la etapa inicial de cada variable que seran los generos
infoTerror = datos[datos['genero'].str.contains('terror')]
"""--------------para la variable terror----------------"""
modaTerrorInicial = infoTerror['sentimiento etapa inicial'].mode()
print(modaTerrorInicial)
modaTerrorMedia = infoTerror['sentimiento etapa media'].mode()
modaTerrorFinal = infoTerror['sentimiento etapa final'].mode()
"""..--------------------- para la variable drama ---------------"""
infoDrama = datos[datos['genero'].str.contains('drama')]
modaDramaInicial = infoDrama['sentimiento etapa inicial'].mode()
print(modaDramaInicial)
modaDramaMedia = infoDrama['sentimiento etapa media'].mode()
modaDramaFinal = infoDrama['sentimiento etapa final'].mode()
"""..--------------------- para la variable accion ---------------"""
infoAccion = datos[datos['genero'].str.contains('accion')]
modaAccionInicial = infoAccion['sentimiento etapa inicial'].mode()
print(modaAccionInicial)
modaAccionMedia = infoAccion['sentimiento etapa media'].mode()
modaAccionFinal = infoAccion['sentimiento etapa final'].mode()
"""..--------------------- para la variable aventuras ---------------"""
infoAventuras = datos[datos['genero'].str.contains('aventuras')]
modaAventurasInicial = infoAventuras['sentimiento etapa inicial'].mode()
print(modaAventurasInicial)
modaAventurasMedia = infoAventuras['sentimiento etapa media'].mode()
type(modaAventurasMedia)
modaAventurasFinal = infoAventuras['sentimiento etapa final'].mode()



