#include "DHT.h"

#define DHTPIN 3      
#define DHTTYPE DHT11  
DHT dht(DHTPIN, DHTTYPE);

#define LDRPIN A0 

void setup() {
    Serial.begin(9600);
    dht.begin();
    pinMode(LDRPIN, INPUT);
}

void loop() {
    if (Serial.available() > 0) {
        char command = Serial.read();
        
        switch (command) {  
            case 'T':
                float t = dht.readTemperature();
                float h = dht.readHumidity();
                int lightRaw = analogRead(LDRPIN);
                int lightPercent = map(lightRaw, 0, 1023, 0, 100);
                
                if (isnan(t) || isnan(h) || isnan(lightPercent)) {
                    Serial.println("ERROR");
                } else {
                    Serial.print(t);
                    Serial.print(";");
                    Serial.print(h);
                    Serial.print(";");
                    Serial.println(lightPercent);
                }
                break;
        }
    }
}
