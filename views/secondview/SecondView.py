from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('views\secondview\SecondView.kv')

class SecondView(Screen,BoxLayout):
   def __init__(self, **kwargs):
       super().__init__(**kwargs)  