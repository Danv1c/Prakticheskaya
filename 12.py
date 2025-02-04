from kivy.lang import Builder
from kivymd.app import MDApp  # Импортируем MDApp
from kivymd.uix.backdrop import MDBackdrop
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDRaisedButton, MDTextButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.image import Image

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
            padding: dp(10)
            spacing: dp(10)

            MDCard:
                orientation: 'vertical'
                size_hint: (1, None)
                height: dp(200)

                MDLabel:
                    text: "Card 1"
                    halign: "center"
                    font_style: "H6"

                Image:
                    source: 'path_to_image_1.jpg'  # Укажите путь к изображению
                    size_hint_y: 0.7

                MDRaisedButton:
                    text: "Button 1"
                    pos_hint: {"center_x": 0.5}

            MDCard:
                orientation: 'vertical'
                size_hint: (1, None)
                height: dp(200)

                MDLabel:
                    text: "Card 2"
                    halign: "center"
                    font_style: "H6"

                Image:
                    source: 'path_to_image_2.jpg'  # Укажите путь к изображению
                    size_hint_y: 0.7

                MDRaisedButton:
                    text: "Button 2"
                    pos_hint: {"center_x": 0.5}

            MDCard:
                orientation: 'vertical'
                size_hint: (1, None)
                height: dp(200)

                MDLabel:
                    text: "Card 3"
                    halign: "center"
                    font_style: "H6"

                Image:
                    source: 'path_to_image_3.jpg'  # Укажите путь к изображению
                    size_hint_y: 0.7

                MDRaisedButton:
                    text: "Button 3"
                    pos_hint: {"center_x": 0.5}
'''

class MyApp(MDApp):  # Наследуемся от MDApp
    def build(self):
        return Builder.load_string(KV)

    def on_raised_button(self):
        print("Raised Button Pressed")

    def on_text_button(self):
        print("Text Button Pressed")

MyApp().run()
