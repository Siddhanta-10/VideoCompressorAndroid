from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from ui.home_screen import HomeScreen
from ui.compress_screen import CompressScreen


class VideoCompressorApp(App):
    def build(self):
        # Create the screen manager
        sm = ScreenManager()

        # Add the home screen and compression screen
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(CompressScreen(name='compress'))

        return sm


if __name__ == '__main__':
    VideoCompressorApp().run()
