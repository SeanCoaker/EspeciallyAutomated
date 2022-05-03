/**
 * @file FireflyController.ino
 * @author Sean Coaker (seancoaker@gmail.com)
 * @brief A file that handles all the parts to firefly synchronisation and communication with the software platform.
 * @version 1.0
 * @date 14-04-2022
 * 
 * @copyright Copyright (c) 2022
 * 
 */

#include "OTAComms.h"
#include "UDPHandler.h"

//! The DNS name of this TinyPICO.
#define DNS "esp3"
//! The clock select pin used by the LoRa module.
#define CS 5
//! The name of the router to connect to.
#define SSID "Seans_Router"
//! The password of the router to connect to.
#define PASSWORD "daefa5eb2f"
//! The port to use for the UDP connection.
#define UDP_PORT 7375
//! The port to use for over-the-air uploads.
#define OTA_PORT 3232

//! An object of OTAComms to provide functionality for over-the-air updates.
OTAComms ota;
//! An instance of Firefly to simulate firefly synchronisation.
Firefly firefly;
//! An object of UDPHandler to provide functionality for UDP communication.
UDPHandler udp;

/**
 * @brief The Arduino setup function. This function initialises the WiFi connection, the UDP connection, the OTA connection, and the Firefly object.
 * 
 */
void setup() {

    Serial.begin(115200);
    firefly.init(200, 3500, 75000, 1000);
    udp.init(SSID, PASSWORD, UDP_PORT, &firefly);
    ota.init(OTA_PORT, DNS);
    ota.begin();

}

/**
 * @brief The Arduino loop function. This function handles requests for over-the-air uploads, UDP messages and running a cycle of the firefly system.
 * 
 */
void loop() {
  
    ota.handle();
    udp.handle();
    firefly.cycle();

}
