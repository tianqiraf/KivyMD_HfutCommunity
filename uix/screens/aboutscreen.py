# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window

from kivymd.bottomsheet import MDListBottomSheet, MDGridBottomSheet
from kivymd.button import MDIconButton
from kivymd.date_picker import MDDatePicker
from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivymd.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch, BaseListItem
from kivymd.material_resources import DEVICE_TYPE
from kivymd.navigationdrawer import MDNavigationDrawer, NavigationDrawerHeaderBase
from kivymd.selectioncontrols import MDCheckbox
from kivymd.snackbar import Snackbar
from kivymd.theming import ThemeManager
from kivymd.time_picker import MDTimePicker
from kivymd.menu import MDDropdownMenu

about_kv = '''
#:import Toolbar kivymd.toolbar.Toolbar
#:import ThemeManager kivymd.theming.ThemeManager
#:import MDNavigationDrawer kivymd.navigationdrawer.MDNavigationDrawer
#:import NavigationLayout kivymd.navigationdrawer.NavigationLayout
#:import NavigationDrawerDivider kivymd.navigationdrawer.NavigationDrawerDivider
#:import NavigationDrawerToolbar kivymd.navigationdrawer.NavigationDrawerToolbar
#:import NavigationDrawerSubheader kivymd.navigationdrawer.NavigationDrawerSubheader
#:import MDCheckbox kivymd.selectioncontrols.MDCheckbox
#:import MDSwitch kivymd.selectioncontrols.MDSwitch
#:import MDList kivymd.list.MDList
#:import OneLineListItem kivymd.list.OneLineListItem
#:import TwoLineListItem kivymd.list.TwoLineListItem
#:import ThreeLineListItem kivymd.list.ThreeLineListItem
#:import OneLineAvatarListItem kivymd.list.OneLineAvatarListItem
#:import OneLineIconListItem kivymd.list.OneLineIconListItem
#:import OneLineAvatarIconListItem kivymd.list.OneLineAvatarIconListItem
#:import MDTextField kivymd.textfields.MDTextField
#:import MDSpinner kivymd.spinner.MDSpinner
#:import MDCard kivymd.card.MDCard
#:import MDSeparator kivymd.card.MDSeparator
#:import MDDropdownMenu kivymd.menu.MDDropdownMenu
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import colors kivymd.color_definitions.colors
#:import SmartTile kivymd.grid.SmartTile
#:import MDSlider kivymd.slider.MDSlider
#:import MDTabbedPanel kivymd.tabs.MDTabbedPanel
#:import MDTab kivymd.tabs.MDTab
#:import MDProgressBar kivymd.progressbar.MDProgressBar
#:import MDAccordion kivymd.accordion.MDAccordion
#:import MDAccordionItem kivymd.accordion.MDAccordionItem
#:import MDAccordionSubItem kivymd.accordion.MDAccordionSubItem
#:import MDThemePicker kivymd.theme_picker.MDThemePicker
#:import MDBottomNavigation kivymd.tabs.MDBottomNavigation
#:import MDBottomNavigationItem kivymd.tabs.MDBottomNavigationItem

<AboutScreen>:
    id: aboutscreen
    name: 'AboutScreen'
    padding: dp(10)
    BoxLayout:
        orientation: 'vertical'
        Toolbar:
            title: "关于"
            pos_hint: {'center_x': 0.5, 'center_y': 0.25}
            md_bg_color: app.theme_cls.primary_color
            left_action_items: [['arrow-left', lambda x: app.load_screen('MainScreen', direction='right')]]
        ScrollView:
            BoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                padding: dp(10)
                spacing: 10
                BoxLayout:
                    orientation: 'vertical'
                    padding: dp(24)
                    spacing: 24
                    size_hint: 1, None
                    height: self.minimum_height + dp(64)
                    MDLabel:
                        height: 72
                        halign: 'center'
                        text: 'HFUT Community'
                        font_style: 'Headline'
                        theme_text_color: 'Primary'
                    MDLabel:
                        height: 36
                        halign: 'center'
                        text: 'V1.0.0'
                        font_style: 'Body1'
                        theme_text_color: 'Primary'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: 10
                    size_hint: 1, None
                    height: self.minimum_height
                    MDList:    
                        NavigationDrawerDivider:
                        OneLineRightWidgetListItem:
                            text: "自动检查更新"
                            on_release: print(root.ids['auto_update'].active)
                            RightSampleWidget:
                                id: auto_update
                                active: True
                        OneLineRightWidgetListItem:
                            text: "更新日志"
                            on_release: app.load_screen('UpdateLogScreen')
                            IconRightSampleWidget:
                                id: go_to_icon
                                icon: "chevron-right"
                        OneLineRightWidgetListItem:
                            text: "帮助"
                            on_release: app.load_screen('HelpScreen')
                            IconRightSampleWidget:
                                id: go_to_icon
                                icon: "chevron-right"
                        OneLineRightWidgetListItem:
                            text: "吐槽与反馈"
                            on_release: app.load_screen('FeedbackScreen')
                            IconRightSampleWidget:
                                id: go_to_icon
                                icon: "chevron-right"
                        OneLineRightWidgetListItem:
                            text: "关于我"
                            on_release: app.load_screen('AboutMeScreen')
                            IconRightSampleWidget:
                                id: go_to_icon
                                icon: "chevron-right"
                                
                            
'''


class AboutScreen(Screen):

    Builder.load_string(about_kv)
