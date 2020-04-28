# -*- coding: utf-8 -*-
import os, sys
from os.path import abspath, dirname
# import sqlite3
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivymd.theming import ThemeManager
from kivymd.snackbar import Snackbar
from uix.hfutcommunityconf import HfutCommunityConfScreenManager

# 引入资源目录
from kivy.resources import resource_add_path, resource_find
resource_add_path(os.path.abspath('./data/fonts'))
# 替换kivy中的默认字体，使用我们的新字体
from kivy.core.text import LabelBase
LabelBase.register('Roboto', 'DroidSansFallback.ttf')

# This allows you to use a custom data dir for kivy allowing you to
# load only the images that you set here in this dir.
# This way you avoid first loading kivy default images and .kv then
# loading your data files on top.
os.environ['KIVY_DATA_DIR'] = abspath(dirname(__file__)) + '/data'

script_path = os.path.dirname(os.path.realpath(__file__))

# add module path for screen so they can be dnamically be imported
module_path = script_path + '/uix/screens/'
sys.path.insert(0, module_path)


class HfutCommunity(App):
    theme_cls = ThemeManager()
    title = StringProperty('HFUT')
    # icon = StringProperty('./pic/logo.png')

    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.exit_flag = False
        self.icon = 'pic/logo.png'
        # self.conn = sqlite3.connect('./data/sql/userdata.db')
        # self.cursor = self.conn.cursor()

        # this is the main entry point of the app
        sm = HfutCommunityConfScreenManager()
        # This `sm` is the root widget of the app refered by app.root
        Window.bind(on_keyboard=self.android_back_click)
        return sm

    def on_start(self):
        # self.alldata = self.cursor.execute("select * from user").fetchall()
        # print(self.alldata)
        print("App on_start, Load MainScreen")
        self.load_screen('MainScreen')

    def on_pause(self):
        return True

    def on_stop(self):
        pass

    def load_screen(self, screen, manager=None, store_back=True, direction='left'):

        store_back = False if screen == 'StartupScreen' else store_back

        manager = manager or self.root
        # load screen modules dynamically
        # for example load_screen('LoginScreen')
        # will look for uix/screens/loginscreen
        # load LoginScreen
        module_path = screen.lower()
        if not hasattr(self, module_path):
            import imp
            module = imp.load_module(screen, *imp.find_module(module_path))
            print(module)
            screen_class = getattr(module, screen)
            print(screen_class)
            sc = screen_class()
            sc.from_back = not store_back
            setattr(self, module_path, sc)
            manager.add_widget(sc)

        else:
            sc = getattr(self, module_path)

        sc.from_back = not store_back
        manager = manager or self.root
        print(screen)
        # load screen modules dynamically
        # for example load_screen('LoginScreen') will look for uix/screens/loginscreen to load LoginScreen
        manager.transition.direction = direction
        manager.current = screen
        return getattr(self, module_path)

    def android_back_click(self, window, key, *largs):
        if key == 27:
            if not self.exit_flag:
                if self.root.current == 'MainScreen':
                    Snackbar(text="再按一次退出").show()
                    self.exit_flag = True
                    Clock.schedule_once(lambda x: self.clear_exit_flag(), 2)
                    return True
                else:
                    self.load_screen('MainScreen')
                    return True
            else:
                print("exit")
                self.stop()

    def clear_exit_flag(self):
        self.exit_flag = False


if __name__ == '__main__':
    global hfutcommunity
    hfutcommunity = HfutCommunity()
    hfutcommunity.run()
