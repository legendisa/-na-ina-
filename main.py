from kivy.app import App
from kivy.uix.button import Button
from jnius import autoclass
from kivy.utils import platform

# Android sınıflarını güvenli bir şekilde çağır
if platform == 'android':
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    TextToSpeech = autoclass('android.speech.tts.TextToSpeech')
    Locale = autoclass('java.util.Locale')

class InaApp(App):
    def build(self):
        return Button(text="Konuş!", on_release=self.konus)

    def konus(self, instance):
        if platform == 'android':
            # Android TTS motorunu başlat
            tts = TextToSpeech(PythonActivity.mActivity, None)
            tts.setLanguage(Locale.US) # Şimdilik İngilizce test
            tts.speak("I am ready.", TextToSpeech.QUEUE_FLUSH, None)
        else:
            instance.text = "Sadece Android'de çalışırım!"

if __name__ == '__main__':
    InaApp().run()
