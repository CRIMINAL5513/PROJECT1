from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
Window.clearcolor = (100/255.0,10/255.0,1,1)
Window.size = (400,600)
class CRIMINAL(App):
    def build(self):
        self.title = 'CRIMINAL APP'
        return Builder.load_file('kv.kv')
if __name__ == '__main__':
    CRIMINAL().run()