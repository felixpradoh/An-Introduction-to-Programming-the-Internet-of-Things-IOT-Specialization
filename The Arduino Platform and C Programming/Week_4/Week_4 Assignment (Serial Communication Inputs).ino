/*
Write a program that allows the user to control the LED connected to pin 13 of the Arduino.
When the program is started, the LED should be off.
The user should open the serial monitor to communicate with the Arduino. 
If the user sends the character '1' through the serial monitor then the LED should turn on. If the user sends the character '0' through the serial monitor then the LED should turn off.
*/
// Most of the Arduino Boards have a BUILT-IN LED connected to PIN 13

int status = 0; // Initial status of the LED is off so '0'
void setup() 
  {  
  pinMode(LED_BUILTIN, OUTPUT);  // Initialize the digital pin as an output.  
  Serial.begin(9600);            // Sets the Serial Communication baud_rate
  }

void loop() 
  {
    if (Serial.available() > 0)  // Checks whether data is comming from the serial port  
        {state = Serial.read();  // Reads the data from the serial port  
        }  
    if (status == '0')  
        {digitalWrite(LED_BUILTIN, LOW); // Turn LED OFF 
        }
    if (status == '1')  
        {digitalWrite(LED_BUILTIN, HIGH); // Turn LED ON
        }
    }