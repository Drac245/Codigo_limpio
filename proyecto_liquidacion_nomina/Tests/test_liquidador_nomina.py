import unittest
import pytest
from liquidacion_nomina.liquidador_nomina import calcular_valor_hora_extra_diurna


from liquidacion_nomina.liquidador_nomina import calcular_valor_hora_extra_diurna

@pytest.mark.parametrize("valor_hora_laborada, horas_extra_diurnas, expected", [
    (10000, 2, 10000.0),  # Caso normal 1
    (15000, 1.5, 11250.0),  # Caso normal 2
    (20000, 3, 30000.0),  # Caso normal 3
])
def test_casos_normales(valor_hora_laborada, horas_extra_diurnas, expected):
    """Prueba casos normales de la función calcular_valor_hora_extra_diurna."""
    resultado = calcular_valor_hora_extra_diurna(valor_hora_laborada, horas_extra_diurnas)
    assert resultado == expected








# Funciones que se deben probar unitariamente:

#     Funciones de cálculo (como calcular_valor_hora_extra_diurna, calcular_valor_incapacidad, etc.): Estas funciones realizan cálculos basados en parámetros de entrada.

#     Funciones de solicitud de entrada (solicitar_datos_entrada): Esta función solicita datos al usuario.

#     Función de cálculo de fondo de solidaridad pensional (calcular_valor_fondo_solidaridad_pensional)o según la lógica establecida.

# Funciones que no necesitan pruebas unitarias:

#     Funciones de presentación (mostrar_informacion, modificar_parametros, mostrar_menu): Estas funciones se encargan de la presentación de datos al usuario o la modificación de variables globales. 

#     Función principal (main): La función principal interactúa con otras funciones y maneja el flujo de ejecución del programa. 