# Keymap Autogenerated by Pog do not edit
from kmk.keys import KC
from kmk.modules.macros import Macros, Press, Release, Tap, Delay
from kmk.modules.combos import Chord, Sequence

import pog
import customkeys

keymap = [
    [KC.A, KC.B, KC.C, KC.D, KC.E, KC.F, KC.G, KC.H, KC.J, KC.K, KC.Z, KC.X, KC.C, KC.V, KC.B]
]

encoderKeymap = []
for l, layer in enumerate(pog.config['encoderKeymap']):
    layerEncoders = []
    for e, encoder in enumerate(layer):
        layerEncoders.append(tuple(map(eval, encoder)))
    encoderKeymap.append(tuple(layerEncoders))
