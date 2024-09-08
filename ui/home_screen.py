from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')
        self.file_chooser = FileChooserListView()
        layout.add_widget(self.file_chooser)

        self.select_button = Button(text="Select Video", size_hint=(1, 0.2))
        self.select_button.bind(on_press=self.on_file_selected)
        layout.add_widget(self.select_button)

        self.add_widget(layout)

    def on_file_selected(self, instance):
        selected_file = self.file_chooser.selection
        if selected_file:
            # Pass the file path to the next screen
            self.manager.get_screen('compress').set_video(selected_file[0])
            self.manager.current = 'compress'
