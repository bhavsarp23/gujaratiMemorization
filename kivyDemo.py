from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.checkbox import CheckBox
from kivy.core.clipboard import Clipboard
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown

import logging

import gujhk
import mukhpath
import harikrishna

GHANSHYAM_FONT_PATH = './GHANSHYAM.ttf'
#GHANSHYAM_FONT_PATH = './sarjudas.ttf'
UNICODE_FONT_PATH = '/home/parthbhavsar/.fonts/Noto_Sans_Gujarati/static/NotoSansGujarati-Medium.ttf'
MARKUP_CLOSER = '[/color]'
FONT_SIZE = '58sp'

logger = logging.getLogger(__name__)

class MukhpathApp(App):

    harvard_kyoto_mode = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.q_current = 1
        self.average_score = 0
        self.mukhpath = mukhpath.open_mp_file('simple.txt')
        self.q_total = len(self.mukhpath)

    def build(self):

        # Create a horizontal box layout
        top_level_layout = BoxLayout(orientation='horizontal')

        # Create three vertical box layouts within the top layout; the middle
        # layout will be used for widgets
        left_panel = BoxLayout(size_hint=(0.2, 1))
        middle_panel = BoxLayout(orientation='vertical')
        right_panel = BoxLayout(size_hint=(0.2, 1))
        top_level_layout.add_widget(left_panel)
        top_level_layout.add_widget(middle_panel)
        top_level_layout.add_widget(right_panel)

        # Mukhpath label
        self.mukhpath_label = Label(text='m&Kpiq', font_size='96sp',
                               font_name=GHANSHYAM_FONT_PATH)
        middle_panel.add_widget(self.mukhpath_label)

        # Score & options panel
        score_panel = BoxLayout(orientation='horizontal')
        self.score_label = Label(text=f'Question {self.q_current}/{self.q_total}, Average: {self.average_score}')
        virama_box_label = Label(text="Implicitly use viramas")
        self.virama_box = CheckBox()

        # Add widgets to the score panel
        score_panel.add_widget(self.score_label)
        score_panel.add_widget(virama_box_label)
        score_panel.add_widget(self.virama_box)
        middle_panel.add_widget(score_panel)

        # Hint box
        self.hint_box = Label(width=200, font_size=FONT_SIZE,
            font_name=GHANSHYAM_FONT_PATH,
            halign='center',
            text_size=(1000,None))
        self.hint_box.text = " aj sK) ain>dn) h[l)..."
        middle_panel.add_widget(self.hint_box)

        # Difference box
        self.difference_box = Label(width=200, font_size=FONT_SIZE,
            halign='center',
            text_size=(1000,None),
            markup=True)
        middle_panel.add_widget(self.difference_box)

        # Transliterated box
        self.transliterated_output = Label(width=200, font_size=FONT_SIZE,
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

        # Control widget
        control_widget = BoxLayout(orientation='horizontal')

        # Previous button
        previous_button = Button(text='Previous')
        previous_button.bind(on_press=self.previous_mp)
        control_widget.add_widget(previous_button)

        # Copy buttons
        copy_button = Button(text='Copy Output')
        copy_input = Button(text='Copy Input')
        copy_button.bind(on_press=self.copy_text)
        copy_input.bind(on_press=self.copy_input)
        control_widget.add_widget(copy_button)
        control_widget.add_widget(copy_input)

        # Font selection
        font_select = DropDown()
        for font in ['GHANSHYAM', 'sarjudas', 'Unicode', 'probolinggo', 'alphabetized-cassette-tapes','DejaVuSans']:
            drop_down = Button(text=font, size_hint_y=None, height=44)
            drop_down.bind(on_press=lambda btn: font_select.select(btn.text))
            font_select.add_widget(drop_down)
        font_select.bind(on_select=self.set_font)
        drop_down = Button(text='Select Font', size_hint_y=None)
        drop_down.bind(on_release=font_select.open)
        control_widget.add_widget(drop_down)

        # Next button
        next_button = Button(text='Next')
        next_button.bind(on_press=self.next_mp)
        control_widget.add_widget(next_button)

        middle_panel.add_widget(control_widget)

        return top_level_layout

    def update_output(self, ascii_text):
        #self.transliterated_output.text = gujhk.ascii_to_guj(ascii_text)
        if self.harvard_kyoto_mode:
            self.transliterated_output.text = harikrishna.ascii_to_harikrishna(ascii_text)
        else:
            self.transliterated_output.text = harikrishna.ascii_to_latin_diacritic(ascii_text)

    def on_text_input(self, instance, value):
        self.update_output(self.text_input.text)

    def copy_text(self, instance):
        Clipboard.copy(self.transliterated_output.text)
        # logger.info('Copied output text to clipboard.')

    def copy_input(self, instance):
        Clipboard.copy(self.text_input.text)

    def set_font(self, instance, font):
        if 'Unicode' in font:
            font = UNICODE_FONT_PATH
        if font in ['probolinggo', 'alphabetized-cassette-tapes','DejaVuSans']:
            self.harvard_kyoto_mode = False
        else:
            self.harvard_kyoto_mode = True
        self.transliterated_output.font_name = font
        self.hint_box.font_name = font
        self.difference_box.font_name = font
        self.mukhpath_label.font_name = font

    def update_difference_box(self, diff_str : str):
        # Set all text to green
        self.difference_box.color = '#00FF00'

        # Escape [ and ] with a backslash
        #diff_str = diff_str.replace('[', '\[').replace(']', '\]')

        markup_str = []
        i = 0

        # while i < len(diff_str):
        #     if diff_str[i] in ['+', '-']:
        #         markup_str.append(diff_str[i])
        #         i += 1
        #         # Add a closer after the letter
        #         markup_str.append(diff_str[i])
        #         markup_str.append(MARKUP_CLOSER)
        #     else:
        #         markup_str.append(diff_str[i])

        #     i += 1
        # Get rid of extra spaces
        markup_str = diff_str.replace('   ', '*').replace(' ','').replace('*',' ')
        colored_list = []

        i = 0
        while i < len(markup_str):
            # If there is a + or -, a character always exist to the right
            if markup_str[i] == '+':
                colored_list.append('[color=ffff00]')
                colored_list.append(markup_str[i+1])
                colored_list.append('[color=00ff00]')
                i += 2
            elif markup_str[i] == mukhpath.NDIFF_RM_CHAR and i+1 < len(markup_str):
                colored_list.append('[color=ff0000]')
                colored_list.append(markup_str[i+1])
                colored_list.append('[color=00ff00]')
                i += 2
            else:
                colored_list.append(markup_str[i])
                i += 1

        # Add markup closing brackets for - and +
        # markup_str = ''.join(markup_str).replace('+','[color=ffff00]').replace('-','[color=ff0000]')
        # i = 0
        # while i < len(markup_str):
        #     if markup_str[i] in ['[color=ffff00]','[color=ff0000]'] and \
        #        i + 2 < len(markup_str):
        #         markup_str = markup_str[:i] + '[color=ffffff]' + markup_str[i:]
        #   i += 1
        markup_str = ''.join(colored_list)
        logger.info('Markup string: ' + markup_str)
        if not self.harvard_kyoto_mode:
            markup_str = harikrishna.ascii_to_latin_diacritic(markup_str)
        self.difference_box.text = markup_str

    def update_score(self, ratio : float):
        self.score_label.text = 'Question {}/{}, Avg. Score: {:.2f}'.format(self.q_current, self.q_total, ratio)

    def get_hint(self) -> str:
        # Return the first three words of the mukhpath
        if self.harvard_kyoto_mode:
            return harikrishna.ascii_to_harikrishna(' '.join(self.mukhpath[self.q_current].split(' ')[0:3]))
        else:
            # Get the first three words of the question
            result = ' '.join(self.mukhpath[self.q_current].split(' ')[0:3])
            # Add latin diacritics
            return harikrishna.ascii_to_latin_diacritic(result)

    def next_mp(self, instance):
        self.q_current = (self.q_current + 1) % len(self.mukhpath)
        # Clear difference box
        self.difference_box.text = ''
        # Update the hint
        self.hint_box.text = self.get_hint()
        # Update the question
        self.score_label.text = 'Question {}/{}, Avg. Score {:.2f}'.format(self.q_current+1, self.q_total, self.average_score)

    def previous_mp(self, instance):
        self.q_current = (self.q_current - 1) % len(self.mukhpath)
        # Clear difference box
        self.difference_box.text = ''
        # Update the hint
        self.hint_box.text = self.get_hint()
        # Update the question
        self.score_label.text = 'Question {}/{}, Avg. Score {:.2f}'.format(self.q_current+1, self.q_total, self.average_score)

    def text_compare(self, instance):
        diff_str, ratio = mukhpath.compare(
                                           self.text_input.text,
                                           self.mukhpath[self.q_current]
        )
        self.update_score(ratio)
        print(diff_str)
        self.update_difference_box(diff_str)
        # self.update_difference_box(harikrishna.ascii_to_harikrishna(''.join(diff_str.replace('   ', '128').replace(' ', '').replace('128', ' '))))

        # def on_text_change(self, instance):
    #     # Update the output label with the text from the TextInput
    #     self.output_label.text = self.text_input.text


if __name__ == '__main__':
    MukhpathApp().run()
