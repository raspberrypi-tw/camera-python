#!/bin/bash
for effect in none negative solarise sketch denoise emboss oilpaint hatch gpen pastel watercolour film blur saturation colourswap washedout posterise colourpoint colourbalance cartoon
do
        echo $effect
        raspivid -d -ifx $effect
done

