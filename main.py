from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyApp(App):
    def built(self):
        l1=Label(text="Hello Click")
        b=Button(text="Click")

        return b

MyApp().run()
