import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from liquidador_nomina import *

class NominaApp(App):
    def build(self):
        self.main_layout = BoxLayout(orientation="vertical")

        # Salario base mensual
        self.main_layout.add_widget(Label(text="Salario base mensual"))
        self.salario_input = TextInput(multiline=False)
        self.main_layout.add_widget(self.salario_input)

        # Tiempo laborado
        self.main_layout.add_widget(Label(text="Tiempo laborado al mes en horas"))
        self.tiempo_laborado_input = TextInput(multiline=False)
        self.main_layout.add_widget(self.tiempo_laborado_input)

        # Tiempo festivo laborado
        self.main_layout.add_widget(Label(text="Tiempo festivo laborado en días"))
        self.tiempo_festivo_laborado_input = TextInput(multiline=False)
        self.main_layout.add_widget(self.tiempo_festivo_laborado_input)

        # Horas extra diurnas
        self.main_layout.add_widget(Label(text="Horas extras diurnas laboradas"))
        self.horas_extra_diurnas_input = TextInput(multiline=False)
        self.main_layout.add_widget(self.horas_extra_diurnas_input)

        # Horas extra nocturnas
        self.main_layout.add_widget(Label(text="Horas extras nocturnas laboradas"))
        self.horas_extra_nocturnas_input = TextInput(multiline=False)
        self.main_layout.add_widget(self.horas_extra_nocturnas_input)

        # Horas extra festivos
        self.main_layout.add_widget(Label(text="Horas extras festivas laboradas"))
        self.horas_extra_festivos_input = TextInput(multiline=False)
        self.main_layout.add_widget(self.horas_extra_festivos_input)

        # Tiempo de incapacidades
        self.main_layout.add_widget(Label(text="Tiempo de incapacidades en días"))
        self.tiempo_incapacidades_input = TextInput(multiline=False)
        self.main_layout.add_widget(self.tiempo_incapacidades_input)

        # Tiempo de licencias no remuneradas
        self.main_layout.add_widget(Label(text="Tiempo de licencias no remuneradas en días"))
        self.tiempo_licencias_no_remuneradas_input = TextInput(multiline=False)
        self.main_layout.add_widget(self.tiempo_licencias_no_remuneradas_input)

        # Botón para calcular la nómina
        self.calcular_button = Button(text="Calcular liquidación de nómina")
        self.calcular_button.bind(on_press=self.calcular_nomina)
        self.main_layout.add_widget(self.calcular_button)

                # Etiqueta para mostrar los resultados
        self.resultado_label = Label(text="", size_hint_y=None)
        self.resultado_label.bind(width=lambda s, w: setattr(s, 'text_size', (w, None)), texture_size=lambda s, ts:setattr(s, 'height', ts[1]))

        scroll_view = ScrollView()
        scroll_view.add_widget(self.resultado_label)
        self.main_layout.add_widget(scroll_view)

        return self.main_layout


    def calcular_nomina(self, instance):
        # Recuperar los datos de entrada de los widgets
        salario_base_mensual = float(self.salario_input.text)
        tiempo_laborado = float(self.tiempo_laborado_input.text)
        tiempo_festivo_laborado = float(self.tiempo_festivo_laborado_input.text)
        horas_extra_diurnas = float(self.horas_extra_diurnas_input.text)
        horas_extra_nocturnas = float(self.horas_extra_nocturnas_input.text)
        horas_extra_festivos = float(self.horas_extra_festivos_input.text)
        tiempo_incapacidades = float(self.tiempo_incapacidades_input.text)
        tiempo_licencias_no_remuneradas = float(self.tiempo_licencias_no_remuneradas_input.text)

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

        total_ingresos = valor_salario + subsidio_transporte + valor_dias_festivos + valor_hora_extra_diurna + valor_hora_extra_nocturna + valor_hora_extra_festivo + valor_incapacidad
        total_deducciones = valor_licencia_no_remunerada + valor_aporte_a_salud + valor_aporte_a_pension + valor_fondo_solidaridad_pensional
        total_neto = total_ingresos - total_deducciones

        # Mostrar información en pantalla
        self.resultado_label.text = f"Salario: {valor_salario}\nSubsidio de transporte: {subsidio_transporte}\nValor días festivos: {valor_dias_festivos}\nValor horas extras diurnas: {valor_hora_extra_diurna}\nValor horas extras nocturnas: {valor_hora_extra_nocturna}\nValor horas extras festivas: {valor_hora_extra_festivo}\nValor de incapacidades: {valor_incapacidad}\nValor de licencia no remunerada: {valor_licencia_no_remunerada}\nValor aporte a salud: {valor_aporte_a_salud}\nValor aporte a pensión: {valor_aporte_a_pension}\nValor al fondo de solidaridad pensional: {valor_fondo_solidaridad_pensional}\nTotal a pagar/neto: {total_neto}"

if __name__ == "__main__":
    NominaApp().run()