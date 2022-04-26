/**
 * @file Firefly.h
 * @author Sean Coaker (seancoaker@gmail.com)
 * @brief This file handles all the inner workings of the firefly simulation system, including running a clock cycle, flashing an LED, and calling the broadcasting and receiving LoRa messages to and from neighbouring TinyPICOs.
 * @version 1.0
 * @date 14-04-2022
 * 
 * @copyright Copyright (c) 2022
 * 
 */

#include <TinyPICO.h>
#include "LoRaComms.h"

class Firefly {

private:

    //! Whether the synchronisation process is allowed to start.
    bool allowedToStart = false;
    //! Has the synchronisation process started?
    bool syncStarted = false;
    //! A counter of the number of clock cycles completed without detecting a LoRa message from a neighbour.
    unsigned int packetNotDetectedCounter = 0;
    //! Whether the firefly has synchronised with its neighbours.
    bool synced = false;
    //! An instance of the TinyPICO helper library to provide configuration of the onboard LED.
    TinyPICO tp = TinyPICO();

    //! The minimum amount to boost the firefly's clock by.
    unsigned int minBoost;
    //! The maximum amount to boost the firefly's clock by.
    unsigned int maxBoost;
    //! The length of the clock cycle.
    unsigned int period;
    //! The size of the window from the end of the clock cycle that can be determined as the firefly being in sync.
    unsigned int syncWindow;
    //! An instance of the LoRaComms class to provide LoRa communication functionality.
    LoRaComms lora;

    /**
     * @brief A private function to flash the LED of the TinyPICO but not broadcast the message.
     * 
     */
    void flashAndSendPacket();

    /**
     * @brief A private function to flash the LED of the TinyPICO and broadcast a message to the neighbouring TinyPICOs.
     * 
     */
    void flashWithoutSendingPacket();

public:

    /**
     * @brief Construct a new Firefly object.
     * 
     */
    Firefly();

    /**
     * @brief Initialise the Firefly object with the necessary clock period, boost range, and sync window.
     * 
     * @param minBoost The minimum amount to boost the firefly's clock by.
     * @param maxBoost The maximum amount to boost the firefly's clock by.
     * @param period The length of the clock cycle.
     * @param syncWindow The size of the window from the end of the clock cycle that can be determined as the firefly being in sync.
     */
    void init(unsigned int minBoost, unsigned int maxBoost, unsigned int period, unsigned int syncWindow);

    /**
     * @brief A function that cycles through the firefly's clock and handles the boosting of the clock when LoRa messages are detected. This function also calls for the flashing functions when the end of the clock cycle is reached.
     * 
     */
    void cycle();

    /**
     * @brief Set the value of the allowedToStart variable.
     * 
     * @param isAllowedToStart Whether the synchronisation process is allowed to start.
     */
    void setAllowedToStart(bool isAllowedToStart);

    /**
     * @brief Get the value of allowedToStart.
     * 
     * @return true if allowed to start, false otherwise.
     */
    bool getAllowedToStart();

    /**
     * @brief Return if the firefly has synchronised with its neighbours or not.
     * 
     * @return true if the firefly has synchronised with its neighbours, false otherwise.
     */
    bool isSynced();

};