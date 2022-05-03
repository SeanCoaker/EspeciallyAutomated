#include "OTAComms.h"

OTAComms::OTAComms() {}

void OTAComms::init(int otaPort, const char *dnsName) {

    this->otaPort = otaPort;
    this->dnsName = dnsName;

    ArduinoOTA.setPort(otaPort);
    ArduinoOTA.setHostname(dnsName);

    ArduinoOTA.onStart([]() {
        String type;

        if (ArduinoOTA.getCommand() == U_FLASH) {
            type = "sketch";            
        } else {
            type = "filesystem";
        }

        Serial.println("Start updating" + type);
    })

    .onEnd([]() {
        Serial.println("\nEnd");
    })

    .onProgress([](unsigned int progress, unsigned int total) {
        Serial.printf("Progress: %u%%\r\n", (progress / (total / 100)));
    })

    .onError([](ota_error_t error) {
        Serial.printf("Error[%u]: ", error);

        switch(error) {
            case OTA_AUTH_ERROR:
                Serial.println("Auth Failed");
                break;

            case OTA_BEGIN_ERROR:
                Serial.println("Begin Failed");
                break;

            case OTA_CONNECT_ERROR:
                Serial.println("Connect Failed");
                break;

            case OTA_RECEIVE_ERROR:
                Serial.println("Receive Failed");
                break;

            case OTA_END_ERROR:
                Serial.println("End Failed");
                break;
        }
    });

}

void OTAComms::begin() {

    ArduinoOTA.begin();

}

void OTAComms::handle() {

    ArduinoOTA.handle();

}