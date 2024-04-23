from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class ResultPopup(Popup):
    def __init__(self, **kwargs):
        super(ResultPopup, self).__init__(**kwargs)
        self.title = 'Resultado'
        self.size_hint = (None, None)
        self.size = (400, 400)

        self.layout = BoxLayout(orientation='vertical')
        self.content = self.layout

        self.resultado_label = Label()
        self.layout.add_widget(self.resultado_label)

        self.cerrar_btn = Button(text='Cerrar', size_hint=(1, 0.2))
        self.cerrar_btn.bind(on_press=self.dismiss)
        self.layout.add_widget(self.cerrar_btn)

    def mostrar_resultado(self, resultado):
        self.resultado_label.text = "Resultado: " + str(resultado)
        self.open()

    def mostrar_error(self, campos_erroneos):
        self.resultado_label.text = "Por favor, introduce números válidos en los siguientes campos: " + ", ".join(campos_erroneos)
        self.open()
