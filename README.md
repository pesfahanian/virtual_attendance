# virtual_attendance  

Python script to virtually attend your online classes for you while you sleep! Built with [Selenium](https://selenium-python.readthedocs.io/) 
and the [World Time API](http://worldtimeapi.org/).

This script checks your local time every minute using an API call. If the time for your class has come, it will open a Chrome tab, go to your university online portal,
enters your username and password, logs in, and opens Adobe Connect Web to connect to the class. You can run this script the night before and let it attend your morning class for 
you while you enjoy your sleep!

**Important Note: This is just for fun. Don't use this to actually skip your classes.**

----------------------------------------
## Usage
Install the requirements:
```sh
pip install requirements.txt
```
Run via the command:
```sh
python main.py
```
