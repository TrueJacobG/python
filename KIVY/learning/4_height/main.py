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



        # podział na kolumny
        self.cols = 1

        # utworzenie tabelki w środku tej jednej kolumny
        # ustawianie wyokości dla całej tabelki
        self.top_grid = GridLayout(row_force_default=True, row_default_height=50, col_force_default=True, col_default_width=200)
        self.top_grid.cols = 2

        # input - imię
        self.top_grid.add_widget(Label(text="Imię: "))
        self.name = TextInput(multiline=False)
        self.top_grid.add_widget(self.name)

        # input - nazwisko
        self.top_grid.add_widget(Label(text="Nazwisko: "))
        self.surname = TextInput(multiline=False)
        self.top_grid.add_widget(self.surname)

        # input - wiek
        self.top_grid.add_widget(Label(text="Wiek: "))
        self.age = TextInput(multiline=False)
        self.top_grid.add_widget(self.age)

        # stworzenie tabelki z podziałem na 2
        self.add_widget(self.top_grid)



        # submit
        # ustawianie wysokości
        self.submit = Button(text="Send", font_size=32,
                             size_hint_y = None, height="50", size_hint_x = None, width="200")
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