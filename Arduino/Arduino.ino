#include <SPI.h>
#include <Wire.h>
#include <RHReliableDatagram.h>
#include <RH_RF69.h>

#define DEST_ADDRESS 2

#define MY_ADDRESS 1

// Change to 434.0 or other frequency, must match RX's freq!
#define RF69_FREQ 915.0

#define RFM69_CS      8
#define RFM69_INT     7
#define RFM69_RST     4

#define butt A0
#define LED      13

// Singleton instance of the radio driver
RH_RF69 rf69(RFM69_CS, RFM69_INT);

// Class to manage message delivery and receipt, using the driver declared above
RHReliableDatagram rf69_manager(rf69, MY_ADDRESS);

void setup(){
    delay(500);
    Serial.begin(115200);
    Serial1.begin(115200);

    pinMode(butt, INPUT_PULLUP);

    pinMode(LED, OUTPUT);     
    pinMode(RFM69_RST, OUTPUT);
    digitalWrite(RFM69_RST, LOW);

    Serial.println("Feather RFM69 RX/TX Test!");

    // manual reset
    digitalWrite(RFM69_RST, HIGH);
    delay(10);
    digitalWrite(RFM69_RST, LOW);
    delay(10);
    
    if (!rf69_manager.init()) {
        Serial.println("RFM69 radio init failed");
        while (1);
    }
    Serial.println("RFM69 radio init OK!");
    
    // Defaults after init are 434.0MHz, modulation GFSK_Rb250Fd250, +13dbM (for low power module)
    // No encryption
    if (!rf69.setFrequency(RF69_FREQ)) {
        Serial.println("setFrequency failed");
    }

    // If you are using a high power RF69 eg RFM69HW, you *must* set a Tx power with the
    // ishighpowermodule flag set like this:
    rf69.setTxPower(14, true);
    
    pinMode(LED, OUTPUT);

    Serial.print("RFM69 radio @");  Serial.print((int)RF69_FREQ);  Serial.println(" MHz");


    delay(500);
}

// Dont put this on the stack:
uint8_t buf[RH_RF69_MAX_MESSAGE_LEN];
uint8_t data[] = "OK";

void loop(){
    if (rf69_manager.available()) {
        // Wait for a message addressed to us from the client
        uint8_t len = sizeof(buf);
        uint8_t from;
        if (rf69_manager.recvfromAck(buf, &len, &from)){
            buf[len] = 0;
            Serial.print("got request from : 0x");
            Serial.print(from, HEX);
            Serial.print(": ");
            Serial.println((char*)buf);
            Serial.print("RSSI: "); Serial.println(rf69.lastRssi(), DEC);
            Serial1.println((char*)buf);

            // echo last button       
            //data[0] = ;
            // Send a reply back to the originator client
            if (!rf69_manager.sendtoWait(data, sizeof(data), from))
                Serial.println("sendtoWait failed");
            
            digitalWrite(LED, HIGH);
            digitalWrite(LED, LOW);
        }

    }

    if (Serial1.available()>=1) //change to serial1 when using with raspbery pi
    {
        //Serial.println("Button pressed!");
        
        char radiopacket[10];
        int numByte= Serial.readBytesUntil('\n',radiopacket,10);

        Serial.print(numByte); Serial.println(" bytes");

        Serial.print("Sending "); Serial.println(radiopacket);
        //strlen(radiopacket)
        if (rf69_manager.sendtoWait((uint8_t *)radiopacket, numByte , DEST_ADDRESS)) {
            // Now wait for a reply from the server
            uint8_t len = sizeof(buf);
            uint8_t from;   
            if (rf69_manager.recvfromAckTimeout(buf, &len, 2000, &from)) {
                buf[len] = 0;
                Serial.print("Got reply from #");
                Serial.print(from); Serial.print(": ");
                Serial.println((char*)buf);

                
            } else {
                Serial.println("No reply, is anyone listening?");
            }
        } else {
            Serial.println("sendtoWait failed");
        }
    }


}
