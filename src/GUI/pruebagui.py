from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from PopupResult import ResultPopup

class MiApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.campos = []
        self.nombres = ["Salario base mensual:", "Tiempo laborado al mes (horas):", "Tiempo festivo laborado (días):", "Licencias no remuneradas (días):", "Horas extras diurnas laboradas:", "Horas extras nocturnas laboradas:", "Horas extras festivas laboradas:", "Incapacidades (días):"]
        for nombre in self.nombres:
            campo = TextInput(hint_text=nombre)
            self.campos.append(campo)
            layout.add_widget(campo)

        btn_calcular = Button(text="Calcular")
        btn_calcular.bind(on_press=self.calcular)
        layout.add_widget(btn_calcular)

        btn_limpiar = Button(text="Limpiar")
        btn_limpiar.bind(on_press=self.limpiar)
        layout.add_widget(btn_limpiar)

        self.popup = ResultPopup()

        return layout

    def calcular(self, instance):
        try:
            total = sum(float(campo.text) for campo in self.campos)
            self.popup.mostrar_resultado(total)
        except ValueError:
            campos_erroneos = [self.nombres[i] for i, campo in enumerate(self.campos) if not self.es_numero(campo.text)]
            self.popup.mostrar_error(campos_erroneos)

    def limpiar(self, instance):
        for campo in self.campos:
            campo.text = ""

    def es_numero(self, texto):
        try:
            float(texto)
            return True
        except ValueError:
            return False

if __name__ == "__main__":
    MiApp().run()
