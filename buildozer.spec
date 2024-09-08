[app]
# (str) Title of your application
title = VideoCompressorApp

# (str) Package name
package.name = videocompressor

# (str) Package domain (needed for Play Store submission)
package.domain = org.example

# (str) Source code where main.py is located (this should fix the error)
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (list) Permissions
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# (str) Application versioning
version = 1.0

# (list) Application requirements
requirements = python3, kivy, ffmpeg

# (str) Presplash of the application
presplash.filename = assets/icons/presplash.png

# (str) Icon of the application
icon.filename = assets/icons/icon.png

# Build API version for Android
android.api = 30

# (str) Min API supported
android.minapi = 21
