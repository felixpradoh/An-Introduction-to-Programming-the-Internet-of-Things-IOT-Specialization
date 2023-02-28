# Peer-graded Assignment: Assignment 3: Testing Document

## RaspberryPi for the energy-saving and heat-watering system.


1. Testing Components
    - First I checked the Photoresistor in series with a capacitor and read the voltage in the middle point.
    - Read the values with a small script.
    - Second, I found a generic SmartPlug of open source that I can communicate.
    - I created a socket between the RaspberryPi and the SmartPlug
    - I sent some orders of ON/OFF with a python Script.

2. Integration Testing
   
    - I made a script to implement the previous scripts in an infinite loop.
    - When the detected sunlight is above a threshold the SmartPlug is ON, and below is OFF.
    - The script sends the order of scheduling from 00.00h to 07.00h.