# Variables globales
salario_minimo = 1300000
subsidio_transporte = 162000
porcentaje_aporte_salud = 0.04
porcentaje_aporte_pension = 0.04
porcentaje_extra_diurno = 0.25
porcentaje_extra_nocturno = 0.75
porcentaje_extra_festivo = 0.75
porcentaje_valor_de_incapacidad = 1.0

def calcular_valor_hora_extra_diurna(valor_hora_laborada, horas_extra_diurnas):
    """Calcula el valor de la hora extra diurna."""
    return (valor_hora_laborada + (valor_hora_laborada * porcentaje_extra_diurno)) * horas_extra_diurnas

def calcular_valor_hora_extra_nocturna(valor_hora_laborada, horas_extra_nocturnas):
    """Calcula el valor de la hora extra nocturna."""
    return (valor_hora_laborada + (valor_hora_laborada * porcentaje_extra_nocturno)) * horas_extra_nocturnas

def calcular_valor_hora_extra_festivo(valor_hora_laborada, valor_hora_extra_festivo):
    """Calcula el valor de la hora extra festiva."""
    return (valor_hora_laborada + (valor_hora_laborada * porcentaje_extra_festivo)) * valor_hora_extra_festivo

def calcular_valor_dias_festivos(valor_hora_laborada, tiempo_festivo_laborado):
    """Calcula el valor de los dias festivos laborados."""
    return (8*(valor_hora_laborada + (valor_hora_laborada * porcentaje_extra_festivo))) * tiempo_festivo_laborado

def calcular_valor_incapacidad(valor_hora_laborada, tiempo_incapacidades):
    """Calcula el valor de las incapacidades."""
    if tiempo_incapacidades <= 2:
        return (valor_hora_laborada * 8) * tiempo_incapacidades
    elif tiempo_incapacidades <= 90:
        return ((valor_hora_laborada * 8) * tiempo_incapacidades) * 0.6666
    else:
        return ((valor_hora_laborada * 8) * tiempo_incapacidades) * 0.5

def calcular_valor_licencia_no_remunerada(valor_hora_laborada, tiempo_licencias_no_remuneradas):
    """Calcula el valor de las licencias no remuneradas."""
    return ((valor_hora_laborada * 8) * tiempo_licencias_no_remuneradas)

def calcular_valor_fondo_solidaridad_pensional(salario_base_mensual):
    """Calcula el valor al fondo de solidaridad pensional."""
    smmlv = salario_base_mensual / 1300000 
    if smmlv > 20:
        return salario_base_mensual * 0.02
    elif 19 < smmlv <= 20:
        return salario_base_mensual * 0.018
    elif 18 < smmlv <= 19:
        return salario_base_mensual * 0.016
    elif 17 < smmlv <= 18:
        return salario_base_mensual * 0.014
    elif 16 < smmlv <= 17:
        return salario_base_mensual * 0.012
    elif 4 < smmlv <= 16:
        return salario_base_mensual * 0.01
    else:
        return 0
    
    
def solicitar_datos_entrada():
    """Solicita los datos de entrada al usuario."""
    salario_base_mensual = float(input("Ingrese el salario básico mensual: "))
    tiempo_laborado = float(input("Ingrese el tiempo laborado al mes en horas: "))
    tiempo_festivo_laborado = int(input("Ingrese el tiempo festivo laborado en días: "))
    horas_extra_diurnas = float(input("Ingrese las horas extras diurnas laboradas: "))
    horas_extra_nocturnas = float(input("Ingrese las horas extras nocturnas laboradas: "))
    horas_extra_festivos = float(input("Ingrese las horas extras festivas laboradas: "))
    tiempo_incapacidades = int(input("Ingrese el tiempo de incapacidades en días: "))
    tiempo_licencias_no_remuneradas = int(input("Ingrese el tiempo de licencias no remuneradas en días: "))
    return salario_base_mensual, tiempo_laborado, tiempo_festivo_laborado, horas_extra_diurnas, horas_extra_nocturnas, horas_extra_festivos, tiempo_incapacidades, tiempo_licencias_no_remuneradas

def mostrar_informacion(valor_salario, subsidio_transporte, valor_hora_extra_diurna, valor_hora_extra_nocturna, valor_hora_extra_festivo, valor_dias_festivos, valor_incapacidad, valor_licencia_no_remunerada, valor_aporte_a_salud, valor_aporte_a_pension, valor_fondo_solidaridad_pensional):
    """Muestra la información calculada en pantalla."""

    total_ingresos = valor_salario + subsidio_transporte + valor_dias_festivos + valor_hora_extra_diurna + valor_hora_extra_nocturna + valor_hora_extra_festivo + valor_incapacidad
    total_deducciones = valor_licencia_no_remunerada + valor_aporte_a_salud + valor_aporte_a_pension + valor_fondo_solidaridad_pensional
    total_neto = total_ingresos - total_deducciones
    
    print("\nInformación de liquidación de nómina:")
    print(f"Salario: {valor_salario}")
    print(f"Subsidio de transporte: {subsidio_transporte}")
    print(f"Valor días festivos: {valor_dias_festivos}")
    print(f"Valor horas extras diurnas: {valor_hora_extra_diurna}")
    print(f"Valor horas extras nocturnas: {valor_hora_extra_nocturna}")
    print(f"Valor horas extras festivas: {valor_hora_extra_festivo}")
    print(f"Valor de incapacidades: {valor_incapacidad}")
    print(f"Valor de licencia no remunerada: {valor_licencia_no_remunerada}")
    print(f"Valor aporte a salud: {valor_aporte_a_salud}")
    print(f"Valor aporte a pensión: {valor_aporte_a_pension}")
    print(f"Valor al fondo de solidaridad pensional: {valor_fondo_solidaridad_pensional}")
    print(f"Total a pagar/neto: {total_neto}")

def modificar_parametros():
    """Permite al usuario modificar los parámetros globales."""
    global subsidio_transporte, porcentaje_aporte_salud, porcentaje_aporte_pension, porcentaje_extra_diurno, porcentaje_extra_nocturno, porcentaje_extra_festivo
    print("\nModificar parámetros:")
    
    nuevo_subsidio = input("Nuevo valor de subsidio de transporte (DEF para dejar como está): ")
    if nuevo_subsidio.upper() != "DEF":
        subsidio_transporte = float(nuevo_subsidio)
    
    nuevo_salud = input("Nuevo % de aporte a salud (DEF para dejar como está): ")
    if nuevo_salud.upper() != "DEF":
        porcentaje_aporte_salud = float(nuevo_salud)
    
    nuevo_pension = input("Nuevo % de aporte a pensión (DEF para dejar como está): ")
    if nuevo_pension.upper() != "DEF":
        porcentaje_aporte_pension = float(nuevo_pension)
    
    nuevo_extra_diurno = input("Nuevo % de valor de hora extra diurna (DEF para dejar como está): ")
    if nuevo_extra_diurno.upper() != "DEF":
        porcentaje_extra_diurno = float(nuevo_extra_diurno)
    
    nuevo_extra_nocturno = input("Nuevo % de valor de hora extra nocturna (DEF para dejar como está): ")
    if nuevo_extra_nocturno.upper() != "DEF":
        porcentaje_extra_nocturno = float(nuevo_extra_nocturno)
    
    nuevo_extra_festivo = input("Nuevo % de valor de hora extra festiva (DEF para dejar como está): ")
    if nuevo_extra_festivo.upper() != "DEF":
        porcentaje_extra_festivo = float(nuevo_extra_festivo)
    
    print("Parámetros modificados correctamente.")

def mostrar_menu():
    """Muestra el menú de opciones."""
    print("\nMenú:")
    print("1. Calcular liquidación de nómina")
    print("2. Modificar parámetros")
    print("3. Salir")

def main():
    """Función principal del programa."""
    print("Bienvenido al sistema de liquidación de nómina")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            salario_base_mensual, tiempo_laborado, tiempo_festivo_laborado, horas_extra_diurnas, horas_extra_nocturnas, horas_extra_festivos, tiempo_incapacidades, tiempo_licencias_no_remuneradas = solicitar_datos_entrada()

            # Cálculo de valores
            valor_hora_laborada = salario_base_mensual / 192
            valor_salario = valor_hora_laborada * tiempo_laborado
            valor_hora_extra_diurna = calcular_valor_hora_extra_diurna(valor_hora_laborada, horas_extra_diurnas)
            valor_hora_extra_nocturna = calcular_valor_hora_extra_nocturna(valor_hora_laborada, horas_extra_nocturnas)
            valor_hora_extra_festivo = calcular_valor_hora_extra_festivo(valor_hora_laborada, horas_extra_festivos)
            valor_dias_festivos = calcular_valor_dias_festivos(valor_hora_laborada, tiempo_festivo_laborado)
            valor_incapacidad = calcular_valor_incapacidad(valor_hora_laborada, tiempo_incapacidades)
            valor_licencia_no_remunerada = calcular_valor_licencia_no_remunerada(valor_hora_laborada, tiempo_licencias_no_remuneradas)
            valor_aporte_a_salud = ((valor_salario) + (subsidio_transporte) +(valor_dias_festivos)+(valor_hora_extra_diurna)+(valor_hora_extra_nocturna)+(valor_hora_extra_festivo)) * porcentaje_aporte_salud
            valor_aporte_a_pension = ((valor_salario) + (subsidio_transporte) +(valor_dias_festivos)+(valor_hora_extra_diurna)+(valor_hora_extra_nocturna)+(valor_hora_extra_festivo)) * porcentaje_aporte_pension
            valor_fondo_solidaridad_pensional = calcular_valor_fondo_solidaridad_pensional(salario_base_mensual)

            # Mostrar información en pantalla
            mostrar_informacion(valor_salario, subsidio_transporte, valor_hora_extra_diurna, valor_hora_extra_nocturna, valor_hora_extra_festivo, valor_dias_festivos, valor_incapacidad, valor_licencia_no_remunerada, valor_aporte_a_salud, valor_aporte_a_pension, valor_fondo_solidaridad_pensional)

        elif opcion == "2":
            modificar_parametros()

        elif opcion == "3":
            print("Gracias por usar el sistema de liquidación de nómina")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()