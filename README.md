# 12864 SSD1306 Video Player
It is a python script for playing videos on 12864 over SPI sockets

### Demo
<a href="http://www.youtube.com/watch?feature=player_embedded&v=7MF6DfqhK14
" target="_blank"><img src="http://img.youtube.com/vi/7MF6DfqhK14/0.jpg" 
alt="Bad Apple on 12864 with Python and Raspberry Pi " width="480" height="360" border="10" /></a>

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
