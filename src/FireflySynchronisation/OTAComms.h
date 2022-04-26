/**
 * @file OTAComms.h
 * @author Sean Coaker (seancoaker@gmail.com)
 * @brief A file that handles the over-the-air uploads from the software platform.
 * @version 1.0
 * @date 14-04-2022
 * 
 * @copyright Copyright (c) 2022
 * 
 */

#include <ArduinoOTA.h>

class OTAComms {

private:

    //! The port to be used for over-the-air updates.
    int otaPort;
    //! The hostname to be used for over-the-air updates.
    const char *dnsName;

public:

    /**
     * @brief Construct a new OTAComms object.
     * 
     */
    OTAComms();

    /**
     * @brief Initialises the attributes of this class and configures the callback functions to each stage of the over-the-air update process.
     * 
     * @param otaPort The port to be used for over-the-air updates.
     * @param dnsName The hostname to be used for over-the-air updates.
     */
    void init(int otaPort, const char *dnsName);

    /**
     * @brief Calls for the ArduinoOTA library to begin.
     * 
     */
    void begin();

    /**
     * @brief Calls for the ArduinoOTA library to handle a request for an over-the-air update.
     * 
     */
    void handle();

};