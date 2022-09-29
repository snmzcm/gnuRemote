# gnuRemote
Simple remote control app for basic needs. 
This app helps you to control your computer and apply your basic needs such as shutting it down or locking the screen.
As long as your desired controller device will remain connected to same network with your computer, app will work. 


### Prerequisites
Python3
 ```
https://www.python.org/downloads/
 ```
 Flask
  ```
 Pip install flask
 --OR--
[ pip install Flask](https://pypi.org/project/Flask/)
  ```
##  Usage

1. Unzip it.
2. Start flasgui.exe 
3. Click on start Remote that will show you a dialog box
4. In the dialog box you can see your computer's internal IP which can be accessed through any desired device to control your computer remotely.
5. Go to shown Ip address in your mobile phone browser and try if it works!


## Adding new features

I will post a well detailed version in the future for how to add if you want to trigger another command. Here is a short brief. You need to write it in pyClasses.py.
You have to call your new feature's function(You just did in pyClasses.py) in app.py under the other commands such as /lockdown . 
Now you have to write a Javascript script for calling the function on the server side.


## License / Lisans

Distributed under GNU General Public License. See `LICENSE` for more information.

## Contact

``` Alicemsonmez98@gmail.com ```

[![LinkedIn][linkedin-shield]][linkedin-url]


[license-shield]: https://img.shields.io/github/license/snmzcm/repo.svg?style=for-the-badge
[license-url]: https://github.com/snmzcm/simpleCenc/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/cem-sönmez-01a58a196/
