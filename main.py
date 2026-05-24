from kivy.app import App
from kivy.uix.label import Label

class InaApp(App):
    def build(self):
        return Label(text="İna sistemi hazır. APK başarıyla derlendi.")

if __name__ == '__main__':
    InaApp().run()
