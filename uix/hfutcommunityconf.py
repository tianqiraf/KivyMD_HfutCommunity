'''uix.hfutcommunityconf module which should house all common widgets.
'''

from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder


class HfutCommunityConfScreenManager(ScreenManager):
    Builder.load_string('''
#:import SlideTransition kivy.uix.screenmanager.SlideTransition

<HfutCommunityConfScreenManager>
    transition: SlideTransition(duration=.3)
    
''')