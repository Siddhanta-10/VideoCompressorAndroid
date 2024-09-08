from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.progressbar import ProgressBar
from compressor.video_compressor import VideoCompressor
import threading


class CompressScreen(Screen):
    def __init__(self, **kwargs):
        super(CompressScreen, self).__init__(**kwargs)

        self.layout = BoxLayout(orientation='vertical')

        # Display selected file
        self.video_label = Label(text="Selected Video: None")
        self.layout.add_widget(self.video_label)

        # User input for compression settings
        self.bitrate_input = TextInput(hint_text="Enter Bitrate (e.g., 1M)", size_hint=(1, 0.1))
        self.layout.add_widget(self.bitrate_input)

        self.resolution_input = TextInput(hint_text="Enter Resolution (e.g., 1280x720)", size_hint=(1, 0.1))
        self.layout.add_widget(self.resolution_input)

        self.progress_bar = ProgressBar(max=100, size_hint=(1, 0.1))
        self.layout.add_widget(self.progress_bar)

        # Compress button
        self.compress_button = Button(text="Start Compression", size_hint=(1, 0.2))
        self.compress_button.bind(on_press=self.start_compression)
        self.layout.add_widget(self.compress_button)

        self.add_widget(self.layout)

    def set_video(self, file_path):
        self.video_file = file_path
        self.video_label.text = f"Selected Video: {file_path}"

    def start_compression(self, instance):
        bitrate = self.bitrate_input.text or "1M"
        resolution = self.resolution_input.text or None

        output_file = self.video_file.replace(".mp4", "_compressed.mp4")

        compressor = VideoCompressor(self.video_file, output_file, bitrate, resolution)

        # Run compression in a separate thread to keep the UI responsive
        threading.Thread(target=self.compress_video, args=(compressor,)).start()

    def compress_video(self, compressor):
        try:
            compressor.compress()
            self.progress_bar.value = 100
        except Exception as e:
            self.video_label.text = str(e)
