# WashDryWebApp

This is a web based app that will be used with raspberry pi vibration sensors. 

Purpose: 
When you live on a 3rd story apartment, and the washers and dryers are located down in the basement, it can be a pain to walk down all the stairs only to find out that the washer or dryer isn't done yet. It would be nice to have a web app that could tell you if the washer and/or dryer is done yet, before you make the trip. Yes, this project sort of promotes laziness!

Project:
A Raspberry Pi will be setup in the basement, and will have 4 vibration sensors attached to the two downstairs washers, and two dryers. The raspberry pi will monitor vibration to tell if the units are in use or not, and will be open to receiving requests from our web app, to get this information. For now, I am focusing on building the web app. The hardware and programming the raspberry pi will be later state. 

The Web App:
This app will present the current status of each unit in the basement. The user will also have the option of accessing logs for when the washer/dryer units were last used. This app will be programmed using the Flask framework. 

Updates:
6/10/17: setting up directories, templates, and testing web server connection. 

More to come!
