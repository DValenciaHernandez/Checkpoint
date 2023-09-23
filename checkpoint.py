# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

# Recordar utilizar la ruta relativa, no la absoluta para ingestar los datos desde los CSV.
# EJ: 'datasets/xxxxxxxxxx.csv'

import csv
from xml.dom.minidom import Entity
import pandas as pd
import numpy as np

def Ret_Pregunta01():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar la cantidad de registros cuya entidad sean Colombia o México retornando ese valor en un dato de tipo tupla (catidad de registros Colombia, catidad de registros México).
    Pista: averiguar la funcion Shape
    '''
    #Tu código aca:
    def contar_registros_pais(Fuentes_Consumo_Energia_csv):
        df = pd.read_csv(Fuentes_Consumo_Energia_csv)  
        registros_colombia = df[df['entidad'] == 'Colombia'].shape[0]
        registros_mexico = df[df['entidad'] == 'México'].shape[0]
        return registros_colombia, registros_mexico


    

def Ret_Pregunta02():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe eliminar las columnas 'Code' y 'Entity' y luego informar la cantidad de columnas
    retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca: 
    def ingestar_y_procesar_csv(Fuentes_Consumo_Energia_csv):
        df = pd.read_csv(Fuentes_Consumo_Energia_csv)
        df.drop(['Code', 'Entity'], axis=1, inplace=True)
        cantidad_columnas = len(df.columns)
        cantidad_columnas = ingestar_y_procesar_csv(Fuentes_Consumo_Energia_csv)
        return cantidad_columnas
    

def Ret_Pregunta03():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar la cantidad de registros de la columna Year sin tener en cuenta aquellos con valores faltantes
    retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:
    
    def contar_registros_con_year_no_nulos(Fuentes_Consumo_Energia_csv):
        df = pd.read_csv(Fuentes_Consumo_Energia_csv)
        registros_con_year_no_nulos = df['Year'].notnull().sum()
        registros_con_year_no_nulos = contar_registros_con_year_no_nulos(Fuentes_Consumo_Energia_csv)
        return registros_con_year_no_nulos

    

def Ret_Pregunta04():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    El ExaJulio es una unidad diferentes al TWh, es decir, no tiene sentido sumarlos o
    buscar proporciones entre ellos, la fórmula de conversión es:
    277.778 Teravatios/Hora (TWh) = 1 Exajulio
    Los campos terminados en "_EJ" corresponden a mediciones en Exajulios,
    y los terminados en "_TWh" corresponden a Teravatios/Hora.
    La consigna es crear un nuevo campo, que se denomine "Consumo_Total"
    y que guarde la sumatoria de todos los consumos expresados en Teravatios/Hora
    (convirtiendo a esta medida los que están en Exajulios)
    Esta función debe informar el consumo total para la entidad 'World' y año '2019',
    redondeado a 2 decimales, retornando ese valor en un dato de tipo float.
    '''
    #Tu código aca:
    #return 'Funcion incompleta'

def Ret_Pregunta05():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar el año de mayor generación de energía hídrica (Hydro_Generation_TWh)
    para la entidad 'Europe' retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:
    def obtener_ano_maxima_generacion_hidrica(Fuentes_Consumo_Energia_csv):
        df = pd.read_csv(Fuentes_Consumo_Energia_csv)
        df_europe = df[df['Entity'] == 'Europe']
        ano_max_generacion_hidrica = df_europe.loc[df_europe['Hydro_Generation_TWh'].idxmax(), 'Year']
        ano_max_generacion_hidrica = obtener_ano_maxima_generacion_hidrica(Fuentes_Consumo_Energia_csv)
        return int(ano_max_generacion_hidrica)
archivo_csv = "Fuentes_Consumo_Energia.csv"


def Ret_Pregunta06(m1, m2, m3):
    '''
    Esta función recibe tres array de Numpy de 2 dimensiones cada uno, y devuelve el valor booleano
    True si es posible realizar una multiplicación entre las tres matrices (n1 x n2 x n3),
    y el valor booleano False si no lo es
    Ej:
        n1 = np.array([[0,0,0],[1,1,1],[2,2,2]])
        n2 = np.array([[3,3],[4,4],[5,5]])
        n3 = np.array([1,1],[2,2])
        print(Ret_Pregunta06(n1,n2,n3))
            True            -> Valor devuelto por la función en este ejemplo
        print(Ret_Pregunta06(n2,n1,n3))
            False            -> Valor devuelto por la función en este ejemplo
    '''
    #Tu código aca:
    def check_shapes(m1,m2,m3):
        m1 = np.asarray(m1)
        m2 = np.asarray(m2)
        m3 = np.asarray(m3)
    if m1.shape == m2.shape == m3.shape:
        return True
    else:
        return False

def Ret_Pregunta07():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto 
    "GGAL - Cotizaciones historicas.csv". Este csv contiene información de cotización de la 
    acción del Banco Galcia SA. Esta función debe tomar la columna máximo y 
    devolver la suma de los valores de esta, con 4 decimales después del punto, redondeado.
    '''
    #Tu código aca:
    archivo_csv = "GGAL - Cotizaciones historicas.csv"

    def suma_maximos_cotizacion(GGAL_Cotizaciones_historicas_csv):
        df = pd.read_csv(GGAL_Cotizaciones_historicas_csv)
        suma_maximos = round(df['máximo'].sum(), 4)
        suma_maximos = suma_maximos_cotizacion(GGAL_Cotizaciones_historicas_csv)
        return suma_maximos

archivo_csv = "GGAL - Cotizaciones historicas.csv"

def Ret_Pregunta08():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar la cantidad de entidades diferentes que están presentes en el dataset
    retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:
    df = pd.read_csv('Fuentes_Consumo_Energia.csv')
    return df['Entidad'].nunique()

def Ret_Pregunta09():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "datasets/Tabla1_ejercicio.csv" y "datasets/Tabla2_ejercicio.csv".
    Esta función debe retornar: score_promedio_femenino y score_promedio_masculino en formato tupla, teniendo en cuenta que no debe haber valores repetidos.'''
    #Tu código aca:
    def calcular_score_promedio_por_genero(tabla1_ejercicio, tabla2_ejercicio):
        tabla1_df = pd.read_csv(tabla1_ejercicio)
        tabla2_df = pd.read_csv(tabla2_ejercicio)
        
        score_promedio_femenino = tabla1_df[tabla1_df['gender'] == 'female']['score'].mean()
        score_promedio_masculino = tabla2_df[tabla2_df['gender'] == 'male']['score'].mean()
        
        score_promedio_femenino = round(score_promedio_femenino, 2) if not pd.isnull(score_promedio_femenino) else None
        score_promedio_masculino = round(score_promedio_masculino, 2) if not pd.isnull(score_promedio_masculino) else None
        
        score_promedio_femenino, score_promedio_masculino = calcular_score_promedio_por_genero(tabla1_ejercicio, tabla2_ejercicio)

        return (score_promedio_femenino, score_promedio_masculino)
        

tabla1_path = "datasets/Tabla1_ejercicio.csv"
tabla2_path = "datasets/Tabla2_ejercicio.csv"
        


def Ret_Pregunta10(lista):
    '''
    Esta función recibe como parámetro un objeto de la clase Lista() definida en el archivo Lista.py.
    Debe recorrer la lista y retornan la cantidad de nodos que posee. Utilizar el método de la clase
    Lista llamado getCabecera()
    Ejemplo:
        lis = Lista()
        lista.agregarElemento(1)
        lista.agregarElemento(2)
        lista.agregarElemento(3)
        print(Ret_Pregunta10(lista))
            3    -> Debe ser el valor devuelto por la función Ret_Pregunta10() en este ejemplo
    '''
    #Tu código aca:
    
