import pytest
from liquidacion_nomina.liquidador_nomina import calcular_valor_hora_extra_diurna,calcular_valor_hora_extra_nocturna,calcular_valor_hora_extra_festivo,calcular_valor_dias_festivos, calcular_valor_incapacidad, calcular_valor_licencia_no_remunerada, calcular_valor_fondo_solidaridad_pensional, solicitar_datos_entrada



#-----------------------------Funcion calcular_valor_hora_extra_diurna_normal

# Casos de prueba normales
@pytest.mark.parametrize("valor_hora_laborada, horas_extra_diurnas, expected", [
    (10000, 2, 25000),  
    (20000, 3, 75000), 
    (15000, 1, 18750)   
])
def test_calcular_valor_hora_extra_diurna_normal(valor_hora_laborada, horas_extra_diurnas, expected):
    assert calcular_valor_hora_extra_diurna(valor_hora_laborada, horas_extra_diurnas) == expected

# Casos de prueba extraordinarios
@pytest.mark.parametrize("valor_hora_laborada, horas_extra_diurnas, expected", [
    (0, 2, 0),  # caso extraordinario: valor de hora laborada es 0
    (10000, 0, 0),  # caso extraordinario: horas extra diurnas es 0
    (-10000, 2, -25000)  # caso extraordinario: valor de hora laborada es negativo
])
def test_calcular_valor_hora_extra_diurna_extraordinario(valor_hora_laborada, horas_extra_diurnas, expected):
    assert calcular_valor_hora_extra_diurna(valor_hora_laborada, horas_extra_diurnas) == expected

# Casos de prueba de error
@pytest.mark.parametrize("valor_hora_laborada, horas_extra_diurnas", [
    ("10000", 2),  # caso de error: valor de hora laborada no es un número
    (10000, "2"),  # caso de error: horas extra diurnas no es un número
    (None, 2),  # caso de error: valor de hora laborada es None
    (10000, None)  # caso de error: horas extra diurnas es None
])
def test_calcular_valor_hora_extra_diurna_error(valor_hora_laborada, horas_extra_diurnas):
    with pytest.raises(TypeError):
        calcular_valor_hora_extra_diurna(valor_hora_laborada, horas_extra_diurnas)

#-----------------------------Funcion calcular_valor_hora_extra_nocturna_normal

# Casos de prueba normales
@pytest.mark.parametrize("valor_hora_laborada, horas_extra_nocturnas, expected", [
    (10000, 2, 35000), 
    (20000, 3, 105000),  
    (15000, 1, 26250)   
])
def test_calcular_valor_hora_extra_nocturna_normal(valor_hora_laborada, horas_extra_nocturnas, expected):
    assert calcular_valor_hora_extra_nocturna(valor_hora_laborada, horas_extra_nocturnas) == expected

# Casos de prueba extraordinarios
@pytest.mark.parametrize("valor_hora_laborada, horas_extra_nocturnas, expected", [
    (0, 2, 0),  # caso extraordinario: valor de hora laborada es 0
    (10000, 0, 0),  # caso extraordinario: horas extra nocturnas es 0
    (-10000, 2, -35000)  # caso extraordinario: valor de hora laborada es negativo
])
def test_calcular_valor_hora_extra_nocturna_extraordinario(valor_hora_laborada, horas_extra_nocturnas, expected):
    assert calcular_valor_hora_extra_nocturna(valor_hora_laborada, horas_extra_nocturnas) == expected

# Casos de prueba de error
@pytest.mark.parametrize("valor_hora_laborada, horas_extra_nocturnas", [
    ("10000", 2),  # caso de error: valor de hora laborada no es un número
    (10000, "2"),  # caso de error: horas extra nocturnas no es un número
    (None, 2),  # caso de error: valor de hora laborada es None
    (10000, None)  # caso de error: horas extra nocturnas es None
])
def test_calcular_valor_hora_extra_nocturna_error(valor_hora_laborada, horas_extra_nocturnas):
    with pytest.raises(TypeError):
        calcular_valor_hora_extra_nocturna(valor_hora_laborada, horas_extra_nocturnas)



#-----------------------------Funcion calcular_valor_hora_extra_festivo

# Casos de prueba normales
@pytest.mark.parametrize("valor_hora_laborada, valor_hora_extra_festivo, expected", [
    (10000, 2, 35000),  
    (20000, 3, 105000), 
    (15000, 1, 26250)  
])
def test_calcular_valor_hora_extra_festivo_normal(valor_hora_laborada, valor_hora_extra_festivo, expected):
    assert calcular_valor_hora_extra_festivo(valor_hora_laborada, valor_hora_extra_festivo) == expected

# Casos de prueba extraordinarios
@pytest.mark.parametrize("valor_hora_laborada, valor_hora_extra_festivo, expected", [
    (0, 2, 0),  # caso extraordinario: valor de hora laborada es 0
    (10000, 0, 0),  # caso extraordinario: valor de hora extra festivo es 0
    (-10000, 2, -35000)  # caso extraordinario: valor de hora laborada es negativo
])
def test_calcular_valor_hora_extra_festivo_extraordinario(valor_hora_laborada, valor_hora_extra_festivo, expected):
    assert calcular_valor_hora_extra_festivo(valor_hora_laborada, valor_hora_extra_festivo) == expected

# Casos de prueba de error
@pytest.mark.parametrize("valor_hora_laborada, valor_hora_extra_festivo", [
    ("10000", 2),  # caso de error: valor de hora laborada no es un número
    (10000, "2"),  # caso de error: valor de hora extra festivo no es un número
    (None, 2),  # caso de error: valor de hora laborada es None
    (10000, None)  # caso de error: valor de hora extra festivo es None
])
def test_calcular_valor_hora_extra_festivo_error(valor_hora_laborada, valor_hora_extra_festivo):
    with pytest.raises(TypeError):
        calcular_valor_hora_extra_festivo(valor_hora_laborada, valor_hora_extra_festivo)


#-----------------------------Funcion calcular_valor_dias_festivos


# Casos de prueba normales
@pytest.mark.parametrize("valor_hora_laborada, tiempo_festivo_laborado, expected", [
    (10000, 2, 280000), 
    (20000, 3, 840000),  
    (15000, 1, 210000)   
])
def test_calcular_valor_dias_festivos_normal(valor_hora_laborada, tiempo_festivo_laborado, expected):
    assert calcular_valor_dias_festivos(valor_hora_laborada, tiempo_festivo_laborado) == expected

# Casos de prueba extraordinarios
@pytest.mark.parametrize("valor_hora_laborada, tiempo_festivo_laborado, expected", [
    (0, 2, 0),  # caso extraordinario: valor de hora laborada es 0
    (10000, 0, 0),  # caso extraordinario: tiempo festivo laborado es 0
    (-10000, 2, -280000)  # caso extraordinario: valor de hora laborada es negativo
])
def test_calcular_valor_dias_festivos_extraordinario(valor_hora_laborada, tiempo_festivo_laborado, expected):
    assert calcular_valor_dias_festivos(valor_hora_laborada, tiempo_festivo_laborado) == expected

# Casos de prueba de error
@pytest.mark.parametrize("valor_hora_laborada, tiempo_festivo_laborado", [
    ("10000", 2),  # caso de error: valor de hora laborada no es un número
    (10000, "2"),  # caso de error: tiempo festivo laborado no es un número
    (None, 2),  # caso de error: valor de hora laborada es None
    (10000, None)  # caso de error: tiempo festivo laborado es None
])
def test_calcular_valor_dias_festivos_error(valor_hora_laborada, tiempo_festivo_laborado):
    with pytest.raises(TypeError):
        calcular_valor_dias_festivos(valor_hora_laborada, tiempo_festivo_laborado)


#-----------------------------Funcion calcular_valor_incapacidad


# Casos de prueba normales
@pytest.mark.parametrize("valor_hora_laborada, tiempo_incapacidades, expected", [
    (10000, 2, 160000),  
    (20000, 1, 160000), 
    (15000, 3, 239976)  
])
def test_calcular_valor_incapacidad_normal(valor_hora_laborada, tiempo_incapacidades, expected):
    assert calcular_valor_incapacidad(valor_hora_laborada, tiempo_incapacidades) == expected

# Casos de prueba extraordinarios
@pytest.mark.parametrize("valor_hora_laborada, tiempo_incapacidades, expected", [
    (0, 2, 0),  # caso extraordinario: valor de hora laborada es 0
    (10000, 0, 0),  # caso extraordinario: tiempo de incapacidades es 0
    (-10000, 2, -160000)  # caso extraordinario: valor de hora laborada es negativo
])
def test_calcular_valor_incapacidad_extraordinario(valor_hora_laborada, tiempo_incapacidades, expected):
    assert calcular_valor_incapacidad(valor_hora_laborada, tiempo_incapacidades) == expected

# Casos de prueba de error
@pytest.mark.parametrize("valor_hora_laborada, tiempo_incapacidades", [
    ("80-000@", 4),  # caso de error: valor de hora laborada no es un número
    (10000, "2"),  # caso de error: tiempo de incapacidades no es un número
    (None, 2),  # caso de error: valor de hora laborada es None
    (10000, None)  # caso de error: tiempo de incapacidades es None
])
def test_calcular_valor_incapacidad_error(valor_hora_laborada, tiempo_incapacidades):
    with pytest.raises(TypeError):
        calcular_valor_incapacidad(valor_hora_laborada, tiempo_incapacidades)



#-----------------------------Funcion calcular_valor_licencia_no_remunerada


# Casos de prueba normales
@pytest.mark.parametrize("valor_hora_laborada, tiempo_licencias_no_remuneradas, expected", [
    (10000, 2, 160000), 
    (20000, 3, 480000),  
    (15000, 1, 120000)  
])
def test_calcular_valor_licencia_no_remunerada_normal(valor_hora_laborada, tiempo_licencias_no_remuneradas, expected):
    assert calcular_valor_licencia_no_remunerada(valor_hora_laborada, tiempo_licencias_no_remuneradas) == expected

# Casos de prueba extraordinarios
@pytest.mark.parametrize("valor_hora_laborada, tiempo_licencias_no_remuneradas, expected", [
    (0, 2, 0),  # caso extraordinario: valor de hora laborada es 0
    (10000, 0, 0),  # caso extraordinario: tiempo de licencias no remuneradas es 0
    (-10000, 2, -160000)  # caso extraordinario: valor de hora laborada es negativo
])
def test_calcular_valor_licencia_no_remunerada_extraordinario(valor_hora_laborada, tiempo_licencias_no_remuneradas, expected):
    assert calcular_valor_licencia_no_remunerada(valor_hora_laborada, tiempo_licencias_no_remuneradas) == expected

# Casos de prueba de error
@pytest.mark.parametrize("valor_hora_laborada, tiempo_licencias_no_remuneradas", [
    ("vuevemil", "a2"),  # caso de error: valor de hora laborada no es un número
    ("1000a0", "s"),  # caso de error: tiempo de licencias no remuneradas no es un número
    (None, 2),  # caso de error: valor de hora laborada es None
    (10000, None)  # caso de error: tiempo de licencias no remuneradas es None
])
def test_calcular_valor_licencia_no_remunerada_error(valor_hora_laborada, tiempo_licencias_no_remuneradas):
    with pytest.raises(TypeError):
        calcular_valor_licencia_no_remunerada(valor_hora_laborada, tiempo_licencias_no_remuneradas)



#-----------------------------Funcion calcular_valor_fondo_solidaridad_pensional

# Casos de prueba normales
@pytest.mark.parametrize("salario_base_mensual, expected", [
    (1000000, 0), 
    (4000000, 0), 
    (5000000, 0) 
])
def test_calcular_valor_fondo_solidaridad_pensional_normal(salario_base_mensual, expected):
    assert calcular_valor_fondo_solidaridad_pensional(salario_base_mensual) == expected

# Casos de prueba extraordinarios
@pytest.mark.parametrize("salario_base_mensual, expected", [
    (0, 0),  # caso extraordinario: salario base mensual es 0
    (-1000000, 0),  # caso extraordinario: salario base mensual es negativo
    (10000000, 100000)  # caso extraordinario: salario base mensual es muy alto
])
def test_calcular_valor_fondo_solidaridad_pensional_extraordinario(salario_base_mensual, expected):
    assert calcular_valor_fondo_solidaridad_pensional(salario_base_mensual) == expected

# Casos de prueba de error
@pytest.mark.parametrize("salario_base_mensual", [
    ("1000000"),  # caso de error: salario base mensual no es un número
    (None),  # caso de error: salario base mensual es None
    ("mil"),  # caso de error: salario base mensual es una cadena no numérica
    ("10ty0"),  # caso de error: salario base mensual no es un número
])
def test_calcular_valor_fondo_solidaridad_pensional_error(salario_base_mensual):
    with pytest.raises(TypeError):
        calcular_valor_fondo_solidaridad_pensional(salario_base_mensual)



#-----------------------------Funcion solicitar_datos_entrada
        








# Funciones que se deben probar unitariamente:

#     Funciones de cálculo (como calcular_valor_hora_extra_diurna, calcular_valor_incapacidad, etc.): Estas funciones realizan cálculos basados en parámetros de entrada.

# Funciones que no necesitan pruebas unitarias:

#     Funciones de presentación (mostrar_informacion, modificar_parametros, mostrar_menu): Estas funciones se encargan de la presentación de datos al usuario o la modificación de variables globales. 

#     Función principal (main): La función principal interactúa con otras funciones y maneja el flujo de ejecución del programa. 