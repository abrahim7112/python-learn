from kivmob import KivMob, TestIds
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.slider import Slider
from functools import partial
from kivy.clock import Clock
from kivy.lang import Builder
import arabic_reshaper
import bidi.algorithm
from bidi.algorithm import get_display
from kivymd.app import MDApp
from kivymd.uix.behaviors import CommonElevationBehavior
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.toolbar import MDTopAppBar
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.textfield import MDTextField

KV = '''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
#:import arabic_reshaper arabic_reshaper
#:import get_display bidi.algorithm.get_display

<ExtendedButton>
    elevation: 3
    shadow_radius: 10
    shadow_softness: 2
    -height: "56dp"


<DrawerClickableItem@MDNavigationDrawerItem>
    focus_color: "orange"
    unfocus_color: "#f55cf4"


MDScreen:

    MDNavigationLayout:

        ScreenManager:
            MDScreen:

                MDBoxLayout:
                    orientation: "vertical"

                    MDTopAppBar:
                        title: get_display(arabic_reshaper.reshape("Python language"))
                        #title_font:"Arial.ttf"
                        text_color_active: "blue"
                        text_color_normal: "orange"
                        panel_color: "black"
                        #elevation: 5
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]

                    MDBottomNavigation:
                        text_color_active: "blue"
                        text_color_normal: "orange"
                        panel_color: "black"
        
                        MDBottomNavigationItem:
                            name: 'screen 1'
                            text: 'python'
                            icon: 'language-python'

                            ScreenManager:
                                #id: manager

                                MDScreen:
                                    #name: "one"

                                    ScrollView:
                                        GridLayout:
                                            size_hint_y: None
                                            height: self.minimum_height
                                            spacing: "5dp"
                                            padding: "5dp"
                                            cols: 1
                                            Button:
                                                text_size: self.width, None
                                                height: self.texture_size[1]
                                                size_hint_y: None
                                                background_color:"orange"
                                                halign: "center"
                                                spacing: "20dp"
                                                padding: "20dp"
                                                font_size: "65"
                                                font_name:"Arial.ttf"
                                                text: get_display(arabic_reshaper.reshape("ليساعدك هنا البرنامج التعليمي المصمم خصيصًا على تعلم لغة برمجة  بايثون بأكثر الطرق فعالية ، مع موضوعات من الأساسيات إلى المتقدمة"))
                                                color: "white"

                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("مقدمة لغة برمجة بايثون"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page1()

                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("اول تطبيق  بايثون"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page2()
                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("كلمات بايثون"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page3()
                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("مساحات الأسماء والنطاق في بايثون"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page4()
                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("كيفية تعيين قيم للمتغيرات في بايثون"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page5()
                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("أخذ المدخلات في بايثون"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page6()
                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("كيف تطبع بدون سطر جديد في بايثون؟"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page7()
                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("بايثون | تنسيق الإخراج"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page8()
                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("مشغلي بايثون"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page9()
                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("عامل ثلاثي في ​​بايثون"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page10()
                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("مشغلي القسم في بايثون"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page11()
                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("وظائف المشغل في بايثون"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page12()

                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("سلاسل ، قوائم ، مجموعات ، تكرارات"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page13()

                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("Python Tuples"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page14()

                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("مجموعات بايثون"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page15()


                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("قاموس بايثون"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page16()

                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("بيثون إذا كان آخر"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page17()

                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("بايثون للحلقات"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page18()
                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("بيان كسر بايثون"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page19()
                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("تقنيات التكرار في بايثون"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page20()
                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("وظائف بايثون"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page21()
                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("بايثون لامدا"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page22()
                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("كلمة رئيسية عالمية في Python"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page23()
                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("وظائف First Class في Python"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page24()
                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("مصممون في بايثون"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page25()
                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("فئات وكائنات بايثون"))
                                                on_release:
                                                    app.interstitial()
                                                    app.page26()

                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("المدمرات في بايثون"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page27()
                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("أنواع وراثة بايثون"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page28()
                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("التغليف في بايثون"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page29()

                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("المتغيرات الطبقية أو الثابتة في بايثون"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page30()

                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("معالجة استثناء بايثون"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page31()

                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("بايثون جرب إلا"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page32()

                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("الأخطاء والاستثناءات في بايثون"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page33()
                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("خطأ NZEC في Python"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page34()

                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("افتح ملفًا في بايثون"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page35()

                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("أساسيات معالجة الملفات"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page36()
                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("التعبيرات العادية في Python"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page37()

                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("عدادات في بايثون"))
                                                on_release: app.page38()

                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("الافتراضي في بايثون"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page39()

                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("قائمة انتظار الكومة (أو heapq) في Python"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page40()

                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("البرمجة الوظيفية في بايثون"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page41()

                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("Metaprogramming مع Metaclasses في بايثون"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page42()

                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("دروس مجردة في بايثون"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page43()

                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("تعدد مؤشرات الترابط في بايثون"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page44()

                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("المعالجة المتعددة في بايثون"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page45()

                                            Button:
                                                size_hint_y : None
                                                height : 100
                                                font_name:"Arial.ttf"
                                                background_color:(1, 0, 0, 1)
                                                text: get_display(arabic_reshaper.reshape("برمجة المقبس في بايثون"))
                                                on_release: 
                                                    app.interstitial()
                                                    app.page46()


        
                        MDBottomNavigationItem:
                            name: 'screen 2'
                            text: 'home'
                            icon: 'home'

                            ScrollView:
                                GridLayout:
                                    size_hint_y: None
                                    height: self.minimum_height
                                    spacing: "5dp"
                                    padding: "5dp"
                                    cols: 1

                                    Button:
                                        text_size: self.width, None
                                        height: self.texture_size[1]
                                        size_hint_y: None
                                        background_color:"orange"
                                        halign: "center"
                                        spacing: "20dp"
                                        padding: "20dp"
                                        font_name:"Arial.ttf"
                                        font_size: "60"
                                        text: get_display(arabic_reshaper.reshape("البرامج والمشاريع  والمواقع والبنى التحتية أساسيات البرمجة  عبر المكتبات التالية لانشاء  يساعدك هذا البرنامج التعليمي  على تعلم"))
                                        color: "white"

                                    TwoLineAvatarListItem:
                                        text: "Python NumPy"
                                        secondary_text: "learn Python NumPy"
                                        on_release:
                                            app.REWARDED_VIDEO()
                                            app.NumPy()
                                        IconLeftWidget:
                                            icon: "language-python"

                                    TwoLineAvatarListItem:
                                        text: "Python Pandas"
                                        secondary_text: "learn Python Pandas"
                                        on_release:
                                            app.REWARDED_VIDEO()
                                            app.Pandas()
                                        IconLeftWidget:
                                            icon: "language-python"

                                    TwoLineAvatarListItem:
                                        text: "Python Django"
                                        secondary_text: "learn Python Django"
                                        on_release:
                                            app.REWARDED_VIDEO()
                                            app.Django()
                                        IconLeftWidget:
                                            icon: "language-python"

                                    TwoLineAvatarListItem:
                                        text: "Python mysql"
                                        secondary_text: "learn Python mysql"
                                        on_release:
                                            app.REWARDED_VIDEO()
                                            app.mysql()
                                        IconLeftWidget:
                                            icon: "language-python"

                                    TwoLineAvatarListItem:
                                        text: "Python MongoDB"
                                        secondary_text: "learn Python MongoDB"
                                        on_release:
                                            app.REWARDED_VIDEO()
                                            app.MongoDB()
                                        IconLeftWidget:
                                            icon: "language-python"

                                    TwoLineAvatarListItem:
                                        text: "Python OpenCV"
                                        secondary_text: "learn Python OpenCV"
                                        on_release:
                                            app.REWARDED_VIDEO()
                                            app.OpenCV()
                                        IconLeftWidget:
                                            icon: "language-python"

                                    TwoLineAvatarListItem:
                                        text: "Python selenium"
                                        secondary_text: "learn Python selenium"
                                        on_release:
                                            app.REWARDED_VIDEO()
                                            app.selenium()
                                        IconLeftWidget:
                                            icon: "language-python"

                                    TwoLineAvatarListItem:
                                        text: "Python Tkinter"
                                        secondary_text: "learn Python Tkinter"
                                        on_release:
                                            app.REWARDED_VIDEO()
                                            app.Tkinter()
                                        IconLeftWidget:
                                            icon: "language-python"

                                    TwoLineAvatarListItem:
                                        text: "Python kivy"
                                        secondary_text: "learn Python kivy"
                                        on_release:
                                            app.REWARDED_VIDEO()
                                            app.kivy()
                                        IconLeftWidget:
                                            icon: "language-python"



    MDNavigationDrawer:
        id: nav_drawer
        radius: (0, 16, 16, 0)
        md_bg_color: "#444444"#"orange"##fffcf4
        elevation: 4
        width: "240dp"

        MDNavigationDrawerMenu:

            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                spacing: "5dp"
                padding: "3dp", 0, 0, "5dp"

                FitImage:
                    source: "image.jpg"
                    height: "200dp"
                    size_hint_y: None
                    radius: (20, 25, 25, 20)
                ExtendedButton:
                    text: "abrahim71192@gmail.com"
                    icon: "pencil"

            DrawerClickableItem:
                text: "Python"
                icon: "language-python"
                on_release: 
                    app.interstitial()
                    import webbrowser
                    webbrowser.open('https://www.geeksforgeeks.org/python-programming-language/')

            DrawerClickableItem:
                text: "JavaScript"
                icon: "language-javascript"
                on_release: 
                    app.interstitial()
                    import webbrowser
                    webbrowser.open('https://www.geeksforgeeks.org/javascript/?ref=shm')

            DrawerClickableItem:
                text: "CPP"
                icon: "language-cpp"
                on_release:
                    app.interstitial()
                    import webbrowser
                    webbrowser.open('https://www.geeksforgeeks.org/c-plus-plus/?ref=shm')

            DrawerClickableItem:
                text: "Swift"
                icon: "language-swift"
                on_release:
                    app.interstitial()
                    import webbrowser
                    webbrowser.open('https://www.geeksforgeeks.org/swift-tutorial/?ref=header_search')
            DrawerClickableItem:
                text: "about"
                icon: "account"
                on_release: 
                    app.interstitial()
                    import webbrowser
                    webbrowser.open('https://github.com/abrahim7112')
'''


class ExtendedButton(MDFillRoundFlatIconButton, CommonElevationBehavior):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.padding = "16dp"
        Clock.schedule_once(self.set_spacing)

    def set_spacing(self, interval):
        self.ids.box.spacing = "12dp"

    def set_radius(self, *args):
        if self.rounded_button:
            self._radius = self.radius = self.height / 4


class Python(MDApp):
    def build(self):
        #self.theme_cls.theme_style = "Dark"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.material_style = "M2"
        self.theme_cls.primary_palette = "Orange"
        self.ads = KivMob('ca-app-pub-9960257549650503~9574565740')
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9613298039')
        self.ads.request_interstitial()
        self.ads.show_interstitial()
        self.ads.new_banner('ca-app-pub-9960257549650503/9996441416')
        self.ads.request_banner()
        self.ads.hide_banner()
        self.ads.show_banner()
        return Builder.load_string(KV)

    def on_resume(self):
        self.ads.load_rewarded_ad("ca-app-pub-9960257549650503/3095914504")
        self.ads.request_interstitial()
        self.ads.request_banner()

    def interstitial(self):
        self.ads.new_interstitial('ca-app-pub-9960257549650503/3095914504')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def REWARDED_VIDEO(self):
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def REWARDED(self):
        self.ads.load_rewarded_ad("ca-app-pub-9960257549650503/3095914504")
        self.ads.show_rewarded_ad()
    def NumPy(self):
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()
        popup = Popup(title=get_display(arabic_reshaper.reshape("مكتبة بايثون نومبي")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/NumPy.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()

    def Pandas(self):
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()
        popup = Popup(title=get_display(arabic_reshaper.reshape("مكتبة بايثون باندا")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/Pandas.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
    def Django(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape("مكتبة بايثون ديجنجو")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/Django.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()
    def mysql(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape("مكتبة بايثون mysql")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/mysql.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()
    def MongoDB(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape("مكتبة بايثون MongoDB")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/MongoDB.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def OpenCV(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape("مكتبة بايثون OpenCV")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/OpenCV.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def selenium(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape("مكتبة بايثون selenium")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/selenium.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()
    def Tkinter(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape("رنامج بايثون تكينتر التعليمي")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/Tkinter.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()
    def kivy(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape("مكتبة بايثون Kivy")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/kivy.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page1(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape("مقدمة لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, halign="center", font_size=50,multiline= True)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page2(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape("اول تطبيق  بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et1.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page3(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape("لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et2.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page4(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et3.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page5(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et4.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page6(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et5.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page7(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et6.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page8(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et7.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page9(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et8.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page10(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et9.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page11(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et10.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None,multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page12(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et11.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page13(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et12.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page14(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et14.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page15(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et15.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page16(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et16.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page17(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et17.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page18(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et18.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None,multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page19(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et19.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()
    def page20(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et20.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None,multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()    
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page21(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et21.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None,multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page22(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et22.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()


    def page23(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et23.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()


    def page24(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et24.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()


    def page25(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et25.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page26(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et26.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page27(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et27.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page28(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et28.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page29(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et29.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page30(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et30.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page31(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et31.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page32(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et32.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page33(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et33.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page34(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et34.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page35(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et35.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page36(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et36.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page37(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et37.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None,multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page38(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et38.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page39(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et39.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None,multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page40(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et40.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None,multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page41(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et41.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page42(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et42.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page43(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et43.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page44(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et44.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page45(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et45.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def page46(self):
        popup = Popup(title=get_display(arabic_reshaper.reshape(" لغة برمجة بايثون")), title_font="Arial.ttf")
        layout1 = StackLayout(orientation='lr-bt')
        closebutton = Button(text=get_display(arabic_reshaper.reshape("اغلاق الصفحة")), font_name="Arial.ttf", size_hint=(0.9,0.05),background_color=(1, 0, 0, 1))
        closebutton.bind(on_press=popup.dismiss)
        scrlv = ScrollView(size_hint=(0.9,0.95))
        s = Slider(min=0, max=1, value=15, orientation='vertical', step=0.01, size_hint=(0.1, 0.95))
        scrlv.bind(scroll_y=partial(self.slider_change, s))
        s.bind(value=partial(self.scroll_change, scrlv))
        layout2 = GridLayout(cols=1, size_hint_y=None)
        layout2.bind(minimum_height=layout2.setter('height'))
        btnn = open(r"lin/et46.txt", "r").read()
        reshaped_text = arabic_reshaper.reshape(btnn)
        bidi_text = bidi.algorithm.get_display(reshaped_text)
        btn = MDTextField(text=bidi_text, font_name="Arial.ttf", size_hint_y=None, multiline= True, halign="center", font_size=50)
        btn.text_size = (btn.size)
        layout2.add_widget(btn)
        scrlv.add_widget(layout2)
        layout1.add_widget(closebutton)
        layout1.add_widget(scrlv)
        layout1.add_widget(s)
        popup.content = layout1
        popup.open()
        self.ads.new_interstitial('ca-app-pub-9960257549650503/9750636978')
        self.ads.request_interstitial()
        self.ads.show_interstitial()

    def scroll_change(self, scrlv, instance, value):
        scrlv.scroll_y = value

    def slider_change(self, s, instance, value):
        if value >= 0:
        #this to avoid 'maximum recursion depth exceeded' error
            s.value=value

if __name__ == '__main__':
    Python().run()

