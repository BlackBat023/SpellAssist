import speech_recognition as sr
from kivy.lang import Builder
from kivymd.app import MDApp


class SpellAssist(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_file('spell.kv')

    def input(self):
        voice = sr.Recognizer()
        with sr.Microphone() as source:
            voice.adjust_for_ambient_noise(source, duration=1)
            audio = voice.listen(source)

        try:
            result = voice.recognize_google(audio).capitalize()
            self.root.ids.spell_Label.text = result
            # print(sr.__version__)
        except LookupError:
            print("Could not understand audio")


SpellAssist().run()
