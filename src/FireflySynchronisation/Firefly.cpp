#include "Firefly.h"

Firefly::Firefly() {}

void Firefly::init(unsigned int minBoost, unsigned int maxBoost, unsigned int period, unsigned int syncWindow) {

    this->minBoost = minBoost;
    this->maxBoost = maxBoost;
    this->period = period;
    this->syncWindow = syncWindow;
    this->lora.init(2, 0x28, 16E6, 866E6, 5);
    this->tp.DotStar_SetPixelColor(0,128,0);

}

void Firefly::cycle() {

    unsigned int counter = 0;
    bool flashed = false;
    bool boosted = false;

    // A loop to count to the max of the flash's 'clock'
    while ((counter < this->period) && this->allowedToStart) {

        // Ensures counter is never negative due to negative boosts.
        if (counter < 0) counter = 0;

        /*
        * If a flash packet is detected then the clock of the device is 
        * boosted forwards or backwards by a random value between 500 and 
        * 1000 depending on where in the cycle the clock is. Otherwise the 
        * the clock is checked to see if it is within the 'flash window'
        * where it will either flash the LED if it is within the window
        * or increment the counter if it is not.
        */
        if (this->lora.isPacketDetected()) {
            
            boosted = true;
            this->syncStarted = true;
            this->packetNotDetectedCounter = 0;
            int boost = std::rand() % (this->maxBoost - this->minBoost + 1) + this->minBoost;
            Serial.println("Boost");

            if (counter < this->period / 2) {
                counter -= boost;
            } else {
                counter += boost;
            }
            
            delayMicroseconds(50);
            
        } else {

            // Values given to act as a 'flash window' where devices will flash when they reach it.
            if ((counter >= this->period - this->syncWindow) && (counter <= this->period)) {
                
                this->flashAndSendPacket();
                flashed = true;
                counter = this->period;
                
            } else {
                counter++;
                delayMicroseconds(50);
            } 
        }
      
    }

    if (!boosted && this->syncStarted && this->allowedToStart) {
        Serial.println("Reached");
        packetNotDetectedCounter++;
    }

    /*
     * This is used the check if the 'flash clock' of the device has been boosted past the device's 'flash window'.
     * If it has, then the device will flash the LED without broadcasting a packet to other devices.
     */
    if (!flashed && this->allowedToStart) {
        this->flashWithoutSendingPacket();
    }

    if (this->packetNotDetectedCounter == 2 && this->allowedToStart) {
        synced = true;
    }

}

void Firefly::flashAndSendPacket() {

    tp.DotStar_SetBrightness(128);
    tp.DotStar_Show();
    this->lora.broadcastMessage("FLASH");
    tp.DotStar_SetBrightness(0);
    tp.DotStar_Show();

}

void Firefly::flashWithoutSendingPacket() {

    tp.DotStar_SetBrightness(128);
    tp.DotStar_Show();
    tp.DotStar_SetBrightness(0);
    tp.DotStar_Show();

}

void Firefly::setAllowedToStart(bool isAllowedToStart) {
    this->allowedToStart = isAllowedToStart;
}

bool Firefly::getAllowedToStart() {
    return this->allowedToStart;
}

bool Firefly::isSynced() {
    return this->synced;
}