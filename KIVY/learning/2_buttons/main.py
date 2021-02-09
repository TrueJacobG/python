import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    # niskończona ilość znaków
    def __init__(self, **kwargs):
        # wpisywane znaki
        super(MyGridLayout, self).__init__(**kwargs)

        # podział na 2 kolumny
        self.cols = 2

        # input - imię
        self.add_widget(Label(text="Imię: "))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        # input - nazwisko
        self.add_widget(Label(text="Nazwisko: "))
        self.surname = TextInput(multiline=False)
        self.add_widget(self.surname)

        # input - imię
        self.add_widget(Label(text="Wiek: "))
        self.age = TextInput(multiline=False)
        self.add_widget(self.age)

        # submit
        self.submit = Button(text="Send", font_size=32)
        # przypisanie działania do guzika
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        imie = self.name.text
        nazwisko = self.surname.text
        wiek = self.age.text

        # print on terminal
        print(f"Hello {imie} {nazwisko}! Are you really {wiek} y.o?")

        # print on screen
        self.add_widget(Label(text=f"Hello {imie} {nazwisko}! Are you really {wiek} y.o?"))

        # clear inputs
        self.name.text = ""
        self.surname.text = ""
        self.age.text = ""


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__=='__main__':
    MyApp().run()
