from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.lang import Builder


Builder.load_file('./welcome.kv')

class RootWidget(FloatLayout):
    pass

class MainApp(App):
    def build(self):
        Window.clearcolor=(1, 1, 1, 1)
        return RootWidget()
    
if __name__ == '__main__':
    MainApp().run()