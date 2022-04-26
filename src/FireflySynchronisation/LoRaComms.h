/**
 * @file LoRaComms.h
 * @author Sean Coaker (seancoaker@gmail.com)
 * @brief This file contains the LoRaComms class that handles the recieving and broadcasting of LoRa messages.
 * @version 1.0
 * @date 14-04-2022
 * 
 * @copyright Copyright (c) 2022
 * 
 */

#include <LoRa.h>

class LoRaComms {

private:

    //! The LoRa module output power.
    int txPower;
    //! The sync word used to ensure that packets can only be read from LoRa modules using the same sync word.
    int syncWord;
    //! The frequency of the SPI communication between the TinyPICO. 
    uint32_t spiFreq;
    //! The frequency of the LoRa communication.
    long frequency;
    //! The select pin connected from the TinyPICO to the LoRa module.
    int CS;

public:

    /**
     * @brief Construct a new LoRa Comms object.
     * 
     */
    LoRaComms();

    /**
     * @brief Initialises the LoRa module and LoRa library with the specified parameters.
     * 
     * @param txPower The LoRa module output power.
     * @param syncWord The sync word used to ensure that packets can only be read from LoRa modules using the same sync word.
     * @param spiFreq The frequency of the SPI communication between the TinyPICO. 
     * @param frequency The frequency of the LoRa communication.
     * @param CS The select pin connected from the TinyPICO to the LoRa module.
     */
    void init(int txPower, int syncWord, uint32_t spiFreq, long frequency, int CS);

    /**
     * @brief Return if a packet is available.
     * 
     * @return true if a message was received, false otherwise.
     */
    bool isPacketDetected();

    /**
     * @brief Broadcast a message containing the specified data.
     * 
     * @param message The message to broadcast.
     */
    void broadcastMessage(String message);

};