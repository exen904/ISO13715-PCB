# Build Guide

For this build guide I am using a matte black PCB, which was kindly sponsored by PCBway. Huge shoutout here, I had a great order experience with them and the unique matte black/yellow silkscreen is something I really wanted to try in the past. 
## BOM

- 15x SOD123 Diodes
- 3x SK-6812 MINI-E
- 2x 2U PCB mounted Stabilizers
- 1x MCU of your choice
- 13-15 Switches of your choice
- Keycaps (obviously)

### MCU choice
The PCB design supports two different MCU choices, both based of the RP2040. Depending on which MCU you choose, you have to place it face up or face down. Version 1.1 of the PCB also references this on the silkscreen.

- Option 1: Seeed Xiao RP2040, the MCU footprint is also based on this
	- **face up**
- Option 2: Waveshare RP2040 Zero, 0xCB Gemini (personal preference if youre EU/DE based), 
	- **face down**

## Diodes
The SMD package might be intimidating if you never worked with it before, but I prefer it a lot over the easier looking 1N4148 THT diodes. Its always a pain to get those perfectly straight, clip all the legs, just creates a huge mess and I dont like the clipped solder joints on the other side of the PCB. 

The diodes are directional, you see a mark on one of the pads with a `U-shape` (also towards the MCU). This is your cathode marking which corresponds to a line on top of the diode. To solder these, tin one of the pads first. Place the diode then with tweezers just above that tinned pad, reheat the pad and push the side of the diode on the now heated pad. Before I solder the other side of the diode, I push a little on top of it to make sure its sitting plane on the PCB, while keeping the pad heated. Now solder the other side. Repeat for all of your diodes. You can also tack all of them down on one side first and then solder the other. Just make sure you dont forget any soldering joints. 

![Diode alignment](https://github.com/exen904/ISO13715-PCB/blob/main/pictures/diode.png)

## LEDs
The LEDs are a bit more tricky, as they dont like too much heat. For directions, the `GND` pad is marked with an `L-Shape`. Align the feet with the cut here to the L-Shape. For soldering these, I prefer to bump my temperature up a bit and work with as little contact as needed. On the Pinecil, I go up to 400°C for reference. 

Also tin one of the pads, align the LED, re-heat the pad and solder the other joints. If youre not sure that you placed the LED in the correct orientation and the GND leg is covered by solder, you can also look on the front side of the LED. Under the glass pane is a little notch, where your GND is located. If you solder the LEDs in backwards, you create a short and the MCU will go into smoke machine mode after enough time. Dont do this to your MCU. 

![LED alignment](https://github.com/exen904/ISO13715-PCB/blob/main/pictures/led.png)

## MCU
I recommend socketing your MCU but you can also work with regular header pins if you want. Just make **really** sure in that case, that your MCU is facing the right way. In this guide, I will refer to socketing the MCU. 

**Before you solder anything here, connect it to your PC and check if you can put your firmware on it. It that works/your MCU turns on, proceed.**

If you are going the Gemini way, you will be left with not connected/needed pins. That is intentional and no issue.

At fist, solder in your socket headers. The so called `IC sockets` work just fine, no need to get the expensive Millmax ones. For soldering these, I fixate it with one pin soldered, check for needed alignment, correct if needed and then solder the remaining pins down. Do this for both sides. 

For pins of your MCU, I personally recommend getting the Millmax pins. Some people use cut of legs of those awful 1N4148 diodes or similar, which are definitely way cheaper, but also the inferior choice. In the past I had connection issues with them, as they are much slimmer in diameter and maybe not contact your socket headers correctly. They also bend if you just look at them, which can make removing/inserting the MCU in the headers more difficult. 

![Millmax Pins](https://github.com/exen904/ISO13715-PCB/blob/main/pictures/millmax_pins.png)

For soldering the pins in, I place them in the socket headers and the MCU on top. To prevent solder from permanently fuse your pins and sockets together, cover the socket headers first with a layer of kapton tape. I then use a sewing needle to pierce the kapton in preparation for the Millmax pins. I recommend alternating left/right while soldering the pins to your MCU for a bit better thermal management of your MCU PCB. I never really had any issues with RP2040 based MCUs here, but I like to make sure. 

![Sockets with Kapton](https://github.com/exen904/ISO13715-PCB/blob/main/pictures/kapton_sockets.png)
![MCU soldering](https://github.com/exen904/ISO13715-PCB/blob/main/pictures/mcu_pin.png)

After you soldered your pins, remove the MCU, peel off the tape and you can start soldering your switches. 

![MCU with pins](https://github.com/exen904/ISO13715-PCB/blob/main/pictures/mcu_with_pins.png)

## Switches, Stabilizers, Keycaps
**Remember to first print the plate from the case before you solder Switches!** The PCB is Millmax Socket compatible by the way, tested with mine.

Solder your switches in the positions for your wanted layout, please check with keycaps if you are not sure what to use. 

Install stabilizers and keycaps, I will not explain this one. 