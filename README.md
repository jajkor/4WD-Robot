![20231206_102644](https://github.com/jajkor/4WD-Robot/assets/97195875/8f8a64f6-2617-4450-83a5-b9dd52f76100)

<p align="center">A simple four wheel-drive robot written in Python</p>

<p align="center">
<a href="./LICENSE.md"><img src=https://img.shields.io/badge/license-MIT-blue>
<a href="https://github.com/jajkor/4WD-Robot/releases"><img src=https://img.shields.io/badge/release-v1.0.0-green>
</p>

4WD Robot is a simple four wheel drive robot written in `Python` and controlled with a Bluetooth Controller using the `evdev` library. 4WD Robot is equipped with four 12V DC Motors that are connected to an L298N H-Bridge Module, powered by 8 AA Batteries. The L298N is connected to a Raspberry Pi 3 Model B utilizing the `gpiozero` library. External modules connected to the Raspberry Pi include, an HC-S04 Ultrasonic Sensor, a 3.5 Inch touchscreen LCD display, and an ESP32 Cam using a UART USB to FT232 Module. 

The ESP32 Cam is enabled by `MicroPython` which allows the ESP32 to livestream the feed to a web server and be easily integrated with into a `tkinter` GUI application. The GUI displays the video feed from the ESP32 at a resolution of 640x480 while also providing additional photographic functionality via the touch screen display such as screen capture and screen record.

### More: [[Wiki](https://github.com/jajkor/4WD-Robot/wiki)\]
