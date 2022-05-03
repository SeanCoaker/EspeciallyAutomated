# Especially Automated - User Manual

## Contents

- 1 Welcome
- 2 Quick Start Guide
   - 2.1 Introduction
   - 2.2 Hardware Requirements
   - 2.3 Software Requirements
   - 2.4 Setup Guide
      - 2.4.1 Utilising the software platform
         - 2.4.1.1 Installing the software platform executable
            - duino CLI) 2.4.1.2 Setting up the Arduino Command-Line Interface (Ar-
            - sketch 2.4.1.3 Creating an Especially Automated compatible Arduino
            - sketch for the first time 2.4.1.4 Uploading your Especially Automated compatible
         - 2.4.1.5 Running the software platform for the first time
            - platform 2.4.1.6 Uploading and timing a sketch from the software
         - 2.4.1.7 Saving your timed result
            - eters 2.4.1.8 Viewing charts of saved results against saved param-
      - 2.4.2 Utilising the firefly synchronisation system
         - 2.4.2.1 LoRa module to ESP32 device wiring
         - 2.4.2.2 TinyPICO pinouts
         - 2.4.2.3 RFM95 LoRa module pinouts
         - 2.4.2.4 Configuring the software system
- 3 Troubleshooting
   - 3.1 Software platform
      - 3.1.1 Upload configuration errors
      - 3.1.2 Upload process errors
      - 3.1.3 Save result errors
      - 3.1.4 Load results errors
- 2.1 Upload window on launch of software
- 2.2 Upload dialog during the upload and timing process
- 2.3 Button to save the timing result
- 2.4 Save result dialog
- 2.5 Results screen with matplotlib charts
- 2.6 TinyPICO Pinouts
- 2.7 RFM95 Pinouts


## 1 Welcome

Especially Automated is a tool for the automated uploading of Arduino sketches
wirelessly to development boards that house ESP32 chips. It was designed for use
by developers who are keen to automate the process of uploading and testing their
sketches within an internet-of-things network. However, Especially Automated also
offers features that allow the developer to upload their sketch wirelessly to singular
devices. Especially Automated was designed with versatility in mind to allow for the
uploading and timing of sketches that contain a wide variety of functionalities.
Should the developer follow the software schematic provided within this user
manual, they can develop their sketches such that they can be timed until they
reach a point of convergence. Convergence is determined as a point where the
developer’s devices have completed their task and have all reached a common
state of completeness. For example, this project developed a firefly synchronisation
use case, where the state of convergence was determined to be when all devices
had synchronised with each other. Other examples could include a single device
responding to the Especially Automated application when its connected thermometer
has reached a specified temperature. The theory behind this testing functionality
is that it allows for areas of optimisation to be implemented in a simpler fashion
into embedded system design. The timing system should allow the developer to test
different values for independent variables and then compare the results to identify
the optimal parameters for performing the desired task.
Following the timing of convergence, Especially Automated offers the function-
ality to allow the developer to save their results and what parameters were used
within the sketch to a log file. This log file can be loaded later on to allow the de-
veloper to compare the results of their experiments in scatter graphs. Each scatter
graph compares a single parameter against the results received, which is hoped to
provide the developer with a clear insight into which independent variable provides
the largest variance in results. Ultimately, this aids the developer in identifying the
optimal parameters for their task.
The remainder of this chapter will include a quick start guide to allow the user to
get started with the software platform. Following this will be a more in depth user
guide that will provide a more detailed explanation of how to set up the software
platform and how to utilise its full functionality. Finally, a section will be provided that
explains how the developer can build on top of this project’s firefly synchronisation
use case. The firefly synchronisation system included within this project will hopefully
provide a basis for the advancement of synchronisation technology within embedded
systems networks.


**Next Steps:**

Excited to get started?
Head to section 2 for the Quick Start Guide.

## 2 Quick Start Guide

### 2.1 Introduction

Especially Automated is a software platform designed to allow Arduino developers
to upload sketches to batches of ESP32 devices wirelessly and optionally time the
convergence of those devices. Convergence in this context is defined as a state in
which the developer’s devices have completed their task. For example, a cluster of
ESP32 devices might be seen as converged once they have all synchronised with
each other, or once they have all completed a start-up script and woken from a deep
sleep state. The idea for developing this platform was stumbled upon when the
developer noticed an inefficiency when attempting to test their firefly synchronisation
code on a network of decentralised ESP32 devices, and wanted to provide a tool that
would speed up the process of uploading to and testing a batch of ESP32 devices to
help facilitate the advancements of embedded systems.
The following section is a quick start guide aimed at instructing the user how to
set up their Especially Automated environment and begin using it for the purposes
of uploading sketches to their ESP32 devices as well as testing them.

### 2.2 Hardware Requirements

- At least one ESP32 device.
- Access to an internet connection to install required tools.
- A WiFi router to allow for wireless sketch uploads.
- USB Cable to connect your ESP32 device to your computer system for initial
    upload of compatible code.
- A computer system running Linux or Windows.
- (Optional) A MicroUSB compatible wall socket to power the ESP32 devices
    from a mains supply.
- (Optional) LoRa module for use in the firefly synchronisation system.


### 2.3 Software Requirements

- Linux or Windows operating system. Our system has been tested on Ubuntu
    22.04 and Windows 11.
- A text editor to create Arduino sketches.
- A command line interface for installing and configuring required tools.

### 2.4 Setup Guide

#### 2.4.1 Utilising the software platform

##### 2.4.1.1 Installing the software platform executable

To begin, please download the software here. The directory structure contains
an ’src’ directory for developers who wish to edit the source code under the MIT
copyright license, and two further directories, ’Windows’ and ’Linux’, each containing
the relevant files needed to launch the Especially Automated software platform on
their respective operating systems.

**Extra step for Linux users**
To utilise Especially Automated on Linux, you will also need to execute this line
from your terminal.

```
sudo apt-get install'^libxcb.*-dev'
```
**2.4.1.2 Setting up the Arduino Command-Line Interface (Arduino CLI)**

The use of the Especially Automated software platform requires the installation and
configuration of the Arduino Command-Line Interface (Arduino CLI) to provide the
functionality of compiling Arduino sketches into binary files. The following step-by-
step guide will lead you through the set up process of the Arduino CLI for use with
the software platform.

1. Download and install the latest version of Arduino CLI for your system here.

2. Ensure that the directory containing arduino-cli is added to your system’s envi-
roment variables. Running the following command in your selected terminal
will confirm whether you have done this correctly or not.

```
arduino-cli version
```

3. Run the following command in your preferred terminal to create a config file
for Arduino CLI.


```
arduino-cli config init
```

4. Within that config file, replace lines 1 and 2 with the following.

```
board_manager:
    additional_urls:
        - https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
```

5. In the same config file, set ’enable_unsafe_install’ to true if you intend to install
Arduino libraries from GitHub.

6. Execute the following within your terminal.

```
arduino-cli core update-index
arduino-cli board listall
arduino-cli core install esp32:esp
```

**2.4.1.3 Creating an Especially Automated compatible Arduino sketch**

To allow the Especially Automated software platform to successfully communicate
with the ESP32 devices and to successfully upload Arduino sketches to them wire-
lessly on demand, the following schematic should be followed. Please note that
extra steps are required to allow for a functioning timing feature. These steps will be
included with an ’optional’ prefix.

**Over-the-air upload handling**
To allow your ESP devices to continually identify and allow the wireless flashing
of Arduino sketches, it is crucial that you implement the pre-developed code included
with this project. That code can be found within the following files EspeciallyAu-
tomated/src/NecessaryArduinoLibs/OTAComms.h and OTAComms.cpp, and they
should be copied into the directory of the Arduino sketch that you wish to upload.
Following that, the following steps need to take place to ensure that the files above
are configured and called correctly.

1. Include the following code in your setup() function, replacing ’OTA_PORT’ with
the port you intend to use for the transferral of Arduino sketches over-the-air.

```
ota.init(OTA_PORT, DNS);
ota.begin();
```

2. Include the following code in your loop() function, allowing for your device to
keep checking for over-the-air upload requests.

```
ota.handle();
```

**UDP message handling**
To allow the ESP32 devices to be pinged and to allow their states to be checked
by the software platform, you will need to include the files EspeciallyAutomated/src
/NecessaryArduinoLibs/UDPHandler.h and UDPHandler.cpp within the same direc-
tory as your Arduino sketch. When this is complete, you can follow these steps to
implement code which configures the UDPHandler class and checks for incoming
UDP messages.

1. (Optional) If you are wanting to use the software platform’s timing feature,
within the handle() function of UDPHandler.cpp, replace the comment in the
code below with the code that you wish to be carried out when the device
starts.

```
} else if (packet_string == "Start") {
    this ->udp.beginPacket(remoteIp, remotePort);
    this ->udp.print("Started");
    this ->udp.endPacket();

    // Include code to start the sketch.

}
```

2. (Optional) If you are wanting to use the software platform’s timing feature,
within the handle() function of UDPHandler.cpp, replace the commented if
condition in the code below with the code that you wish to be carried out when
the device has converged.

```
} else if (packet_string == "Sync") {

    //if (condition) {

        this ->udp.beginPacket(remoteIp, remotePort);
        this ->udp.print("Done");
        this ->udp.endPacket();

    //}

}
```

3. Add the following line of code into the preamble of your sketch .ino file. This
define directive is changed with the name of the ESP32 device set in the
Especially Automated software platform later on. Thus, each ESP32 device
will be assigned their own individual name and DNS. Replace "esp1" below with
a standard name for an ESP32 device. The DNS of this device will become
name-you-assign.local. So for the example provided below, the DNS name of
the ESP32 device would be esp1.local.

```
#define DNS "esp1"
```

Make sure to assign a different DNS string for each ESP32 device you are
uploading to and remember the names you set. You will need these DNS names
to be able to upload the sketches from the Especially Automated software
platform later on.

4. Include the following code in your setup() function, replacing ’SSID’ with the
SSID of the router you will be using to upload the sketches, ’PASSWORD’ with
the password needed to connect to that router, and ’UDP_PORT’ with your
desired port for UDP communication between the software platform and ESP
device(s).

```
udp.init(SSID, PASSWORD, UDP_PORT);
```

5. Include the following code in your loop() function, allowing for your device to
keep checking for over-the-air upload requests.

```
ota.handle();
```

**2.4.1.4 Uploading your Especially Automated compatible sketch for the first time**

To ensure that your ESP32 devices function correctly with the Especially Automated
software platform, you will need to upload the previously configured Especially
Automated compatible Arduino sketch to your ESP32 devices using a conventional
method. A conventional method for uploading the sketch for the first time includes
the use of either the Arduino IDE or the Arduino-CLI which you should have installed
earlier. As you are aiming to upload sketches to a batch of ESP32 devices, the
assumption can be made that you have some previous experience of uploading
sketches to individual devices using either Arduino IDE or Arduino-CLI. However, this
section will still include instructions to upload the sketch using these tools just in
case they are needed. Remember, before uploading the sketch to each device, you
need to set the desired DNS name for the device being uploaded to. You will use these
DNS names to communicate with the devices through the Especially Automated
software platform in future.

**Arduino IDE**
Please open the sketch to be uploaded within the Arduino IDE and repeat the
instructions below for each ESP32 device.

1. Connect the ESP32 device to your computer system.

2. Set the #define DNS value for the ESP32 device to be uploaded to within the
sketch code.

3. Click Tools -> Port and select the port name of the ESP32 device.

4.Select Tools -> Board and select the relevant development board to the one
you are using from the list of ESP32 device boards.

5. Click the upload button.

**Arduino-CLI**

1. Connect the ESP32 device to your computer system.

2. Set the #define DNS value for the ESP32 device to be uploaded to within the
sketch code.

3. Identify the port of the ESP32 device you wish to upload to by running the
following command in your preferred terminal.

```
arduino-cli board list
```

4. Compile the sketch in the terminal using the command below.

```
arduino-cli compile --fqbn esp32:esp32:esp32 path-to-sketch
```

5. Upload the sketch to the desired ESP32 device with the following terminal command.

```
arduino-cli upload -p port-of-device --fqbn esp32:esp32:esp
path-to-sketch-bin-file
```

##### 2.4.1.5 Running the software platform for the first time

**Windows**
To open the Especially Automated software platform for the first time on Windows,
please follow the steps below in order:

1. Locate the EspeciallyAutomated directory that you should have installed as
per the instructions in section 2.4.1.1.

2. Within this directory, open one of the ’Windows’ or ’Linux’ directories that match
the operating system of your computer system.

3. You should now see an executable file for EspeciallyAutomated. Double click the file to open it.

**Linux**
It should be noted that a particular bug was identified when testing the soft-
ware platform where Arduino-CLI is not executed correctly when opening the Linux
executable of Especially Automated from the file explorer. The same issue was
not encountered when running the executable file from the terminal, so the current
assumption is that permission errors were causing this bug. But for now, please
follow the steps listed below to run Especially Automated on Linux.

1. Open your preferred terminal software.

2. Navigate to the EspeciallyAutomated/Linux/ directory using the following ter-
minal command.

```
cd directory-containing-your-especially-automated-folder/EspeciallyAutomated/Linux
```

3. Now that you are within the Linux directory of your Especially Automated
download, you can run the following terminal command to open the Linux
executable file.

```
./EspeciallyAutomated
```

**Please Note:** Should any further libraries be missing from your system that are
required for the executing of the Especially Automated software. Attempting to open
Especially Automated from the terminal will identify the missing libraries. Those
libraries can then be installed with simple Google search of how to install those
missing libraries on your distribution of Linux.

**2.4.1.6 Uploading and timing a sketch from the software platform**

Upon completing the steps listed so far, you should now see the window in figure
2.1 on your screen. The following section details the necessary steps that must
be followed to upload a sketch to your device(s) and have the convergence of your
device(s) timed if desired. The number of each step corresponds to a number
displayed on the upload window in figure 2.1. Optional steps will be prefixed with the
’(Optional)’ flag.


Figure 2.1: A screenshot of the upload window which is displayed when opening the
software platform.

1. Enter the name of the ESP device to be uploaded to. This value will replace the
#define DNS directive in the sketch file. Therefore, the DNS of the device being
uploaded to will become ESP-Name.local, with ESP-Name being replaced with
the string you enter in this text field.

2. Enter the current DNS of the ESP device that you wish to upload the sketch to.

3. (Optional) Remove the record of an ESP to reduce the number of devices to
upload to. The first record can not be removed.

4. (Optional) Add the record of an ESP device to increase the number of devices
to upload to.

5. Include the IP address of the computer system you are running Especially
Automated from.

6. Enter the UDP port to be used to send and receive messages to and from the
software platform and the ESP devices.

7. Enter the port to use to upload the sketch to the devices over-the-air. This port
should also have been declared in your sketch file.

8. Select the sketch to be uploaded to the ESP devices. Remember that the
selected sketch should follow the schematic set out in section 2.4.1.3.

9. (Optional) Set whether the software platform should time the convergence of
your device(s) or not.

10. (Optional) Set whether the software platform should provide a verbose output
during the upload and timing process.

11. Click the start button to begin the upload and timing process.

Following the click of the start button, the data that had been input is used to
carry out the uploading of the chosen sketch to the specified ESP device(s). Figure
2.2 displays an example of the upload dialog and includes numbered pointers to
import aspects of the user interface for the process of uploading and timing your
sketches. Descriptions of those pointers can be viewed below Figure 2.2.

Figure 2.2: A screenshot of an upload dialog that is displayed when an upload and
timing process is being carried out.

1. This text box is used to display the progress of the uploading and timing of
sketches throughout. Setting the verbose output checkbox in the main upload
window would allow for a verbose output to be displayed within this text box.

2. The progress bar and label display the progress of the whole upload and timing
task, and a message describing what process is currently being carried out
respectively.

3. This label stores the timer that counts in seconds how long the devices take to
converge.

4. A button box is displayed here containing a cancel button and a save button.
The cancel button can be used to cancel the current process that is taking
place during the upload. The save button becomes enabled once the timing
process has complete, allowing the user to save their result to a log file along
with details on parameters used within their sketch.

##### 2.4.1.7 Saving your timed result

If you followed the instructions in section 2.4.1.6 and selected to have the conver-
gence of your device(s) timed upon the completion of the uploading of your chosen
sketch, then you will receive the option to save your result in a specified log file when
the timing process is complete. To begin the process of saving your result, click the
save button marked in figure 2.3 below.

Figure 2.3: A screenshot of the upload dialog window with the save button marked
for saving the result of the timing process.

Following the click of the save button in figure 2.3, another dialog is displayed
that will allow the saving of the timed result and any details on the parameters used
in the uploaded sketch to a user specified log file. That dialog can be seen in figure
2.4 below. Accompanying the figure will be a set of instructions for the tasks that
need to be carried out to ensure that your data and result are stored correctly.

Figure 2.4: A screenshot of the save result dialog.

1. This label displays the result of the upload process. Please confirm that you
are content with the result received before continuing with the saving process.

2. Using the button containing a directory icon, please select a .txt file to save
your result and desired parameters to. The file being saved to should either be
empty or should be in the following format:
PARAMETER:VALUE,PARAMETER:VALUE,RESULT:VALUE

3. For each parameter record to be saved, please assign a name for the parameter
within this text box. Your parameter records to be saved should follow the
same order as how the parameters are saved within the log file. For example,
if your log file is in the following format:
PERIOD:10,NUM DEVICES:3,RESULT:
then you should be trying to save two parameter records, one for the ’period’
parameter, and one for the ’num devices’ parameter. Parameter names are
also case insensitive and are capitalised before being saved to the log file. You
must avoid using ’result’ as a name for a parameter to be saved, as this will
render your log file unusable by the software platform.

4. Following the name of the parameter within each parameter record, you should
include a numerical value for the value that should be assigned to that parame-
ter.

5. (Optional) You can use this button to remove a parameter record should you
wish to save less parameters.

6. (Optional) You can use this button to add a parameter record should you wish
to save more parameters.

7. This button box contains a ’Cancel’ button to allow you to leave the save result
form without submitting data to the log file. It also contains a ’Save’ button
which ensures that the parameters you are attempting to save match the format
of the log file you are trying to save to. It also ensures that a ’RESULT’ parameter
is identified in each line within the log file.

Following the saving of your result and details of your parameters, the log file
can be accessed again by the loading feature of the software platform later. Details
on how to use the loading feature can be found in section 2.4.1.8.
Should you experience error messages during the saving of your data to your log
file, please refer to the troubleshooting details found in section 3.

**2.4.1.8 Viewing charts of saved results against saved parameters**

The load feature of the software platform can allow the user to render matplotlib
charts of the results they have saved within their specified log file, against the param-
eters that were also saved. The testing of the firefly synchronisation system bundled
with this software was carried out using this feature, to develop an understanding of
the optimal parameters for demonstration purposes.
When loading charts from a log file, the system identifies each parameter that
has been saved along with each result. It then creates a chart for each parameter,
comparing the values of the parameter against the result values saved within the
file. Figure 2.5 demonstrates this.

Following figure 2.5 is a list of details that describe the labels contained within the
image. Those labels point towards a feature of the chart viewing function which have
been implemented to benefit the experience of the user when using the software
platform.

Figure 2.5: A screenshot of the results screen when a log file has been selected and
charts are displayed for the data within that file.

1. To arrive at this feature within the software platform, the results tab must be
clicked from the main window.

2. Clicking the button containing the directory icon opens a window that allows
the user to select a log file to view the charts of. When a log file is selected, data
is automatically loaded into the platform and charts are displayed comparing
parameter values against results received.

3. Each chart contains a matplotlib toolbar that allows the user to pan the chart,
zoom in and out of the chart, and provides other useful features such as
allowing filtering the saving of charts as images.

4. This denotes a scroll area which is used to display the number of charts that
the user wishes to view. In this instance, the charts of two parameters are
selected and therefore only those two charts are displayed within the scroll
area.

5. A list of the parameters loaded from the log file is displayed here. The user can
select and deselect the checkbox of a parameter to show and hide the chart of
the parameter.

6. This combo box stores a list of all parameters as well as two extra options, ’all’
and ’none’. The selection of a singular parameter from this combo box allows
for only the chart of the selected parameter to be displayed. The check boxes
at 5 are updated to reflect this selection. Selecting ’all’ or ’none’ allow the all
charts to be displayed or no charts to be displayed respectively. Again, the
check boxes at 5 are updated to reflect this selection.

#### 2.4.2 Utilising the firefly synchronisation system

This section outlines the relevant details required to correctly setup and configure the
firefly synchronisation system provided with this project. The firefly synchronisation
system was developed as a use case for the Especially Automated software platform,
as well as being developed to demonstrate how a decentralised network of embedded
systems can synchronise its nodes for use in creating more robust communication
networks. This section will break down the setup of the firefly synchronisation
system into the following parts; wiring between the LoRa module and ESP32 device,
illustrations of the pinouts for each device, and instructions for configuring the
software systems for the nodes. Configuring the software systems for the nodes
itself will be detailed in parts, with descriptions of how to configure the behaviour
of the libraries included within the software system, and how some libraries can be
adjusted to attempt to improve the efficiency of the software systems.

##### 2.4.2.1 LoRa module to ESP32 device wiring

To allow the firefly synchronisation system included with this project to function
correctly, you first need to wire the correct pins between the ESP32 devices and the
LoRa modules. The specific hardware used within this project was a Hope RFM
(Semtech SX1276) LoRa module and a TinyPICO (ESP32) development board. Using
this hardware and the following wiring configuration, the project was able to include
a fully functional firefly synchronisation network with use of the developed software
system included. Please see below the wiring used to create each node of the
network. Please note that the following wiring configuration is for the aforementioned
hardware included in this project’s firefly synchronisation solution. Although the
wiring should be the same for ESP32 devices, it may differ on some boards.

- TinyPICO 3.3V Pin (3V3) —> RFM95 3.3V Pin (3.3V).
- TinyPICO Ground Pin (G) —> RFM95 Ground Pin (GND).
- TinyPICO SS Pin (5) —> RFM95 NSS Pin (NSS).
- TinyPICO SCK Pin (18) —> RFM95 SCK Pin (SCK).
- TinyPICO MI Pin (19) —> RFM95 MISO Pin (MISO).
- TinyPICO MO Pin (23) —> RFM95 MOSI Pin (MOSI).


##### 2.4.2.2 TinyPICO pinouts

Figure 2.6: An illustration of the TinyPICO pinouts provided by [1]

##### 2.4.2.3 RFM95 LoRa module pinouts

Figure 2.7: An illustration of the RFM95 LoRa module pinouts provided by [2]

##### 2.4.2.4 Configuring the software system

For those users who wish to adjust the firefly synchronisation system provided for
experimentation purposes or for the purpose of attempting to improve the efficiency
and performance of the system, this section is included. It includes relevant infor-
mation on how the system is initialised, what values can be changed to alter the
behaviour of the system, and how the inner workings of the provided firefly library
can be experimented with.

**Initialising the firefly library**

The sketch included within this software system creates an instance of the firefly
class initially using the empty constructor. Following this, the setup() function of the
sketch includes a line of code that runs the init() function for that firefly instance. The
init() function takes 4 arguments, ’minBoost’, ’maxBoost’, ’period’, and ’syncWindow’.
The description of those arguments can be seen below:

- minBoost - The minimum possible random value that can be used to boost the
    value of the firefly’s clock forwards or backwards.
- maxBoost - The maximum possible random value that can be used to boost
    the value of the firefly’s clock forwards or backwards.
- period - The number of iterations to run through. In effect, the firefly’s clock
    length.
- syncWindow - Defines how close the firefly’s clock should be to the value of
    the period for the synchronised state to be identified.

Further information of the software system can be found in the firefly synchroni-
sation system’s documentation provided with the submission of this document.
Significant differences in the efficiency and performance of the firefly synchro-
nisation system can be attained with adjustments to the minBoost, maxBoost and
period values included within the init() function of the firefly library. Changes made to
the minBoost and maxBoost values can speed up or slow down how quickly nodes
of the network synchronise with each other. Adjustments made to the period value
can have the same effect whilst causing each node to flash its LED more or less
frequently, depending on the change to the value of the period. The call of the init()
function to initialise the firefly object can be seen below:

```
Firefly firefly;
firefly.init(minBoost, maxBoost, period, syncWindow);
```

**Changes to the firefly library**

Also included with the firefly synchronisation software system is the Firefly.cpp
and Firefly.h files which make up the firefly library. These files are responsible for
dealing with the clock cycle and LED flashing of each node. Changes can be made

within this file to alter the behaviour of the nodes within each clock cycle. The
possible adjustments that will be focused on in this section will be listed below,
along with a body of text describing what the relevant code provides within the file
and what changes can be made to effect the whole firefly system.

- Random boost values:
    Random values between the minBoost and maxBoost values of the firefly class
    are used to boost the clock of the firefly forwards and backwards. This was
    developed to avoid an issue where nodes boosting by identical amounts was
    causing the nodes to remain in an asynchronous state. The code for this can
    be found in the cycle() function of the Firefly.cpp file and can also be seen
    below:

        ```
        int boost = std::rand() % (this->maxBoost -
                this->minBoost + 1) + this->minBoost;

        if (counter < this ->period / 2) {
            counter -= boost;
        } else {
            counter += boost;
        }
        ```

    Experimentation could take place with this block of code to attempt to re-
    move the need for random boost values. This could create a more efficient
    and more predictable synchronisation system, potentially improving the ef-
    fectiveness of this firefly synchronisation system for robustness use cases in
    communication networks.

- Delays after each change to the clock cycle:
    The current firefly software system blocks the system by 50 microseconds
    each time the firefly clock is incremented by 1 or each time the clock is boosted.
    This code could be adjusted in an attempt to change the length of time between
    each flash of the ESP32 device’s LED. However, development within this project
    identified that changes to these delays made a minuscule difference to the
    time between LED flashes and instead noticed that larger changes could be
    made with the change to the period set for each firefly. Further information on
    changing the period of the fireflies can be found in the previous paragraph.
    The line of code that blocks the system for a specific number of microseconds
    can be seen below:

        ```
        delayMicroseconds(50);
        ```

- Synchronisation detection:
    The final recommended feature to be experimented with is the synchronisation
    detection feature included in the cycle() function of the Firefly.cpp file. The
    current system identifies synchronisation being completed when two passes of
    the clock cycle is made without a LoRa message being detected by a neighbour-
    ing node. Synchronisation detection only begins when the first LoRa message
    has been received by a neighbouring node. Therefore, lone nodes that do not
    detect neighbouring LoRa messages cannot be classed as synchronised with
    the network in this current system. The code for synchronisation detection can
    be viewed below:

        ```
        if (!boosted && this ->syncStarted && this ->allowedToStart) {
            packetNotDetectedCounter++;
        }

        if ( this ->packetNotDetectedCounter == 2
                && this ->allowedToStart) {
            synced = true;
        }
        ```

    The code listing above firstly runs a check to see if the firefly clock has not been boosted due to a received LoRa message, a check to see if synchronisation has started where an initial LoRa message had previously been detected, and a check to see if the synchronisation system is allowed to start (it is only allowed to start when a start UDP message is received from the Especially Automated software platform). If all of these checks hold true then the packetNotDetectedCounter is incremented. In the instance that this counter reaches a value of 2, the system is deemed as synchronised and a message can be returned to the software platform stating that this particular node has synchronised with its neighbours.

Experimentation here could include work to reset the counter each time a
message is detected. This ensures that the node’s synchronisation progress
is reset when more neighbours are introduced to the network after the syn-
chronisation process has begun. Other changes could involve the counter
needing to be higher or lower numbers to allow the system to be identified as
synchronised, depending on the use case of the firefly syncrhonisation system.


## 3 Troubleshooting

The following chapter includes troubleshooting details for both the Especially Automated software platform and the firefly synchronisation system.

### 3.1 Software platform

This section includes all the relevant troubleshooting information for the various errors that can be experienced throughout the use of the software platform. Troubleshooting for the software platform will be split into sub sections for each feature of the software to allow the user to be able to quickly identify the troubleshooting steps for the particular issue they are facing.

#### 3.1.1 Upload configuration errors

- **"Field must not be empty."**
    The user must ensure that a field within the main upload window cannot be left blank when attempting to upload a sketch to ESP32 devices. Please ensure that all fields are filled before attempting to start the upload process.

#### 3.1.2 Upload process errors

- **"Pinging ESP_IP_Address Failed"**
This states that a message has been sent to the specified ESP device’s IP address, but an acknowledgement has not been received. The following troubleshooting steps can be followed to attempt to resolve this.

   - Make sure that the device you are trying to ping is powered on.
   - Ensure that you are connected to the same router as the ESP devices.
   - Check that the IP address you are attempting to ping is the correct IP address.
   - Make sure that code to respond to ping messages are included within the sketch uploaded to your ESP devices. Further information on how to create Especially Automated compatible Arduino sketches can be seen in section 2.4.1.3.
   - Attempts to ping the ESP device may have reached the exceeded amount, try uploading again.

- **"Sketch Upload to ESP_Name - ESP_IP_Address Failed"**
This states that the process of uploading the sketch to the specified ESP device has failed. The following troubleshooting steps can be followed to attempt to resolve this.

   - Make sure that the device you are trying to upload to is powered on.
   - Ensure that you are connected to the same router as the ESP devices.
   - Check that the IP address of the device you are attempting to upload the sketch to is the correct IP address.
   - Make sure that code to respond to over-the-air upload requests are included within the sketch uploaded to your ESP devices. Further information on how to create Especially Automated compatible Arduino sketches can be seen in section 2.4.1.3.
   - Attempts to upload the sketch to the ESP device may have reached the exceeded amount, try uploading again.
    
- **"Starting ESP_Name - ESP_IP_Address Failed"**
The software platform has failed in its attempts to start the coding system within the sketch that has been uploaded to the ESP device(s). The following troubleshooting steps can be followed to attempt to resolve this.

   - Make sure that the device you are trying to start is powered on.
   - Ensure that you are connected to the same router as the ESP devices.
   - Check that the IP address of the device you are attempting to start is the correct IP address.
   - Make sure that code to respond to start messages are included within the sketch uploaded to your ESP devices. Further information on how to create Especially Automated compatible Arduino sketches can be seen in section 2.4.1.3.
   - Ensure that the name of the ESP device to start matches the text prefixes the .local of the device’s IP address if a DNS name is being used.
   - Attempts to start the ESP device may have reached the exceeded amount, try uploading again.
    
- **Convergence timing not concluding**
This issue is caused when a "Done" message is not received by the software platform from each ESP device being timed. The following troubleshooting steps can be followed to attempt to resolve this.

   - Make sure that all ESP devices are powered on.
   - Ensure that you are connected to the same router as the ESP devices.
   - Check that the IP addresses of all the devices you are trying to communicate with are correct.
   - Make sure that code to respond to convergence messages are included within the sketch uploaded to your ESP devices. Further information on how to   create Especially Automated compatible Arduino sketches can be seen in section 2.4.1.3.
   - Check your uploaded sketch for bugs that stops the system from completing and ultimately sending a "Done" message back to the software platform.

#### 3.1.3 Save result errors

- **"ERROR: Path must not be empty."**
    This error is displayed when a log file is not selected to save the result and parameters to. Please ensure that a log file is selected.
- **"Field must not be empty."**
    Displayed when a parameter name or parameter value field have been left blank, this error can be fixed by ensuring that no empty fields are visible when attempting to save a result.
- **"Number of parameters do not match length of line n."**
    This error is displayed when the number of parameters you are attempting to save along with the result does not match the number of parameters saved at line n in the log file. Avoid this issue by ensuring all lines of the file store the same parameters and that those parameters are matched in the data you are attempting to save.
- **"Param not in log file, line n."**
    Displayed when the order of parameters being saved does not match the order of parameters in line n of the log file, this error can be fixed by ensuring that the order of parameters in all lines of the log file match each other, and that the order of the parameters being saved matches the order of parameters in the log file.
- **"Result not found in line n."**
    This error is displayed when a line in the log file being saved to does not contain ’RESULT’ as its final parameter. This can be fixed by either deleting this line or by manually adding a ’RESULT’ parameter and its corresponding value to the end of line n.


#### 3.1.4 Load results errors

- **"File is empty."**
    Please ensure that the log file you are trying to view the charts of is not empty.
- **"RESULT parameter should appear last on Line n."**
    This error is displayed when the last parameter of line n is not ’RESULT’ in the log file. Fix this issue by either deleting line n or by setting the last parameter to be ’RESULT’ and its corresponding value.
- **"Number of parameters in Line n does not match Line 1."**
    This error can be solved by ensuring that the number of parameters in line n matches the number of parameters contained in line 1 of the log file.
- **"A parameter in Line n does not match the parameters in Line 1."**
    Displayed when a parameter in line n does not match the parameter at the same index in line 1, this error can be solved by ensuring that all parameters in line n match all parameters in line 1.
- **"Value of a parameter in Line n is not a float."**
    This error can be solved by ensuring that all values associated with all parameters within the selected log file are in numerical form.


## Bibliography

[1] “Tinypico.” [Online]. Available: https://www.tinypico.com/

[2] “Rfm95w feature the loratm long range model.” [Online]. Available: https:
//www.hoperf.com/modules/lora/RFM95.html
