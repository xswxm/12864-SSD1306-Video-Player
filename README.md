# 12864 SSD1306 Video Player
It is a python script for playing videos on 12864 over SPI sockets
### Modules
Adafruit_GPIO.SPI
Adafruit_SSD1306

### Setting Up
Configure your 128464 by following this tutorial: https://learn.adafruit.com/ssd1306-oled-displays-with-raspberry-pi-and-beaglebone-black/usage?view=all

Install additional modules
```sh
sudo apt-get install python-pip
sudo apt-get install python-pygame
sudo pip install opencv-python
```

Edit the script. Replace the ports to yours
```python
# Ports used for fthe Display. You may have to change them to yours
RST = 25
DC = 24
```

### How to Use
Open System Settings - Keyboard - Shortcuts and add your commands
```sh
# Play BadApple.zip
# sudo python player.py file_path
sudo python player.py BadApple.zip
```

### Convert a video
I provided a m file for matlab for converting videos while you can also convert any videos with opencv

License
----
MIT
