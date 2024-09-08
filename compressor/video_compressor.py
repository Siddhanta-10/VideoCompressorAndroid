import subprocess
import os

class VideoCompressor:
    def __init__(self, input_file, output_file, bitrate="1M", resolution=None):
        self.input_file = input_file
        self.output_file = output_file
        self.bitrate = bitrate
        self.resolution = resolution

    def compress(self):
        if not os.path.exists(self.input_file):
            raise FileNotFoundError(f"{self.input_file} does not exist.")

        command = ["ffmpeg", "-i", self.input_file, "-b:v", self.bitrate]

        if self.resolution:
            command.extend(["-s", self.resolution])  # Resolution option

        command.append(self.output_file)

        try:
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            return result
        except subprocess.CalledProcessError as e:
            print(f"Error during compression: {e.stderr.decode('utf-8')}")
            raise Exception("Compression failed")
