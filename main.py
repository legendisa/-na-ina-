from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from jnius import autoclass
from kivy.utils import platform
from kivy.core.window import Window

class InaApp(App):
    def build(self):
        # Ana Layout (Arka Plan Rengi Ekleme)
        self.root = BoxLayout(orientation='vertical', padding=40, spacing=30)
        
        with self.root.canvas.before:
            Color(0.95, 0.95, 1, 1) # Açık Lavanta/Beyaz arka plan
            self.rect = Rectangle(size=(2000, 2000), pos=self.root.pos)
        
        # Başlık - İNA
        self.header = Label(
            text="İNA", 
            font_size='60sp', 
            color=(0.4, 0.2, 0.7, 1), # Mor renk
            bold=True,
            size_hint=(1, 0.2)
        )
        
        # Durum Yazısı
        self.status_label = Label(
            text="Merhaba! Senin için ne yapabilirim?",
            font_size='20sp',
            color=(0.2, 0.2, 0.2, 1),
            halign='center',
            valign='middle'
        )
        self.status_label.bind(size=self.status_label.setter('text_size'))

        # Konuştur Butonu (Modern Renkler)
        btn = Button(
            text="KONUŞTUR",
            size_hint=(1, 0.15),
            background_normal='',
            background_color=(0.5, 0.3, 0.9, 1), # Canlı Mor
            color=(1, 1, 1, 1),
            bold=True
        )
        btn.bind(on_release=self.konus)

        # Widget'ları ekle
        self.root.add_widget(self.header)
        self.root.add_widget(self.status_label)
        self.root.add_widget(btn)
        
        return self.root

    def konus(self, instance):
        self.status_label.text = "İna seninle konuşuyor..."
        
        if platform == 'android':
            try:
                PythonActivity = autoclass('org.kivy.android.PythonActivity')
                TextToSpeech = autoclass('android.speech.tts.TextToSpeech')
                Locale = autoclass('java.util.Locale')
                
                # Türkçe Locale oluştur
                tr_locale = Locale("tr", "TR")
                
                # TTS motorunu başlat ve Türkçe yap
                tts = TextToSpeech(PythonActivity.mActivity, None)
                tts.setLanguage(tr_locale)
                
                mesaj = "Merhaba! Ben İna. Senin için buradayım. Modern arayüzüm nasıl görünüyor?"
                tts.speak(mesaj, TextToSpeech.QUEUE_FLUSH, None)
            except Exception as e:
                self.status_label.text = f"Hata: {str(e)}"
        else:
            self.status_label.text = "Sadece Android üzerinde Türkçe konuşabilirim."

if __name__ == '__main__':
    InaApp().run()
