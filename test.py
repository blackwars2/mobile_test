from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.button import Label #Текст, если нужно
from kivy.uix.boxlayout import BoxLayout #Лайаут, если нужно
from kivy.config import Config


Config.set('graphics', 'resizable', '0') #параметр в положении 0, говорит о том, что наше окно мы растягивать не можем, потянув за края окна мышкой
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '800')





class MyNewApp (App):  #Создам класс
    def build(self):   #Функция лайаут
        layout = BoxLayout(orientation = 'vertical')
        self.lb = Label(text='Алонсо', pos=(20, 50))
        btn1 = Button(text='', background_color = [0,255,0,1], background_normal='', on_press=self.greenBtnpress)
        btn2 = Button(text='', background_color = [255,69,0,1], background_normal='', on_press=self.yellowBtnpress)
        btn3 = Button(text='', background_color = [0,128,128,1], background_normal='', on_press=self.blueBtnpress)
        btn4 = Button(text='', background_color = [255,0,0,1], background_normal='', on_press=self.redBtnpress)
        layout.add_widget(self.lb)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        return layout
    def greenBtnpress(self, instance):
        instance.text = ("Привет Алонсо")
        self.lb.text = "Будешь играть как покушаешь?"
    def yellowBtnpress(self, instance):
        instance.text = ("Привет Алонсо")
        self.lb.text = "Или ты не будешь?"
    def blueBtnpress(self, instance):
        instance.text = ("Привет Алонсо")
        self.lb.text = "Может ты слабый?"

    def redBtnpress(self, instance):
        instance.text = ("Привет Алонсо")
        self.lb.text = "А нет, ты не слабый"

#        return Button(text = "Кнопка", font_size = 20, background_color = [1,0,0,1], background_normal = '', on_press=self.btn_pressRed) #Прописываем кнопку на весь экран, font- размер, background_color = [1,0,0,1] - крас., зел., синий, непрозрачность 1=100



#    def btn_pressRed (self, instance): #Функция кнопки (istance ссылка на наш объект)
#       instance.text = "Ты нажал на кнопку"



if __name__ == "__main__":
    MyNewApp().run()