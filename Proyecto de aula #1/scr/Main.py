import unittest
from io import StringIO
from unittest.mock import patch

def calcular_nomina():
    salario_basico = float(input("Ingrese el salario basico mensual: "))
    subsidio_transporte = float(input("Ingrese el subsidio de transporte: "))
    tiempo_laborado = str(input("Ingrese el tiempo laborado (# semana/quincena/decada/años): "))
    tiempo_festivo_laborado = int(input("Ingrese el tiempo festivo laborado (dias): "))
    horas_extra_diurnas = int(input("Ingrese las horas extras diurnas laboradas: "))
    horas_extra_nocturnas = int(input("Ingrese las horas extra nocturnas laboradas: "))
    horas_extra_festivas = int(input("Ingrese las horas extras festivas laboradas: "))
    porcentaje_salud = float(input("Ingrese el porcentaje de aporte a salud: %"))
    porcentaje_pension = float(input("Ingrese el porcentaje de aporte a pensión: %"))
    porcentaje_fondo_solidaridad = float(input("Ingrese el porcentaje de aporte al fondo de solidaridad pensional: %"))
    tiempo_incapacidades = int(input("Ingrese el tiempo de incapacidades (Horas): "))
    tiempo_licencias = int(input("Ingrese el tiempo de licencias (Horas): "))
    
    # Cálculos
    aux = tiempo_laborado.split(" ")

    if (aux[1] == "semana" or (aux[1] == "semanas")):
        salario = salario_basico * (float(aux[0]) / 4)
    elif (aux[1] == "mes" or aux[1] == "meses"):
        salario = salario_basico * float(aux[0])
    elif ( aux[1] == "quincena" or aux[1] == "quincenas"):
        salario = salario_basico * (float(aux[0]) / 2)
    elif ( aux[1] == "decada" or aux[1] == "decadas"):
        salario = salario_basico * float(aux[0]) * 12 * 10
    elif (aux[1] == "año" or aux[1] == "años" ):
        salario = salario_basico * float(aux[0]) * 12
    else:
        print("error")

    salario_basico_hora = salario_basico / 720
    salario_basico_dia = salario_basico / 30

    valor_festivos = salario_basico_dia * 1.75 * tiempo_festivo_laborado
    valor_horas_extra_diurnas = salario_basico_hora * horas_extra_diurnas * 1.25
    valor_horas_extra_nocturnas = salario_basico_hora * horas_extra_nocturnas * 1.35
    valor_horas_extra_festivas = salario_basico_hora * horas_extra_festivas * 2.10 # 75 por festivo, 35 por extras
    if ((porcentaje_salud+porcentaje_pension+porcentaje_fondo_solidaridad) < 100):
        aporte_salud = salario_basico * porcentaje_salud / 100
        aporte_pension = salario_basico * porcentaje_pension / 100
        aporte_fondo_solidaridad = salario_basico * porcentaje_fondo_solidaridad / 100
    else:
        aporte_salud = "error"
        aporte_pension = "error"
        aporte_fondo_solidaridad = "error"
    valor_incapacidades = salario_basico_hora * tiempo_incapacidades
    valor_licencias = salario_basico_hora * tiempo_licencias
    
    # Retención en la fuente (ejemplo arbitrario)
    retencion_fuente = salario_basico * 0.1
    
    # Total a pagar
    if aporte_salud != "error":
        total_pagar = (salario + subsidio_transporte + valor_festivos + valor_horas_extra_diurnas +
                   valor_horas_extra_nocturnas + valor_horas_extra_festivas + aporte_salud + aporte_pension +
                   aporte_fondo_solidaridad - valor_incapacidades - valor_licencias - retencion_fuente)
    else:
        total_pagar = "error"

    # Salida de resultados
    print("\n=== Ingresados ===")
    print(str(salario_basico)+","+str(subsidio_transporte)+","+str(tiempo_laborado)+","+str(tiempo_festivo_laborado)+","+str(horas_extra_diurnas)+","+
        str(horas_extra_nocturnas)+","+str(horas_extra_festivas)+","+str(porcentaje_salud)+","+str(porcentaje_pension)+","+
        str(porcentaje_fondo_solidaridad)+","+str(tiempo_incapacidades)+","+str(tiempo_licencias))
    print("\n=== Resultados ===")
    print("Salario: ", salario)
    print("Subsidio de transporte: ", subsidio_transporte)
    print("Valor festivos: ", valor_festivos)
    print("Valor horas extras diurnas laboradas: ", valor_horas_extra_diurnas)
    print("Valor horas extra nocturnas laboradas: ", valor_horas_extra_nocturnas)
    print("Valor horas extras festivas: ", valor_horas_extra_festivas)
    print("Valor aporte a salud: ", aporte_salud)
    print("Valor aporte a pensión: ", aporte_pension)
    print("Valor aporte fondo de solidaridad pensional: ", aporte_fondo_solidaridad)
    print("Valor incapacidades: ", valor_incapacidades)
    print("Valor licencias: ", valor_licencias)
    print("Retención en la fuente: ", retencion_fuente)
    print("Total a pagar: ", total_pagar)
    print(str(salario)+","+str(subsidio_transporte)+","+str(valor_festivos)+","+str(valor_horas_extra_diurnas)+","+str(valor_horas_extra_nocturnas)+","+
          str(valor_horas_extra_festivas)+","+str(aporte_salud)+","+str(aporte_pension)+","+str(aporte_fondo_solidaridad)+","+str(valor_incapacidades)+","+
          str(valor_licencias)+","+str(retencion_fuente)+","+str(total_pagar))
    print("///////////////////////////////////////////////////")

    return (salario,subsidio_transporte,valor_festivos,valor_horas_extra_diurnas,valor_horas_extra_nocturnas,
            valor_horas_extra_festivas,aporte_salud,aporte_pension,aporte_fondo_solidaridad,valor_incapacidades,
            valor_licencias,retencion_fuente,total_pagar)

for i in range(20):
    calcular_nomina()
