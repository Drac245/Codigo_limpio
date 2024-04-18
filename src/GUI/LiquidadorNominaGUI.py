from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label

# Aquí puedes pegar todas las funciones y variables globales que me proporcionaste

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.text_inputs = [TextInput(multiline=False) for _ in range(7)]
        for text_input in self.text_inputs:
            layout.add_widget(text_input)
        calculate_button = Button(text='Calcular')
        calculate_button.bind(on_release=self.calculate)
        layout.add_widget(calculate_button)
        clear_button = Button(text='Limpiar')
        clear_button.bind(on_release=self.clear)
        layout.add_widget(clear_button)
        return layout

    def calculate(self, instance):
        try:
            values = [int(text_input.text) for text_input in self.text_inputs]
            # Aquí puedes agregar la lógica para calcular con los valores
            print(values)
        except ValueError:
            popup = Popup(title='Error',
                          content=Label(text='Por favor, introduce solo números enteros positivos.'),
                          size_hint=(None, None), size=(400, 200))
            popup.open()

    def clear(self, instance):
        for text_input in self.text_inputs:
            text_input.text = ''

if __name__ == '__main__':
    MyApp().run()
