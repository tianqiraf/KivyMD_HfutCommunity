# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

from kivymd.bottomsheet import MDListBottomSheet, MDGridBottomSheet
from kivymd.button import MDIconButton
from kivymd.date_picker import MDDatePicker
from kivymd.dialog import MDDialog
from kivymd.textfields import MDTextField
from kivymd.label import MDLabel
from kivymd.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch, BaseListItem
from kivymd.material_resources import DEVICE_TYPE
from kivymd.navigationdrawer import MDNavigationDrawer, NavigationDrawerHeaderBase
from kivymd.selectioncontrols import MDCheckbox
from kivymd.snackbar import Snackbar
from kivymd.theming import ThemeManager
from kivymd.time_picker import MDTimePicker
from kivymd.menu import MDDropdownMenu

my_info_kv = '''
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
#:import Snackbar kivymd.snackbar.Snackbar
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

<MyInfoScreen>:
    id: myinfoscreen
    name: 'MyInfoScreen'
    padding: dp(10)
    BoxLayout:
        orientation: 'vertical'
        Toolbar:
            title: "我的信息"
            pos_hint: {'center_x': 0.5, 'center_y': 0.25}
            md_bg_color: app.theme_cls.primary_color
            left_action_items: [['arrow-left', lambda x: app.load_screen('MainScreen', direction='right')]]
        NavigationDrawerDivider:
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
                    height: self.minimum_height
                    canvas:
                        Color:
                            rgb: app.theme_cls.primary_color
                        Rectangle:
                            pos: self.pos
                            size: self.size
                    ImageButton:
                        id: head_img
                        mipmap: True
                        pos_hint: {'center_x': 0.5}
                        size_hint: None, None
                        size: 108, 108
                        source: 'pic/account.png'
                        on_press: Snackbar(text="暂不支持修改头像~").show()
                    MDLabel:
                        height: 64
                        halign: 'center'
                        text: '请登录'
                        font_style: 'Body1'
                        theme_text_color: 'Primary'
                    MDLabel:
                        height: 64
                        halign: 'center'
                        text: '性别 校区 专业'
                        font_style: 'Body1'
                        theme_text_color: 'Primary'
                BoxLayout:
                    orientation: 'vertical'
                    spacing: 10
                    size_hint: 1, None
                    height: self.minimum_height
                    MDList:    
                        NavigationDrawerDivider:
                        NavigationDrawerButton:
                            text: "信息门户"
                            badge_text: "未绑定"
                            on_release: root.bind_dialog(0)
                        NavigationDrawerButton:
                            text: "教务系统"
                            badge_text: "未绑定"
                            on_release: root.bind_dialog(1)
                        NavigationDrawerDivider:
                        NavigationDrawerDivider:
                        NavigationDrawerButton:
                            text: "学号"
                            badge_text: "无"
                            on_release: 
                        NavigationDrawerButton:
                            text: "学院"
                            badge_text: "无"
                            on_release: 
                        NavigationDrawerButton:
                            text: "专业"
                            badge_text: "无"
                            on_release: 
                        NavigationDrawerRightIconButton:
                            text: "邮箱"
                            badge_text: "tianqiraf@mail.hfut.edu.cn"
                            icon: "chevron-right"
                            on_release: root.bind_email_dialog()
                        #NavigationDrawerRightIconButton:
                        #    text: "修改密码"
                        #    icon: "chevron-right"
                        #    on_release: root.change_password_dialog()
                        NavigationDrawerDivider:          
'''


class MyInfoScreen(Screen):
    Builder.load_string(my_info_kv)

    def bind_dialog(self, bind_type):           # bind_type: 0-->信息门户， 1-->教务系统
        self.content = MDTextField()
        self.content.hint_text = "密码"
        # content.password = True
        self.dialog = MDDialog(title="绑定信息门户" if bind_type == 0 else "绑定教务系统",
                               content=self.content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=True)

        self.dialog.add_action_button("绑定", action=lambda *x: self.bind_infoport() if bind_type == 0 else self.bind_edusys())
        self.dialog.add_action_button("取消", action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    def bind_email_dialog(self):
        self.content = MDTextField()
        self.content.hint_text = "邮箱"
        # content.password = True
        self.dialog = MDDialog(title="修改邮箱",
                               content=self.content,
                               size_hint=(.8, None),
                               height=dp(200),
                               auto_dismiss=True)

        self.dialog.add_action_button("确定", action=lambda *x: self.bind_email())
        self.dialog.add_action_button("取消", action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    def change_password_dialog(self):
        Snackbar(text="请登录教务系统修改密码!").show()
        '''
        self.content = BoxLayout()
        self.content.size_hint_y = None
        self.content.height = self.content.minimum_height
        self.content_old_pass = MDTextField()
        self.content_old_pass.hint_text = "原密码"
        self.content_new_pass = MDTextField()
        self.content_new_pass.hint_text = "新密码"

        # self.content.add_widget()
        self.content.add_widget(self.content_new_pass)
        print(self.content.children)
        # content.password = True
        self.dialog = MDDialog(title="修改密码",
                               content=self.content,
                               size_hint=(.8, None),
                               height=dp(600),
                               auto_dismiss=True)

        self.dialog.add_action_button("确定", action=lambda *x: self.change_password())
        self.dialog.add_action_button("取消", action=lambda *x: self.dialog.dismiss())
        self.dialog.open()
        '''

    def bind_infoport(self):
        if self.content.text == '':
            Snackbar(text="密码不能为空!").show()
        else:
            self.dialog.dismiss()

    def bind_edusys(self):
        if self.content.text == "":
            Snackbar(text="密码不能为空!").show()
        else:
            self.dialog.dismiss()

    def bind_email(self):
        if "@" not in self.content.text:
            Snackbar(text="邮箱格式不正确!").show()
        else:
            self.dialog.dismiss()

    def change_password(self):
        if self.content_new_pass.text == "" or self.content_old_pass == "":
            Snackbar(text="密码不能为空!").show()
        else:
            self.dialog.dismiss()


class ImageButton(ButtonBehavior, Image):
    pass
