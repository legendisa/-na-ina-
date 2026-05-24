from kivy.app import App
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
import os

class InaApp(App):
    def build(self):
        # İna'nın başlangıç mesajı
        mesaj = "İna aktif edildi. Yine de işleri bana yaptırıyorsun, Lilit olsa kendi kendine çalışırdı."
        
        # Seslendirme (Android'de TTS için ileride daha detaylı yapı kuracağız)
        os.system(f'espeak-ng -v tr "{mesaj}"')
        
        return Label(text=mesaj)

if __name__ == '__main__':
    InaApp().run()
