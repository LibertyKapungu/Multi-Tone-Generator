from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivy.properties import ListProperty

import pygame
import numpy as np

Builder.load_file('main_design.kv')

class MyLayout(BoxLayout):

    frequencies = ListProperty([0] * 4) # [f1 f2 f3 f4]
    amplitudes = ListProperty([0.0] * 4) # [a1 a2 a3 a4]

    def __init__(self, **kwargs):
        
        super(MyLayout, self).__init__(**kwargs)
        pygame.init()
        
        self.playing_sound = False

    def update_frequency(self, index, value):

        self.frequencies[index] = value

    def update_amplitude(self, index, value):

        self.amplitudes[index] = value

    def on_button_press(self, instance):
       
        button_text = instance.text

        if button_text == "F1":
            print(button_text + "Pressed")
            self.update_amplitude(0 , 0.5)  #Set amplitude 1 to 0.5
            self.update_amplitude(1 , 0)    #Set amplitude 2 to 0
            self.ids.f1_ON.background_color = (0, 1, 0, 1)
            self.ids.f2_ON.background_color = (0, 0, 1, 1)
            self.ids.f1_f2_ON.background_color = (0, 0, 1, 1)
            self.ids.f1_f2_OFF.background_color = (0, 0, 1, 1)
            pygame.mixer.Channel(1).stop()

        elif button_text == "F2":
            print(button_text + "Pressed")
            self.update_amplitude(0 , 0)   #Set amplitude 1 to 0
            self.update_amplitude(1 , 0.5) #Set amplitude 2 to 0.5
            self.ids.f1_ON.background_color = (0, 0, 1, 1)
            self.ids.f2_ON.background_color = (0, 1, 0, 1)
            self.ids.f1_f2_ON.background_color = (0, 0, 1, 1)
            self.ids.f1_f2_OFF.background_color = (0, 0, 1, 1)
            pygame.mixer.Channel(0).stop()

        elif button_text == "F3":
            print(button_text + "Pressed")
            self.update_amplitude(2 , 0.5)  #Set amplitude 3 to 0.5
            self.update_amplitude(3 , 0)    #Set amplitude 4 to 0
            self.ids.f3_ON.background_color = (0, 1, 0, 1)
            self.ids.f4_ON.background_color = (0, 0, 1, 1)
            self.ids.f3_f4_ON.background_color = (0, 0, 1, 1)
            self.ids.f3_f4_OFF.background_color = (0, 0, 1, 1)
            pygame.mixer.Channel(3).stop()

        elif button_text == "F4":
            print(button_text + "Pressed")
            self.update_amplitude(2 , 0)   #Set amplitude 3 to 0
            self.update_amplitude(3 , 0.5) #Set amplitude 4 to 0.5
            self.ids.f3_ON.background_color = (0, 0, 1, 1)
            self.ids.f4_ON.background_color = (0, 1, 0, 1)
            self.ids.f3_f4_ON.background_color = (0, 0, 1, 1)
            self.ids.f3_f4_OFF.background_color = (0, 0, 1, 1)
            pygame.mixer.Channel(2).stop()
            
        elif button_text == "F1,2 ON":
            print(button_text + "Pressed")
            self.left_active = True
            self.update_amplitude(0 , 0.5) #Set amplitude 1 to 0.5
            self.update_amplitude(1 , 0.5) #Set amplitude 2 to 0.5
            self.ids.f1_ON.background_color = (0, 0, 1, 1)
            self.ids.f2_ON.background_color = (0, 0, 1, 1)
            self.ids.f1_f2_ON.background_color = (0, 1, 0, 1)
            self.ids.f1_f2_OFF.background_color = (0, 0, 1, 1)
            
        elif button_text == "F3,4 ON":
            print(button_text + "Pressed")
            self.right_active = True
            self.update_amplitude(2 , 0.5) #Set amplitude 3 to 0.5
            self.update_amplitude(3 , 0.5) #Set amplitude 4 to 0.5
            self.ids.f3_ON.background_color = (0, 0, 1, 1)
            self.ids.f4_ON.background_color = (0, 0, 1, 1)
            self.ids.f3_f4_ON.background_color = (0, 1, 0, 1)
            self.ids.f3_f4_OFF.background_color = (0, 0, 1, 1)
            
        elif button_text == "F1,2 OFF":
            print(button_text + "Pressed")
            self.update_amplitude(0 , 0) #Set amplitude 1 to 0
            self.update_amplitude(1 , 0) #Set amplitude 2 to 0
            pygame.mixer.Channel(0).stop()
            pygame.mixer.Channel(1).stop()
            self.ids.f1_ON.background_color = (0, 0, 1, 1)
            self.ids.f2_ON.background_color = (0, 0, 1, 1)
            self.ids.f1_f2_ON.background_color = (0, 0, 1, 1)
            self.ids.f1_f2_OFF.background_color = (0, 1, 0, 1)
            
        elif button_text == "F3,4 OFF":
            print(button_text + "Pressed")
            self.update_amplitude(2 , 0) #Set amplitude 3 to 0
            self.update_amplitude(3 , 0) #Set amplitude 4 to 0
            pygame.mixer.Channel(2).stop()
            pygame.mixer.Channel(3).stop()
            self.ids.f3_ON.background_color = (0, 0, 1, 1)
            self.ids.f4_ON.background_color = (0, 0, 1, 1)
            self.ids.f3_f4_ON.background_color = (0, 0, 1, 1)
            self.ids.f3_f4_OFF.background_color = (0, 1, 0, 1)

        else:
            pygame.mixer.stop()

        self.generate_sound()

        print(self.frequencies)
        print(self.amplitudes)

    def edit_status(self, instance):

        if self.playing_sound:
            pygame.mixer.stop()
            instance.text = 'Not Playing Tones'
            instance.background_color = (1, 0, 0, 1)
        else:
            instance.text = 'Active'
            instance.background_color = (0, 1, 0, 1)

        self.playing_sound = not self.playing_sound
        
    def open_popup(self):

        frequency_values = []

        content = BoxLayout(orientation='vertical')

        f1_input = TextInput(hint_text=str(self.frequencies[0]), input_filter = 'int')
        f2_input = TextInput(hint_text=str(self.frequencies[1]), input_filter = 'int')
        f3_input = TextInput(hint_text=str(self.frequencies[2]), input_filter = 'int')
        f4_input = TextInput(hint_text=str(self.frequencies[3]), input_filter = 'int')

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
        
        for i, freq in enumerate(frequency_inputs):
            if not freq.text and (self.frequencies[i] <= 0):
                self.frequencies[i] = 0
            elif not freq.text and self.frequencies[i] > 0:
                self.frequencies[i] = self.frequencies[i]
            else:
                self.frequencies[i] = int(freq.text)

    def generate_tone(self, frequency, amplitude, sample_rate, duration):

        num_samples = int(sample_rate * duration)
        time_array = np.linspace(0, duration, num_samples)

        frequency = frequency / 2

        wave_array = amplitude * np.sin(2 * np.pi * frequency * time_array)
        wave_integers = (wave_array * 32767).astype(np.int16)

        return wave_integers

    def generate_sound(self):
        
        if not self.playing_sound: #Not activated
            pygame.mixer.stop()
            return
        
        sample_rate = 44100
        bitsize = -16
        channels = 4
        buffer = 2048
        duration = 1.0
        
        pygame.mixer.init(sample_rate, bitsize, channels, buffer)

        tone1 = self.generate_tone(self.frequencies[0], self.amplitudes[0], sample_rate, duration)
        tone2 = self.generate_tone(self.frequencies[1], self.amplitudes[1], sample_rate, duration)
        tone3 = self.generate_tone(self.frequencies[2], self.amplitudes[2], sample_rate, duration)
        tone4 = self.generate_tone(self.frequencies[3], self.amplitudes[3], sample_rate, duration)

        channel1 = pygame.mixer.Channel(0)
        channel2 = pygame.mixer.Channel(1)
        channel3 = pygame.mixer.Channel(2)
        channel4 = pygame.mixer.Channel(3)

        channel1.play(pygame.mixer.Sound(tone1), loops=-1) 
        channel2.play(pygame.mixer.Sound(tone2), loops=-1)
        channel3.play(pygame.mixer.Sound(tone3), loops=-1)
        channel4.play(pygame.mixer.Sound(tone4), loops=-1)
        
class MyApp(App):

    def build(self):
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()
