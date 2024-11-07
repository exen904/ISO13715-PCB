# ISO13715 Macropad

![built macropad](https://github.com/exen904/ISO13715-PCB/blob/main/pictures/built.jpg)

Name derives from DIN ISO 13715 ```Kanten mit unbestimmter Gestalt```. Depending on the layout you choose for the bottom row 13/15 keys, 7 where the regular Alpha cluster would be and ISO should be obvious. 

## BOM
- 15x SOD123 Diodes
- 3x SK-6812 MINI-E
- 2x 2U PCB mounted Stabilizers
- 1x MCU of your choice

For the MCU you have two options. Either XIAO RP2040, or Waveshare RP2040 Zero/0xCB Gemini. Both fit and work, however the pinout is mirrored on either option. I originally designed the PCB for the Xiao, with the MCU facing towards you (not like most split builds with face down MCUs). However, my Proto is built with a RP2040 zero, which has to be flipped on its face. I recommend using IC sockets for the MCU. 


## Case
The current case only supports the HHKB bottom row with 2x 1U keys, the version with the larger blockers is still on my todo. If you cant wait though, feel free to edit the STEP files to your needs. For the diffusor, I chose transparent PETG and for a more unified look, changed the last layer to white.

## Firmware
Another todo, QMK is comming soon(tm). Currently im running a version of KMK created with POG to drive my prototype. I added my files from the POG generated KMK, not sure if this works how intended though. Once the QMK port is ready, I link it here.

### KLE layout options

![Screenshot of KLE](https://github.com/exen904/ISO13715-PCB/blob/main/pictures/kle.jpg)
