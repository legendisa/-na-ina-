from kivy.app import App
from kivy.uix.button import Button
from kivy.utils import platform

class InaApp(App):
    def build(self):
        return Button(text="Ses sistemi henüz aktif değil", on_release=self.test_basit)

    def test_basit(self, instance):
        if platform == 'android':
            # Burada TTS kodları gelecek, şu an sadece test ediyoruz
            instance.text = "Android tespit edildi!"
        else:
            instance.text = "Bilgisayardasın, TTS çalışmaz."

if __name__ == '__main__':
    InaApp().run()
