# Variables globales
salario_minimo = 1300000
subsidio_transporte = 162000
porcentaje_aporte_salud = 0.04
porcentaje_aporte_pension = 0.04
porcentaje_extra_diurno = 0.25
porcentaje_extra_nocturno = 0.75
porcentaje_extra_festivo = 0.75
porcentaje_valor_de_incapacidad = 1.0
COMO_USAR_MENSAJE = """Modificación de parámetros: En la opción de modificar parámetros, puedes cambiar los valores que se utilizan en los cálculos de la calculadora. Por ejemplo, puedes cambiar el valor de la hora laborada, el número de horas extras diurnas, el número de horas extras nocturnas, etc. Para hacer esto, simplemente selecciona la opción de modificar parámetros en el menú, luego ingresa el nuevo valor para el parámetro que deseas cambiar.

Manejo de porcentajes: En muchos cálculos financieros y de nómina, se utilizan porcentajes. En la calculadora, estos porcentajes se manejan como valores decimales. Por ejemplo, un 75% se representa como 0.75. Esto se debe a que en matemáticas, un porcentaje es simplemente una forma de representar una fracción con denominador 100. Entonces, 75% es lo mismo que 75/100, que es igual a 0.75.

Ahora, veamos un ejemplo de uso de la calculadora con el salario mínimo en Colombia. Supongamos que el salario mínimo mensual legal vigente (SMMLV) en Colombia es de $908,526 COP para el año 2024.

Ingresar el valor de la hora laborada: Primero, necesitamos calcular el valor de la hora laborada. Esto se hace dividiendo el salario mínimo mensual por el número total de horas laboradas en un mes. Supongamos que se trabaja 8 horas al día, 5 días a la semana, durante 4 semanas al mes. Eso suma un total de 160 horas al mes. Entonces, el valor de la hora laborada sería $908,526 / 160 = $5,678.29 COP.
Calcular el valor de las horas extras: Supongamos que se trabajaron 2 horas extras diurnas y 3 horas extras nocturnas. Usando la calculadora, podemos calcular el valor de estas horas extras. Las horas extras diurnas se pagan con un recargo del 25% sobre el valor de la hora laborada, y las horas extras nocturnas se pagan con un recargo del 75%. Entonces, el valor de las horas extras diurnas sería $11,829.76 COP, y el valor de las horas extras nocturnas sería $24,842.50 COP.
Calcular el valor de los días festivos: Supongamos que se trabajó 1 día festivo. Los días festivos se pagan con un recargo del 75% sobre el valor del día laborado. Entonces, el valor del día festivo sería $66,246.68 COP.
Calcular el valor de las incapacidades: Supongamos que se tuvo 1 día de incapacidad. Las incapacidades se pagan con el valor del día laborado. Entonces, el valor de la incapacidad sería $37,855.25 COP.
Calcular el valor del fondo de solidaridad pensional: Este fondo se aplica a quienes ganan más de 4 SMMLV. Como en este caso el salario es de 1 SMMLV, no se aplica el fondo de solidaridad pensional.
El valor al aporte de fondo de salud y pension serian del 4% del total del sueldo que seria $40,880.95 COP. cada uno por defecto.
Teniendo un subsidio de transporte base de $162,000.00 COP
Nos daria un Total a pagar Neto de $978,117.29 COP"""


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
    smmlv = salario_base_mensual / salario_minimo
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
    global salario_minimo,subsidio_transporte, porcentaje_aporte_salud, porcentaje_aporte_pension, porcentaje_extra_diurno, porcentaje_extra_nocturno, porcentaje_extra_festivo
    print("\nModificar parámetros:")
    

    nuevo_salario_minimo = input("Nuevo valor del salario minimo (DEF para dejar como está): ")
    if nuevo_salario_minimo.upper() != "DEF":
        salario_minimo = float(nuevo_salario_minimo)

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
    print("3. Como usar")
    print("4. Salir")

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
            print(COMO_USAR_MENSAJE)

        elif opcion == "4":
            print("Gracias por usar el sistema de liquidación de nómina")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()