import pandas as pd

def get_constants(HA):

    num_pacientes=HA.shape[0]
    edad_promedio=round(float(HA['Edad'].mean()),0)
    tiempo_seguimiento=round(float(HA['Tiempo'].mean()),0)
    factores_de_riesgo = len(HA.columns)-1

    return num_pacientes,edad_promedio,tiempo_seguimiento,factores_de_riesgo