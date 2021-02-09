import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGridLayout(Widget):
    # w nawiasie to jaka wartość jak aplikacja się uruchamia
    name = ObjectProperty(None)
    surname = ObjectProperty(None)
    age = ObjectProperty(None)

    def press(self):
        name = self.name.text
        surname = self.surname.text
        age = self.age.text

        # print on terminal
        print(f"Hello {name} {surname}! Are you really {age} y.o?")

        # clear inputs
        self.name.text = ""
        self.surname.text = ""
        self.age.text = ""


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__=='__main__':
    MyApp().run()