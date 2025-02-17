# ISO13715 Macropad

![built macropad](https://github.com/exen904/ISO13715-PCB/blob/main/pictures/built.jpeg)

Name derives from DIN ISO 13715 ```Kanten mit unbestimmter Gestalt```. Depending on the layout you choose for the bottom row 13/15 keys, 7 where the regular Alpha cluster would be and ISO should be obvious. 

Huge shoutout to PCBway, who sponsored the run of the matte black PCB I used in the build guide. No strings attached here, if you want a matte black PCB, thats the way to go.

## PCB
You can find the Gerber files for ordering your own PCB in the `PCB\production` folder. For service I can absolutely recommend PCBway, who also reachead out to me and sponsored a run of my prototype PCBs with the matte black and yellow silkscreen option. 

![PCBway PCB](https://github.com/exen904/ISO13715-PCB/blob/main/pictures/pcb.jpg)

## BOM
- 15x SOD123 Diodes
- 3x SK-6812 MINI-E
- 2x 2U PCB mounted Stabilizers
- 1x MCU of your choice
- 8x 3x3mm magnets for the case
- 4-6x M2x3 heat inserts (4 should be more than fine)
- 4-6x M2x4 screws

For the MCU you have two options. Either XIAO RP2040, or Waveshare RP2040 Zero/0xCB Gemini. Both fit and work, however the pinout is mirrored on either option. I originally designed the PCB for the Xiao, with the MCU facing towards you (not like most split builds with face down MCUs). However, my Proto is built with a RP2040 zero, which has to be flipped on its face. I recommend using IC sockets for the MCU. 


## Case
The current case only supports the HHKB bottom row with 2x 1U keys, the version with the larger blockers is still on my todo. If you cant wait though, feel free to edit the STEP files to your needs. For the diffusor, I chose transparent PETG and for a more unified look, changed the last layer to white. The mounting system of the case itself is inspired from the awesome cases from Bubbleology and uses the same magnets.

For printing, I recommend 0.2mm layer height, anything around 10% infill. How tight the plate works for you also depends on the swichtes you choose, if its too loose you can play around with the XY Hole compensation in your slicer.

## Firmware
Another todo, QMK is comming soon(tm). Currently im running a version of KMK created with POG to drive my prototype. I added my files from the POG generated KMK, not sure if this works how intended though. Once the QMK port is ready, I link it here.

### KLE layout options

![Screenshot of KLE](https://github.com/exen904/ISO13715-PCB/blob/main/pictures/kle.jpg)

## Build Guide
[You can find the build guide for the PCB here](https://github.com/exen904/ISO13715-PCB/blob/main/build_guide.md)