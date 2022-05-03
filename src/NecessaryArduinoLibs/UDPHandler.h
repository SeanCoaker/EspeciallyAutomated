/**
 * @file UDPHandler.h
 * @author Sean Coaker (seancoaker@gmail.com)
 * @brief This file handles the incoming and outgoing UDP messages.
 * @version 1.0
 * @date 14-04-2022
 * 
 * @copyright Copyright (c) 2022
 * 
 */

#include <WiFi.h>
#include <WiFiUdp.h>

class UDPHandler {

private:

    //! The name of the router to connect to.
    const char *ssid;
    //! The password of the router to connect to.
    const char *password;
    //! The port to use for the UDP connection.
    unsigned int port;
    //! The WiFiUDP object used to send and receive UDP messages.
    WiFiUDP udp;

public:

    /**
     * @brief Construct a new UDPHandler object.
     * 
     */
    UDPHandler();

    /**
     * @brief Initialises the ESP32 WiFi module and the WiFiUDP object
     * 
     * @param ssid The name of the router to connect to.
     * @param pass The password of the router to connect to.
     * @param port The port to use for the UDP connection.
     */
    void init(const char *ssid, const char *pass, unsigned int port);

    /**
     * @brief Responds to incoming messages with the correct akcnowldegement.
     * 
     */
    void handle();

};
