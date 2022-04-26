#include "UDPHandler.h"

UDPHandler::UDPHandler() {}

void UDPHandler::init(const char *ssid, const char *pass, unsigned int port, Firefly *firefly) {

    this->ssid = ssid;
    this->password = pass;
    this->port = port;
    this->firefly = firefly;

    Serial.println("Booting...");
    WiFi.mode(WIFI_STA);
    WiFi.begin(ssid, pass);

    while (WiFi.waitForConnectResult() != WL_CONNECTED) {
        Serial.println("Connection Failed. Retrying...");
        delay(3000);
        ESP.restart();
    }

    Serial.println("Ready");
    Serial.print("IP Address: ");
    Serial.println(WiFi.localIP());

    this->udp.begin(port);

}

void UDPHandler::handle() {

    int udpPacketSize = this->udp.parsePacket();
  
    if (udpPacketSize) {
          
        IPAddress remoteIp = this->udp.remoteIP();
        uint16_t remotePort = this->udp.remotePort();

        // read the packet into packetBuffer
        char packet_buffer[255];
        int len = this->udp.read(packet_buffer, 255);
            
        if (len > 0) packet_buffer[len] = 0;

        String packet_string(packet_buffer);

        if (packet_string == "Ping") {

            this->udp.beginPacket(remoteIp, remotePort);
            this->udp.print("Received");
            this->udp.endPacket();
            this->firefly->setAllowedToStart(false);

        } else if (packet_string == "Start") {

            this->udp.beginPacket(remoteIp, remotePort);
            this->udp.print("Started");
            this->udp.endPacket();
            this->firefly->setAllowedToStart(true);

        } else if (packet_string == "Sync") {
            
            if (this->firefly->isSynced() && this->firefly->getAllowedToStart()) {
                this->udp.beginPacket(remoteIp, remotePort);
                this->udp.print("Done");
                this->udp.endPacket();    
            }

        }
    }

}