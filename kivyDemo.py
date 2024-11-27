from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.checkbox import CheckBox
from kivy.core.clipboard import Clipboard
from kivy.uix.button import Button

import gujhk
import mukhpath
import harikrishna

GHANSHYAM_FONT_PATH = '~/.fonts/GHANSHYAM.ttf'
MARKUP_CLOSER = '[/color]'

class MyApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.q_current = 1
        self.q_total = 1
        self.average_score = 0


    def build(self):

        # Create a horizontal box layout
        top_level_layout = BoxLayout(orientation='horizontal')

        # Create three vertical box layouts within the top layout; the middle
        # layout will be used for widgets
        left_panel = BoxLayout()
        middle_panel = BoxLayout(orientation='vertical')
        right_panel = BoxLayout()
        top_level_layout.add_widget(left_panel)
        top_level_layout.add_widget(middle_panel)
        top_level_layout.add_widget(right_panel)

        # Mukhpath label
        mukhpath_label = Label(text='m&Kpiq', font_size='96sp',
                               font_name=GHANSHYAM_FONT_PATH)
        middle_panel.add_widget(mukhpath_label)

        # Score & options panel
        score_panel = BoxLayout(orientation='horizontal')
        self.score_label = Label(text=f'Question {self.q_current}/{self.q_total}, Average: {self.average_score}')
        virama_box_label = Label(text="Implicitly use viramas")
        self.virama_box = CheckBox()
        copy_button = Button(text='Copy Output')
        copy_input = Button(text='Copy Input')
        copy_button.bind(on_press=self.copy_text)
        copy_input.bind(on_press=self.copy_input)
        score_panel.add_widget(self.score_label)
        score_panel.add_widget(virama_box_label)
        score_panel.add_widget(self.virama_box)
        score_panel.add_widget(copy_button)
        score_panel.add_widget(copy_input)
        middle_panel.add_widget(score_panel)

        # Hint box
        self.hint_box = Label(width=200, font_size='44sp',
            font_name=GHANSHYAM_FONT_PATH,
            halign='center',
            text_size=(1000,None))
        self.hint_box.text = " aj sK) ain>dn) h[l)..."
        middle_panel.add_widget(self.hint_box)

        # Difference box
        self.difference_box = Label(width=200, font_size='44sp',
            font_name=GHANSHYAM_FONT_PATH,
            halign='center',
            text_size=(1000,None),
            markup=True)
        middle_panel.add_widget(self.difference_box)

        # Transliterated box
        self.transliterated_output = Label(width=200, font_size='44sp',
            font_name=GHANSHYAM_FONT_PATH,
            halign='center',
            text_size=(1000,None))


        middle_panel.add_widget(self.transliterated_output)

        # Text box
        self.text_input = TextInput(multiline=False,
                                    background_color=(0.1, 0.1, 0.1, 1),
                                    foreground_color=(1,1,1,1),
                                    halign='center', width=200)
        self.text_input.bind(text=self.on_text_input)
        self.text_input.bind(on_text_validate=self.text_compare)
        middle_panel.add_widget(self.text_input)

        return top_level_layout

    def update_output(self, ascii_text):
        #self.transliterated_output.text = gujhk.ascii_to_guj(ascii_text)
        self.transliterated_output.text = harikrishna.ascii_to_harikrishna(ascii_text)


    def on_text_input(self, instance, value):
        self.update_output(self.text_input.text)

    def copy_text(self, instance):
        Clipboard.copy(self.transliterated_output.text)
        # logger.info('Copied output text to clipboard.')

    def copy_input(self, instance):
        Clipboard.copy(self.text_input.text)

    def update_difference_box(self, diff_str : str):
        # Set all text to green
        self.difference_box.color = '#00FF00'

        # Escape [ and ] with a backslash
        diff_str = diff_str.replace('[', '\[').replace(']', '\]')

        markup_str = []
        i = 0

        while i < len(diff_str):
            if diff_str[i] in ['+', '-']:
                markup_str.append(diff_str[i])
                i += 1
                # Add a closer after the letter
                markup_str.append(diff_str[i])
                markup_str.append(MARKUP_CLOSER)
            else:
                markup_str.append(diff_str[i])

            i += 1

        # Add markup closing brackets for - and +
        markup_str = ''.join(markup_str).replace('+','[color=ffff00]').replace('-','[color=ff0000]')

        self.difference_box.text = markup_str

    def update_score(self, ratio : float):
        self.score_label.text = '{:.2f}'.format(ratio)

    def text_compare(self, instance):
        diff_str, ratio = mukhpath.compare(
                                           self.transliterated_output.text,
                                           self.hint_box.text
        )
        diff_str = diff_str.replace('   ','128').replace(' ', '').replace('128', ' ')
        self.update_score(ratio)
        self.update_difference_box(diff_str.replace('', ''))

        # def on_text_change(self, instance):
    #     # Update the output label with the text from the TextInput
    #     self.output_label.text = self.text_input.text


if __name__ == '__main__':
    MyApp().run()
