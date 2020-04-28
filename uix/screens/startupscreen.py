'''Startup screen
'''

from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


class StartupScreen(Screen):
    '''
    '''
    Builder.load_string('''

<StartupScreen>
    name: 'StartupScreen'
    on_enter:
        print("StartupScreen on_enter")
        from kivy.animation import Animation

        Animation(d=.1, top=self.height, height=self.height/2., width = self.width, opacity=1).start(label_logo)
        from kivy.clock import Clock
        # Clock.schedule_once(lambda dt: app.load_screen('MainScreen'), 1.75)
    canvas.before:
        Color:
            rgba: (0, 0, 0, 1)
        Rectangle:
            size: self.size
            pos: self.pos
    MDLabel:
        id: label_logo
        font_style: 'Headline'
        theme_text_color: 'Custom'
        text_color: (1,1,1,1)
        text: "HFUT Community"
        halign: 'center'
        
''')
    