#include "LoRaComms.h"

LoRaComms::LoRaComms() {}

void LoRaComms::init(int txPower, int syncWord, uint32_t spiFreq, long frequency, int CS) {

    this->txPower = txPower;
    this->syncWord = syncWord;
    this->spiFreq = spiFreq;
    this->frequency = frequency;
    this->CS = CS;

    LoRa.setTxPower(txPower);
    LoRa.setSyncWord(syncWord);
    LoRa.setSPIFrequency(spiFreq);
    LoRa.setPins(CS);
    while (!LoRa.begin(frequency)) {
        Serial.println(".");
        delay(500);
    }

}

bool LoRaComms::isPacketDetected() {

    int packetSize = LoRa.parsePacket();
    if (packetSize) {
        return true;
    } else {
        return false;
    }

}

void LoRaComms::broadcastMessage(String message) {

    LoRa.beginPacket();
    LoRa.print(message);
    LoRa.endPacket();

}