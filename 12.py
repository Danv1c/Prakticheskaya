from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.backdrop import MDBackdrop
from kivymd.uix.button import MDRaisedButton, MDTextButton

KV = '''
MDBackdrop:
    id: backdrop
    header_text: "MDBackDrop Example"

    MDBackdropFrontLayer:
        MDBoxLayout:
            orientation: 'vertical'
            padding: dp(20)
            spacing: dp(10)

            MDRaisedButton:
                text: "Raised Button"
                pos_hint: {"center_x": 0.5}
                on_release: app.on_raised_button()

            MDTextButton:
                text: "Text Button"
                pos_hint: {"center_x": 0.5}
                on_release: app.on_text_button()

    MDBackdropBackLayer:
        MDBoxLayout:
            orientation: 'vertical'
            MDLabel:
                text: "Back Layer"
                halign: "center"
'''


class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_raised_button(self):
        print("Raised Button Pressed")

    def on_text_button(self):
        print("Text Button Pressed")


MyApp().run()