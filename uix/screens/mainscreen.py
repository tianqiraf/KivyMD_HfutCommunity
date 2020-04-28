# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window
from kivy.clock import Clock
from kivymd.navigationdrawer import NavigationDrawerSubheader
from kivymd.bottomsheet import MDBottomSheet, MDListBottomSheet, MDGridBottomSheet
from kivymd.button import MDIconButton, MDScreenWidthFlatButton
from kivymd.date_picker import MDDatePicker
from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivymd.list import ILeftBody, ILeftBodyTouch, IRightBody, IRightBodyTouch, BaseListItem, MDList
from kivymd.list import OneLineListItem, TwoLineListItem
from kivymd.material_resources import DEVICE_TYPE
from kivymd.slider import MDSlider
from kivymd.navigationdrawer import MDNavigationDrawer, NavigationDrawerHeaderBase
from kivymd.selectioncontrols import MDCheckbox
from kivymd.snackbar import Snackbar
from kivymd.theming import ThemeManager
from kivymd.time_picker import MDTimePicker
from kivymd.menu import MDDropdownMenu

from utils import get_json
main_widget_kv = '''
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
#:import MDThemePicker kivymd.theme_picker.MDThemePicker
#:import MDBottomNavigation kivymd.tabs.MDBottomNavigation
#:import MDBottomNavigationItem kivymd.tabs.MDBottomNavigationItem

<DotsMenuButton@MDFlatButton>:
    on_release:
        app.load_screen(self.name + "Screen") if "My" in self.name else app.mainscreen.select_menu_item(self.name)
        self.parent.parent.parent.parent.dismiss() # Close the menu
        
<MainScreen>:
    id: mainscreen
    name: 'MainScreen'
    padding: dp(10)
    MDBottomNavigation:
        id: BottomNavigation
        MDBottomNavigationItem:
            name: 'course'
            text: "课程"
            icon: "book-open"
            BoxLayout:
                orientation: 'vertical'
                Toolbar:
                    id: toolbar
                    title: "课程(" + root.week[root.selected_week] + ")" \
                            if root.ids.course_tab_panel.ids.tab_manager.current != 'course_score' else "成绩"
                    md_bg_color: app.theme_cls.primary_color
                    background_palette: 'Primary'
                    background_hue: '500'
                    left_action_items: [['menu', lambda x: root.show_week_select()]] if self.title != "成绩" else ''
                    right_action_items: [['dots-vertical', lambda x: MDDropdownMenu(items=root.course_menu_items \
                                            if root.ids.course_tab_panel.ids.tab_manager.current != 'course_score' \
                                            else root.score_menu_items, width_mult=2.5).open(self) ]]
                MDTabbedPanel:
                    id: course_tab_panel
                    tab_display_mode:'text'
                    MDTab:
                        name: 'course_course'
                        text: "课表"
                        icon: "book-open"

                        GridLayout:
                            cols: 2
                            size_hint_x: 1
                            GridLayout:
                                rows: 13
                                size_hint_x: .05
                                MDScreenWidthFlatButton:
                                    text: ' '
                                    disabled: True
                                    size_hint: 1, 1
                                MDScreenWidthFlatButton:
                                    text: '1'
                                    size_hint: 1, 1
                                MDScreenWidthFlatButton:
                                    text: '2'
                                    disabled: True
                                    size_hint: 1, 1
                                MDScreenWidthFlatButton:
                                    text: '3'
                                    disabled: True
                                    size_hint: 1, 1
                                MDScreenWidthFlatButton:
                                    text: '4'
                                    disabled: True
                                    size_hint: 1, 1
                                MDScreenWidthFlatButton:
                                    text: '5'
                                    disabled: True
                                    size_hint: 1, 1
                                MDScreenWidthFlatButton:
                                    text: '6'
                                    disabled: True
                                    size_hint: 1, 1
                                MDScreenWidthFlatButton:
                                    text: '7'
                                    disabled: True
                                    size_hint: 1, 1
                                MDScreenWidthFlatButton:
                                    text: '8'
                                    disabled: True
                                    size_hint: 1, 1
                                MDScreenWidthFlatButton:
                                    text: '9'
                                    disabled: True
                                    size_hint: 1, 1
                                MDScreenWidthFlatButton:
                                    text: '10'
                                    disabled: True
                                    size_hint: 1, 1
                                MDScreenWidthFlatButton:
                                    text: '11'
                                    disabled: True
                                    size_hint: 1, 1
                                MDScreenWidthFlatButton:
                                    text: ''
                                    disabled: True
                                    size_hint: 1, 1
                            GridLayout:
                                rows: 2
                                size_hint_x: .9
                                GridLayout:
                                    cols: 7
                                    size_hint_y: 1/12
                                    MDScreenWidthFlatButton:
                                        text: '周一'
                                        size_hint: 1, 1
                                    MDScreenWidthFlatButton:
                                        text: '周二'
                                        size_hint: 1, 1
                                        disabled: True
                                    MDScreenWidthFlatButton:
                                        text: '周三'
                                        size_hint: 1, 1
                                        disabled: True
                                    MDScreenWidthFlatButton:
                                        text: '周四'
                                        size_hint: 1, 1
                                        disabled: True
                                    MDScreenWidthFlatButton:
                                        text: '周五'
                                        size_hint: 1, 1
                                        disabled: True
                                    MDScreenWidthFlatButton:
                                        text: '周六'
                                        size_hint: 1, 1
                                        disabled: True
                                    MDScreenWidthFlatButton:
                                        text: '周日'
                                        size_hint: 1, 1
                                        disabled: True
                                GridLayout:
                                    cols: 7
                                    id: weekdays
                                    GridLayout:
                                        id: weekday_1
                                        rows: 12
                                        #MDScreenWidthFlatButton:
                                        #    id: 1_1
                                        #    text: ''
                                        #    md_bg_color: (1, 1, 1, 0.12)
                                        #    height: self.parent.height
                                    GridLayout:
                                        id: weekday_2
                                        rows: 12
                                    GridLayout:
                                        id: weekday_3
                                        rows: 12
                                    GridLayout:
                                        id: weekday_4
                                        rows: 12
                                    GridLayout:
                                        id: weekday_5
                                        rows: 12
                                    GridLayout:
                                        id: weekday_6
                                        rows: 12
                                    GridLayout:
                                        id: weekday_7
                                        rows: 12
                        AnchorLayout:
                            anchor_x: "left"
                            anchor_y: "bottom"   
                            MDFloatingActionButton:
                                id: course_add
                                icon: 'arrow-left'
                                opposite_colors: True
                                elevation_normal: 8
                                size: (dp(48), dp(48))
                                on_release: 
                                    root.selected_week -= 1 if root.selected_week > 0  else 0
                                    root.load_course()
                        AnchorLayout:
                            anchor_x: "right"
                            anchor_y: "bottom"  
                            MDFloatingActionButton:
                                id: course_minus
                                icon: 'arrow-right'
                                opposite_colors: True
                                elevation_normal: 8
                                size: (dp(48), dp(48))
                                on_release:
                                    root.selected_week += 1 if root.selected_week < 22 else 0
                                    root.load_course()
                            
                    MDTab:
                        name: 'course_score'
                        text: '成绩'
                        icon: "movie"
                        BoxLayout:
                            MDSpinner:
                                id: new_confe_spinner
                                size_hint: None, None
                                size: dp(46), dp(46)
                                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                                active: True
                    
        MDBottomNavigationItem:
            name: 'community'
            text: "社区"
            icon: 'heart'
            BoxLayout:
                orientation: 'vertical'
                Toolbar:
                    id: toolbar
                    title: "社区"
                    md_bg_color: app.theme_cls.primary_color
                    background_palette: 'Primary'
                    background_hue: '500'
                    right_action_items: [['dots-vertical', lambda x: MDDropdownMenu(items=root.community_menu_items \
                                        if root.ids.community_tab_panel.ids.tab_manager.current != "laf" \
                                        else root.laf_menu_items, width_mult=2.5).open(self)]]
                MDTabbedPanel:
                    tab_width_mode : 'fixed'
                    id: community_tab_panel
                    tab_display_mode:'text'
                    MDTab:
                        name: 'new_confe'
                        text: "社区表白"
                        MDSpinner:
                            id: new_confe_spinner
                            size_hint: None, None
                            size: dp(46), dp(46)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            active: True
                
                    MDTab:
                        name: 'hot_confe'
                        text: '热门表白'
                        MDSpinner:
                            id: hot_confe_spinner
                            size_hint: None, None
                            size: dp(46), dp(46)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            active: True
                    MDTab:
                        name: 'laf'
                        text: '失物招领'
                        MDSpinner:
                            id: new_confe_spinner
                            size_hint: None, None
                            size: dp(46), dp(46)
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            active: True
                    AnchorLayout:
                        anchor_x: "right"
                        anchor_y: "bottom"       
                        MDFloatingActionButton:
                            id: community_menu
                            icon: 'plus'
                            opposite_colors: True
                            elevation_normal: 8
                            size: (dp(48), dp(48))
                            on_release:
                                app.load_screen('WriteConfeScreen' \
                                                    if root.ids.community_tab_panel.ids.tab_manager.current != "laf" \
                                                    else 'WriteLafScreen')
                        
        MDBottomNavigationItem:
            name: 'me'
            text: "我"
            icon: 'account'
            id: account
            BoxLayout:
                orientation: 'vertical'
                Toolbar:
                    id: toolbar
                    title: "我"
                    md_bg_color: app.theme_cls.primary_color
                    background_palette: 'Primary'
                    background_hue: '500'
                ScrollView:
                    do_scroll_x: False    
                    MDList:
                        NavigationDrawerDivider:
                        TwoLineAvatarIconListItem:
                            text: "请登录"
                            secondary_text: "点击编辑"
                            on_release: app.load_screen('MyInfoScreen')
                            AvatarSampleWidget:
                                source: './pic/account.png'
                                
                        NavigationDrawerDivider:
                        NavigationDrawerIconButton:
                            icon: 'message'
                            text: "我的消息"
                            on_release: app.load_screen('MyMsgScreen')
                            IconRightSampleWidget:
                                id: go_to_icon
                                icon: "chevron-right"
                        MDSeparator:
                            height: dp(1)
                        NavigationDrawerIconButton:
                            icon: 'notification-clear-all'
                            text: "系统通知"
                            on_release: app.load_screen('SysMsgScreen')
                            IconRightSampleWidget:
                                id: go_to_icon
                                icon: "chevron-right"
                        NavigationDrawerDivider:
    
                        NavigationDrawerDivider:
                        NavigationDrawerIconButton:
                            icon: 'format-color-fill'
                            text: "主题管理"
                            on_release: MDThemePicker().open()
                            IconRightSampleWidget:
                                id: go_to_icon
                                icon: "chevron-right"
                        MDSeparator:
                            height: dp(1)
                        NavigationDrawerIconButton:
                            icon: 'delete'
                            text: "清理缓存"
                            badge_text: "0 B"
                        MDSeparator:
                            height: dp(1)
                        NavigationDrawerIconButton:
                            icon: 'alert-circle'
                            text: "关于"
                            badge_text: ""
                            on_release: app.load_screen('AboutScreen')
                            IconRightSampleWidget:
                                id: go_to_icon
                                icon: "chevron-right"
                        NavigationDrawerDivider:
                        NavigationDrawerDivider:
                        NavigationDrawerIconButton:
                            icon: 'exit-to-app'
                            text: "注销"
                        NavigationDrawerDivider:


                

'''


class AvatarSampleWidget(ILeftBody, Image):
    pass


class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
    pass


class IconRightSampleWidget(IRightBody, MDIconButton):
    pass


class RightSampleWidget(IRightBodyTouch, MDCheckbox):
    pass


class HackedDemoNavDrawer(MDNavigationDrawer):
    # DO NOT USE
    def add_widget(self, widget, index=0):
        if issubclass(widget.__class__, BaseListItem):
            self._list.add_widget(widget, index)
            if len(self._list.children) == 1:
                widget._active = True
                self.active_item = widget
            # widget.bind(on_release=lambda x: self.panel.toggle_state())
            widget.bind(on_release=lambda x: x._set_active(True, list=self))
        elif issubclass(widget.__class__, NavigationDrawerHeaderBase):
            self._header_container.add_widget(widget)
        else:
            super(MDNavigationDrawer, self).add_widget(widget, index)


class MainScreen(Screen):

    selected_week = NumericProperty(10)
    title = StringProperty()
    week = ['所有课程', '第1周', '第2周', '第3周', '第4周',
            '第5周', '第6周', '第7周', '第8周', '第9周',
            '第10周', '第11周', '第12周', '第13周', '第14周',
            '第15周', '第16周', '第17周', '第18周', '第19周',
            '第20周', '第21周', '第22周']
    course_menu_items = [
        {"viewclass": "DotsMenuButton",
         "name": "UpdateCourse",
         "text": "更新课表"},
        {'viewclass': 'DotsMenuButton',
         "name": "FontSize",
         'text': '字体大小'},
        {'viewclass': 'DotsMenuButton',
         "name": "WeekendCourse",
         'text': '周末课程'},
        {'viewclass': 'DotsMenuButton',
         "name": "DesktopWidget",
         'text': '桌面组件'},
        {'viewclass': 'DotsMenuButton',
         "name": "BackgroundPicture",
         'text': '背景图片'},
        {'viewclass': 'DotsMenuButton',
         "name": "BackgroundTransparent",
         'text': '背景透明度'}
    ]
    community_menu_items = [
        {"viewclass": "DotsMenuButton",
         "name": "MyConfe",
         "text": "我的表白"},
        {'viewclass': 'DotsMenuButton',
         "name": "MyComment",
         'text': '我的评论'},
        {'viewclass': 'DotsMenuButton',
         "name": "Refresh",
         'text': '刷新'}
    ]
    laf_menu_items = [
        {"viewclass": "DotsMenuButton",
         "name": "MyAnnou",
         "text": "我发布的"},
        {'viewclass': 'DotsMenuButton',
         "name": "ConnectOwner",
         'text': '联系失主'}
    ]
    score_menu_items = [
        {"viewclass": "DotsMenuButton",
         "name": "RefreshScore",
         "text": "更新成绩"}
        # {'viewclass': 'DotsMenuButton',
        #  "name": "StatisticsInfo",
        # 'text': '统计信息'},
        # {'viewclass': 'DotsMenuButton',
        #  "name": "Calc",
        # 'text': '计算器'},
    ]

    Builder.load_string(main_widget_kv)

    def on_enter(self):
        Clock.schedule_once(lambda x: self.load_course(), 2)

    def on_pause(self):
        return True

    def on_stop(self):
        pass

    def set_error_message(self, *args):
        if len(self.root.ids.text_field_error.text) == 2:
            self.root.ids.text_field_error.error = True
        else:
            self.root.ids.text_field_error.error = False

    def load_course(self):
        '''
        scheduleList = {'scheduleList': []}
        courseList = {'courseList': {}}
        for schedule_item in a['result']["scheduleList"]:
            scheduleList["scheduleList"].append({'lessonId': schedule_item['lessonId'],'date': schedule_item['date'], 'room': schedule_item['room']['nameZh'], 'campus': schedule_item['room']['building']['campus']['nameZh'], 'weekday': schedule_item['weekday'], 'startTime': schedule_item['startTime'], 'endTime': schedule_item['endTime'], 'personName': schedule_item['personName'], 'weekIndex': schedule_item['weekIndex']})

        for course_item in a['result']['lessonList']:
            courseList['courseList'][course_item['id']] = course_item['courseName']
        scheduleList.update(courseList)
        with open('data.json', 'w',encoding='utf-8') as f:
            json.dump(scheduleList, f, ensure_ascii=False)
        '''
        for weekday in range(1, 8):
            self.ids['weekday_'+str(weekday)].clear_widgets()
        course_data = get_json('course')
        current_week_course = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
        if self.selected_week == 0:
            print("allData")
        else:
            for item in course_data['scheduleList']:               # courses of this week
                if item['weekIndex'] == self.selected_week:
                    current_week_course[item['weekday']].append(item)

        for item in current_week_course:                   # for each day
            print(current_week_course[item])
            weekday_status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # the status of each time
            if current_week_course[item]:                  # if there is any course
                for course in current_week_course[item]:   # for each course
                    last_time = int(round((course['endTime'] - course['startTime'] - 40 * (int(course['endTime'] / 100) -
                                                                                    int(course['startTime'] / 100)))/60))
                    print(last_time)
                    temp_flag = [810, 910, 1020, 1120, 1400, 1500, 1600, 1700, 1900, 2000, 2100].index(course['startTime'])
                    print(temp_flag, last_time)
                    weekday_status[temp_flag] = course['lessonId']
                    for i in range(1, last_time):
                        print(i)
                        weekday_status[temp_flag + i] = course['lessonId']
                print(weekday_status)

                if not weekday_status[0]:                       # 8 o'clock - 9 o'clock
                    self.ids['weekday_' + str(item)].add_widget(
                        MDScreenWidthFlatButton(text="", height=self.ids.weekdays.height / 12))
                else:
                    self.ids['weekday_' + str(item)].add_widget(
                        MDScreenWidthFlatButton(text=str(weekday_status[0]),
                                                height=self.ids.weekdays.height / 12 * weekday_status.count(
                                                    weekday_status[0])))

                for status in range(1, 11):
                    if not weekday_status[status]:              # 10 o'clock - 11 o'clock
                        self.ids['weekday_' + str(item)].add_widget(
                            MDScreenWidthFlatButton(text="", height=self.ids.weekdays.height / 12))
                    else:
                        if weekday_status[status] == weekday_status[status - 1]:
                            pass
                        else:
                            self.ids['weekday_' + str(item)].add_widget(
                                MDScreenWidthFlatButton(text=str(weekday_status[status]),
                                                        height=self.ids.weekdays.height / 12 * weekday_status.count(
                                                            weekday_status[status])))
            else:
                for i in range(0, 11):
                    self.ids['weekday_' + str(item)].add_widget(
                        MDScreenWidthFlatButton(text="", height=self.ids.weekdays.height / 12))


    def select_menu_item(self, name):
        if name == "UpdateCourse":
            self.update_course()
        elif name == "FontSize":
            print("FontSize")
            self.show_sliderbar(text="字体大小")
        # elif name == "WeekendCourse":
        #     print("WeekendCourse")
        # elif name == "DesktopWidget":
        #    print("DesktopWidget")
        elif name == "BackgroundPicture":
            print("BackgroundPicture")
        elif name == "BackgroundTransparent":
            print("BackgroundTransparent")
            self.show_sliderbar(text="背景色透明度")
        elif name == "RefreshScore":
            print("RefreshScore")
        elif name == "Refresh":
            print("Refresh")
        elif name == "ConnectOwner":
            print("ConnectOwner")

    def select_week(self, week):
        self.selected_week = week
        self.bs.dismiss()
        self.load_course()


    def show_week_select(self):
        self.bs = MDListBottomSheet()
        self.bs.add_item("所有课程", lambda x: self.select_week(0))
        self.bs.add_item("第1周", lambda x: self.select_week(1))
        self.bs.add_item("第2周", lambda x: self.select_week(2))
        self.bs.add_item("第3周", lambda x: self.select_week(3))
        self.bs.add_item("第4周", lambda x: self.select_week(4))
        self.bs.add_item("第5周", lambda x: self.select_week(5))
        self.bs.add_item("第6周", lambda x: self.select_week(6))
        self.bs.add_item("第7周", lambda x: self.select_week(7))
        self.bs.add_item("第8周", lambda x: self.select_week(8))
        self.bs.add_item("第9周", lambda x: self.select_week(9))
        self.bs.add_item("第10周", lambda x: self.select_week(10))
        self.bs.add_item("第11周", lambda x: self.select_week(11))
        self.bs.add_item("第12周", lambda x: self.select_week(12))
        self.bs.add_item("第13周", lambda x: self.select_week(13))
        self.bs.add_item("第14周", lambda x: self.select_week(15))
        self.bs.add_item("第15周", lambda x: self.select_week(14))
        self.bs.add_item("第16周", lambda x: self.select_week(16))
        self.bs.add_item("第17周", lambda x: self.select_week(17))
        self.bs.add_item("第18周", lambda x: self.select_week(18))
        self.bs.add_item("第19周", lambda x: self.select_week(19))
        self.bs.add_item("第20周", lambda x: self.select_week(20))
        self.bs.add_item("第21周", lambda x: self.select_week(21))
        self.bs.add_item("第22周", lambda x: self.select_week(22))
        self.bs.open()

    def update_course(self):
        content = MDLabel(font_style='Body1',
                          theme_text_color='Hint',
                          text="更新课表将导致自定义课程丢失，是否继续",
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="更新课表",
                               content=content,
                               size_hint=(.8, None),
                               height=dp(160),
                               auto_dismiss=False)

        self.dialog.add_action_button("取消",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.add_action_button("确定",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    def show_sliderbar(self, text):
        slider = MDSlider(id="slider", min=0, max=100, value=1)
        bs = MDBottomSheet()
        txt = NavigationDrawerSubheader(text=text)
        l = TwoLineListItem()
        bs.add_widget(txt)
        bs.add_widget(slider)
        bs.add_widget(l)
        bs.open()


if __name__ == '__main__':
    MainScreen().run()





'''
class MyApp(App):
    def build(self):
        return MyAppClass()

if __name__=='__main__':
    MyApp().run()
    
    
    
    FloatLayout:       
                                    # size_hint_x: 1 
                                    MDFloatingActionButton:
                                        id: course_add
                                        icon: 'arrow-left'
                                        opposite_colors: True
                                        elevation_normal: 8
                                        # size_hint_x: .5
                                        size: (dp(48), dp(48))
                                        pos_hint: {'center_x': 0.15, 'center_y': 0.3}
                                        on_release: 
                                            root.selected_week -= 1 if root.selected_week > 0  else 0
                                    MDFloatingActionButton:
                                        id: course_minus
                                        icon: 'arrow-right'
                                        opposite_colors: True
                                        elevation_normal: 8
                                        size: (dp(48), dp(48))
                                        pos_hint: {'center_x': 0.85, 'center_y': 0.3}
                                        on_release:
                                            root.selected_week += 1 if root.selected_week < 22 else 0
'''