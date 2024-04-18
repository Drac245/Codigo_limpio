from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import Screen, ScreenManager

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        # Crear un diseño principal vertical
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Título de la aplicación
        header_label = Label(text="Liquidación de Nómina", size_hint_y=None, height=40,
                             font_size='20sp', bold=True)
        main_layout.add_widget(header_label)

        # Crear un diseño de cuadrícula para las entradas de datos
        input_layout = GridLayout(cols=2, row_default_height=40, row_force_default=True,
                                  spacing=10, padding=10)

        # Agregar los campos de entrada
        input_layout.add_widget(Label(text="Salario base mensual:"))
        self.salario_input = TextInput(multiline=False)
        input_layout.add_widget(self.salario_input)

        input_layout.add_widget(Label(text="Tiempo laborado al mes (horas):"))
        self.tiempo_laborado_input = TextInput(multiline=False)
        input_layout.add_widget(self.tiempo_laborado_input)

        input_layout.add_widget(Label(text="Tiempo festivo laborado (días):"))
        self.tiempo_festivo_laborado_input = TextInput(multiline=False)
        input_layout.add_widget(self.tiempo_festivo_laborado_input)

        input_layout.add_widget(Label(text="Horas extras diurnas laboradas:"))
        self.horas_extra_diurnas_input = TextInput(multiline=False)
        input_layout.add_widget(self.horas_extra_diurnas_input)

        input_layout.add_widget(Label(text="Horas extras nocturnas laboradas:"))
        self.horas_extra_nocturnas_input = TextInput(multiline=False)
        input_layout.add_widget(self.horas_extra_nocturnas_input)

        input_layout.add_widget(Label(text="Horas extras festivas laboradas:"))
        self.horas_extra_festivas_input = TextInput(multiline=False)
        input_layout.add_widget(self.horas_extra_festivas_input)

        input_layout.add_widget(Label(text="Incapacidades (días):"))
        # Asegurar que las entradas sean válidas
        self.incapacidades_input = TextInput(multiline=False)
        input_layout.add_widget(self.incapacidades_input)

        input_layout.add_widget(Label(text="Licencias no remuneradas (días):"))
        # Asegurar que las entradas sean válidas
        self.licencias_no_remuneradas_input = TextInput(multiline=False)
        input_layout.add_widget(self.licencias_no_remuneradas_input)

        # Añadir diseño de entradas al diseño principal
        main_layout.add_widget(input_layout)

        # Crear un diseño de scroll para los resultados
        resultado_scroll_view = ScrollView(size_hint_y=1)
        
        # Etiqueta para mostrar los resultados
        self.resultado_label = Label(text="", size_hint_y=None, height=40)
        resultado_scroll_view.add_widget(self.resultado_label)

        # Añadir el diseño de scroll de resultados al diseño principal
        main_layout.add_widget(resultado_scroll_view)

        # Botón para calcular la nómina ubicado en la parte inferior de la aplicación
        self.calcular_button = Button(text="Calcular liquidación de nómina",
                                      size_hint_y=None, height=40)
        self.calcular_button.bind(on_press=self.calcular_nomina)
        
        # Añadir el botón de cálculo al final del diseño principal
        main_layout.add_widget(self.calcular_button)

        # Asignar el diseño principal a la pantalla
        self.add_widget(main_layout)

    def validar_entrada(self, entrada):
        """Intenta convertir una entrada a float. Devuelve None si falla."""
        try:
            valor = float(entrada)
            return valor
        except ValueError:
            return None

    def mostrar_error(self, mensaje):
        """Muestra un mensaje de error en un Popup."""
        popup = Popup(title="Error",
                      content=Label(text=mensaje, size_hint=(0.5, 0.5)),
                      size_hint=(0.5, 0.5))
        popup.open()

    def calcular_nomina(self, instance):
        # Validar las entradas
        salario_base_mensual = self.validar_entrada(self.salario_input.text)
        tiempo_laborado = self.validar_entrada(self.tiempo_laborado_input.text)
        tiempo_festivo_laborado = self.validar_entrada(self.tiempo_festivo_laborado_input.text)
        horas_extra_diurnas = self.validar_entrada(self.horas_extra_diurnas_input.text)
        horas_extra_nocturnas = self.validar_entrada(self.horas_extra_nocturnas_input.text)
        horas_extra_festivas = self.validar_entrada(self.horas_extra_festivas_input.text)
        incapacidades = self.validar_entrada(self.incapacidades_input.text)
        licencias_no_remuneradas = self.validar_entrada(self.licencias_no_remuneradas_input.text)

        # Verificar si alguna entrada es inválida
        if any(value is None for value in [salario_base_mensual, tiempo_laborado, tiempo_festivo_laborado, horas_extra_diurnas, horas_extra_nocturnas, horas_extra_festivas, incapacidades, licencias_no_remuneradas]):
            self.mostrar_error("Por favor, ingrese valores válidos en todas las casillas.")
            return

        # Variables de configuración (porcentajes y valores fijos)
        porcentaje_aporte_salud = 0.04  # 4% de aportes a salud
        porcentaje_aporte_pension = 0.04  # 4% de aportes a pensión
        subsidio_transporte = 100  # Valor del subsidio de transporte (debe verificar el valor exacto)
        dias_trabajo_mensuales = 30

        # Calcular valores
        valor_hora_laborada = salario_base_mensual / 192
        valor_salario = valor_hora_laborada * tiempo_laborado
        valor_días_festivos = valor_hora_laborada * tiempo_festivo_laborado
        valor_horas_extra_diurnas = horas_extra_diurnas * valor_hora_laborada * 1.25
        valor_horas_extra_nocturnas = horas_extra_nocturnas * valor_hora_laborada * 1.75
        valor_horas_extra_festivas = horas_extra_festivas * valor_hora_laborada * 2
        valor_incapacidades = -valor_hora_laborada * incapacidades
        valor_licencias_no_remuneradas = -valor_hora_laborada * licencias_no_remuneradas

        # Calcular aportes a salud, pensión y fondo de solidaridad pensional
        base_de_aporte = valor_salario + subsidio_transporte + valor_días_festivos + valor_horas_extra_diurnas + valor_horas_extra_nocturnas + valor_horas_extra_festivas
        valor_aporte_a_salud = base_de_aporte * porcentaje_aporte_salud
        valor_aporte_a_pension = base_de_aporte * porcentaje_aporte_pension
        
        # Verifique si el salario base mensual excede los 4 salarios mínimos para determinar el fondo de solidaridad pensional
        salario_minimo_mensual = 1000  # Suponga que este es el salario mínimo, ajuste según sea necesario
        if salario_base_mensual > 4 * salario_minimo_mensual:
            porcentaje_fondo_solidaridad_pensional = 0.01  # 1% al fondo de solidaridad pensional
            valor_fondo_solidaridad_pensional = base_de_aporte * porcentaje_fondo_solidaridad_pensional
        else:
            valor_fondo_solidaridad_pensional = 0
        
        # Calcular totales
        total_ingresos = valor_salario + subsidio_transporte + valor_días_festivos + valor_horas_extra_diurnas + valor_horas_extra_nocturnas + valor_horas_extra_festivas
        total_deducciones = valor_incapacidades + valor_licencias_no_remuneradas + valor_aporte_a_salud + valor_aporte_a_pension + valor_fondo_solidaridad_pensional
        total_neto = total_ingresos - total_deducciones

        # Mostrar los resultados
        self.resultado_label.text = (
            f"Salario base mensual: {valor_salario:.2f}\n"
            f"Subsidio de transporte: {subsidio_transporte:.2f}\n"
            f"Valor de días festivos: {valor_días_festivos:.2f}\n"
            f"Valor de horas extra diurnas: {valor_horas_extra_diurnas:.2f}\n"
            f"Valor de horas extra nocturnas: {valor_horas_extra_nocturnas:.2f}\n"
            f"Valor de horas extra festivas: {valor_horas_extra_festivas:.2f}\n"
            f"Valor de incapacidades: {valor_incapacidades:.2f}\n"
            f"Valor de licencias no remuneradas: {valor_licencias_no_remuneradas:.2f}\n"
            f"Aporte a salud: {valor_aporte_a_salud:.2f}\n"
            f"Aporte a pensión: {valor_aporte_a_pension:.2f}\n"
            f"Fondo de solidaridad pensional: {valor_fondo_solidaridad_pensional:.2f}\n"
            f"Total neto a pagar: {total_neto:.2f}"
        )

class NominaApp(App):
    def build(self):
        sm = ScreenManager()
        main_screen = MainScreen(name="main")
        sm.add_widget(main_screen)
        return sm

if __name__ == "__main__":
    NominaApp().run()

