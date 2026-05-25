from kivy.app import App
from kivy.uix.button import Button
from jnius import autoclass

# Android TTS sınıflarını çağır
PythonActivity = autoclass('org.kivy.android.PythonActivity')
TextToSpeech = autoclass('android.speech.tts.TextToSpeech')
Locale = autoclass('java.util.Locale')

class InaApp(App):
    def build(self):
        # Ses motorunu başlat
        self.tts = TextToSpeech(PythonActivity.mActivity, None)
        self.tts.setLanguage(Locale.TR) # Türkçe dil ayarı
        
        btn = Button(text="Konuştur")
        btn.bind(on_release=self.konus)
        return btn

    def konus(self, instance):
        metin = "Sisteme başarıyla entegre edildim. Artık seninle konuşabiliyorum."
        self.tts.speak(metin, TextToSpeech.QUEUE_FLUSH, None)

if __name__ == '__main__':
    InaApp().run()
