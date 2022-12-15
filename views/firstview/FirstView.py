from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('views/firstView/FirstView.kv')

class FirstView(BoxLayout):
    def get_file(self):
        print("button clicked") 
       
 
