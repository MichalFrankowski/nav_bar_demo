from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ToggleButtonBehavior,ButtonBehavior
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.properties import ListProperty
#allowing to add custom fonts
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty

#first set execution policy
#Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force
#RUN kivy_venv\Scripts\activate.ps1 TO ACTIVATE VIRTUAL ENV 

#main view of the app
class navbardemo(BoxLayout,Screen):
    manager = ObjectProperty(None) 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  
       
    def get_file(self):
        print("button clicked") 

class ScreenManager(ScreenManager):
    pass

class FirstView(Screen):
    pass

class SecondView(Screen):
    pass

#custom navtab buttons
class NavTab(ToggleButtonBehavior, BoxLayout):
    text = StringProperty("")
    #background for hover 
    background = ListProperty((23/255, 23/255, 23/255,1))
    def __init__(self, **kw):
        super().__init__(**kw) 
        #finding mouse position for a hover animation
        Window.bind(mouse_pos=self.on_motion)
        
    #preventing the navtab button from being unclick     
    def staydown_callback(self, btn, *args):
        setattr(btn, 'state', 'down')    
    
    #hover animation for nav buttons
    def on_motion(self, src, mouse_pos):
        if self.collide_point(*mouse_pos):
            #print('over Button at', mouse_pos, 'Do animation')
            self.background= (10/255, 65/255, 112/255,1)
        else:   
            self.background= (23/255, 23/255, 23/255,1) 
  
#custom tex label
class Text(Label):
    def __init__(self, **kw):
        super().__init__(**kw)        

class navbardemoApp(App):
    def build(self):
        return navbardemo()
   
    #custom font - CURRENTLY NOT USE AS USING STANDARD STYLE "VERDANA"
    LabelBase.register(name='Roboto-Black',
                   fn_regular='assets/fonts/Roboto/Roboto-Bold.ttf')
            
if __name__ == '__main__':
    navbardemoApp().run()
    
      