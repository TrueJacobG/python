from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


# deklarowanie ekranów
class MenuScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class TestApp(App):
    def build(self):
        # tworzenie dwóch ekranów
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))

        return sm


if __name__ == '__main__':
    TestApp().run()