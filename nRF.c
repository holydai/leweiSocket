#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>
 
int led_pin = 5;
 
int main ()
{
if (wiringPiSetup() == -1)
{
printf(¡°Setup wiringPi failed!¡±);
return 1;
}
printf(¡°linker_led pin : GPIO%d (wiringPi pin)\n¡±,led_pin);
pinMode(led_pin, OUTPUT); // set mode to output
 
while(1) 
{
digitalWrite(led_pin, 1); // output a high level 
delay(200);
digitalWrite(led_pin, 0); // output a low level 
delay(200);
}
 
return 0;
}