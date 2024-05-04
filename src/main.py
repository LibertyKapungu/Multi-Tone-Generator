import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import pygame
from pygame import mixer
import kivy
from kivy.clock import Clock
import math
import numpy as np

class MyLayout(BoxLayout):

    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        pygame.init()
        self.orientation = 'vertical'

        self.playing = False

        self.f1 = 1000
        self.f2 = 3000
        self.f3 = 7000
        self.f4 = 9000

        self.ampl1 = 0.0
        self.ampl2 = 0.0
        self.ampl3 = 0.0
        self.ampl4 = 0.0

        self.left_active = False
        self.right_active = False

        padding_vals = [20, 20, 20, 20]

        menu_button = Button(text='Set Freq', size_hint=(None, None), size=(90, 50), pos_hint={'top': 1, 'left': 1})
        menu_button.bind(on_release=self.open_popup)

        top_layout = BoxLayout(size_hint_y=None, height=110, spacing = 20, padding = padding_vals)
        
        on_f1_f2 = Button(text='F1,2 ON')
        on_f1_f2.bind(on_press=self.on_button_press)
        top_layout.add_widget(on_f1_f2)
        
        f1_on = Button(text = 'F1')
        f1_on.bind(on_press=self.on_button_press)
        top_layout.add_widget(f1_on)

        f2_on = Button(text = 'F2')
        f2_on.bind(on_press=self.on_button_press)
        top_layout.add_widget(f2_on)

        off_f1_f2 = Button(text='F1,2 OFF')
        off_f1_f2.bind(on_press=self.on_button_press)
        top_layout.add_widget(off_f1_f2)

        bottom_layout = BoxLayout(size_hint_y=None, height=110, spacing = 20, padding = padding_vals)
        
        on_f3_f4 = Button(text='F3,4 ON')
        on_f3_f4.bind(on_press=self.on_button_press)
        bottom_layout.add_widget(on_f3_f4)
        
        f3_on = Button(text = 'F3')
        f3_on.bind(on_press=self.on_button_press)
        bottom_layout.add_widget(f3_on)

        f4_on = Button(text = 'F4')
        f4_on.bind(on_press=self.on_button_press)
        bottom_layout.add_widget(f4_on)

        off_f3_f4 = Button(text='F3,4 OFF')
        off_f3_f4.bind(on_press=self.on_button_press)
        bottom_layout.add_widget(off_f3_f4)

        self.LHS_buttons = []
        self.RHS_buttons = []

        self.LHS_buttons.append(f1_on)
        self.LHS_buttons.append(f2_on)
        self.LHS_buttons.append(on_f1_f2)
        self.LHS_buttons.append(off_f1_f2)

        self.RHS_buttons.append(f3_on)
        self.RHS_buttons.append(f4_on)
        self.RHS_buttons.append(on_f3_f4)
        self.RHS_buttons.append(off_f3_f4)

        self.common_frequency_label = Label(text="Common Frequency (Hz):")
        self.status_label = Label(text="Not Playing")
        self.status_button = Button(size_hint=(1, .5) ,text='Start', on_press=self.edit_status)

        self.add_widget(menu_button)
        self.add_widget(top_layout)
        self.add_widget(self.common_frequency_label)
        self.add_widget(self.status_label)
        self.add_widget(self.status_button)

        self.add_widget(BoxLayout())
        self.add_widget(bottom_layout)

    def on_button_press(self, instance):
       
        lhs_btn = False
        rhs_btn = False

        for btn in self.LHS_buttons:
            if btn.text == instance.text:
                lhs_btn = True
                rhs_btn = False
                break

            else:
                rhs_btn = True
                lhs_btn = False

        if lhs_btn:
            for btn in self.LHS_buttons:
                btn.background_color = (0, 0, 1, 1)
        else:
            for btn in self.RHS_buttons:
                btn.background_color = (0, 0, 1, 1)

        button_text = instance.text
        instance.background_color = (1, 0, 0, 1)

        if button_text == "F1":
            print(button_text + "Pressed")
            self.left_active = True
            self.ampl1 = 0.5
            self.ampl2 = 0.0
            pygame.mixer.Channel(1).stop()
            
        elif button_text == "F2":
            print(button_text + "Pressed")
            self.ampl1 = 0.0
            self.ampl2 = 0.5
            pygame.mixer.Channel(0).stop()
            self.left_active = True

        elif button_text == "F3":
            print(button_text + "Pressed")
            self.ampl3 = 0.5
            self.ampl4 = 0.0
            pygame.mixer.Channel(3).stop()
            self.right_active = True

        elif button_text == "F4":
            print(button_text + "Pressed")
            self.right_active = True
            self.ampl3 = 0.0
            self.ampl4 = 0.5
            pygame.mixer.Channel(2).stop()
            
        elif button_text == "F1,2 ON":
            print(button_text + "Pressed")
            self.left_active = True
            self.ampl1 = 0.5
            self.ampl2 = 0.5
            
        elif button_text == "F3,4 ON":
            print(button_text + "Pressed")
            self.right_active = True
            self.ampl3 = 0.5
            self.ampl4 = 0.5
            
        elif button_text == "F1,2 OFF":
            print(button_text + "Pressed")
            self.left_active = False
            self.ampl1 = 0.0
            self.ampl2 = 0.0
            pygame.mixer.Channel(0).stop()
            pygame.mixer.Channel(1).stop()
            
        elif button_text == "F3,4 OFF":
            print(button_text + "Pressed")
            self.right_active = False
            self.ampl3 = 0.0
            self.ampl4 = 0.0
            pygame.mixer.Channel(2).stop()
            pygame.mixer.Channel(3).stop()

        else:
            self.ampl1 = 0.0
            self.ampl2 = 0.0
            self.ampl3 = 0.0
            self.ampl4 = 0.0
            pygame.mixer.stop()

        print(self.f1)
        print(self.f2)
        print(self.f3)
        print(self.f4)

        print(self.ampl1)
        print(self.ampl2)
        print(self.ampl3)
        print(self.ampl4)

        self.generate_sound()

    def edit_status(self, instance):

        if self.playing:
            self.status_button.text = 'Not Playing'
            self.status_button.background_color = (1, 0, 0, 1)
            self.status_label.text = "Status: Stopped"

            self.ampl1 = 0.0
            self.ampl2 = 0.0
            self.ampl3 = 0.0
            self.ampl4 = 0.0

        else:
            self.status_button.text = 'Playing Sound'
            self.status_button.background_color = (0, 0, 1, 1)
            self.status_label.text = "Status: Playing"

        self.playing = not self.playing
        self.generate_sound()
        
    def open_popup(self, instance):

        frequency_values = []

        content = BoxLayout(orientation='vertical')

        f1_input = TextInput(hint_text=str(self.f1), input_filter = 'int')
        f2_input = TextInput(hint_text=str(self.f2), input_filter = 'int')
        f3_input = TextInput(hint_text=str(self.f3), input_filter = 'int')
        f4_input = TextInput(hint_text=str(self.f4), input_filter = 'int')

        frequency_values.append(f1_input)
        frequency_values.append(f2_input)
        frequency_values.append(f3_input)
        frequency_values.append(f4_input)

        content.add_widget(f1_input)
        content.add_widget(f2_input)
        content.add_widget(f3_input)
        content.add_widget(f4_input)

        save_btn = Button(text='Save', size_hint=(1, 1))
        save_btn.bind(on_press = lambda instance: self.save_frequencies(frequency_values))
        content.add_widget(save_btn)

        close_btn = Button(text='Close', size_hint=(1, 1))
        content.add_widget(close_btn)

        popup = Popup(title='Set Frequencies(Hz) 1-4', content=content, size_hint=(None, None), size=(300, 400))
        close_btn.bind(on_release=popup.dismiss)

        popup.open()

    def save_frequencies(self, frequency_inputs, *args):
        
        frequency_array = [0, 0, 0, 0]

        for i, freq in enumerate(frequency_inputs):
            if not freq.text:
                frequency_array[i] = 0
            else:
                frequency_array[i] = freq.text

        self.f1, self.f2, self.f3, self.f4 = frequency_array

        self.generate_sound()

    def generate_tone(self, frequency, amplitude, sample_rate, duration):

        num_samples = int(sample_rate * duration)

        time_array = np.linspace(0, duration, num_samples)

        frequency = frequency / 2

        wave_array = amplitude * np.sin(2 * np.pi * frequency * time_array)
        wave_integers = (wave_array * 32767).astype(np.int16)

        return wave_integers

    
    def generate_sound(self):
        
        sample_rate = 44100
        bitsize = -16
        channels = 4
        buffer = 2048
        duration = 1.0
        
        pygame.mixer.init(sample_rate, bitsize, channels, buffer)

        tone1 = self.generate_tone(self.f1, self.ampl1, sample_rate, duration)
        tone2 = self.generate_tone(self.f2, self.ampl2, sample_rate, duration)
        tone3 = self.generate_tone(self.f3, self.ampl3, sample_rate, duration)
        tone4 = self.generate_tone(self.f4, self.ampl4, sample_rate, duration)

        channel1 = pygame.mixer.Channel(0)
        channel2 = pygame.mixer.Channel(1)
        channel3 = pygame.mixer.Channel(2)
        channel4 = pygame.mixer.Channel(3)

        if self.playing:

            if self.left_active == True:
                channel1.play(pygame.mixer.Sound(tone1), loops=-1) 
                channel2.play(pygame.mixer.Sound(tone2), loops=-1)
            else:
                channel1.stop()
                channel2.stop()
            
            if self.right_active == True:
                channel3.play(pygame.mixer.Sound(tone3), loops=-1)
                channel4.play(pygame.mixer.Sound(tone4), loops=-1)
            else:
                channel3.stop()
                channel4.stop()

        else:
            pygame.mixer.stop()

class MyApp(App):

    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()
