---
dg-publish: true
---
https://oryx.zsa.io/firmware/QyqQD

A gazelle snapshot from August 21, 2024.

I needed a name for my main [[moonlander]] keyboard layout and Gazelle sounds catchy enough.

Let me take you on a tour through my board.

## Layer 0: the alphabet

![[Screenshot from 2024-08-21 09-59-23.png]]
I'm using Dvorak as the base key layout. It might be more optimal to use workman or something, but I'm so used to Dvorak and Dvorak is almost as good, so I'm happy to stick with it.

I have homerow modifiers. I don't know if this is optimal placement. I need a shift to not be on the homerow for optimal layer functionality. It would technically work to press modifiers before you switch rows, but you would have to go back to layer 0 if you wanted to change your pressed modifiers. Plus you would need to go back and press the other hand's modifier if you wanted to type, say, `#)` because it's not possible to press both `#` and `)` with the same homerow modifier. It would be complicated, so I decided to make it a bit easier to press shift.

## Layer 1: navigation

![[Screenshot from 2024-08-21 10-16-45.png]]
On my first layer, accessed with my left thumb, I get access to arrow and navigation keys with my left fingers. Holding homerow modifiers from layer 0, I can relatively easily modify these keys, with the notable exception of `ctrl+del`, `alt+up`, and `shift+down`. I think this is okay. I doubt that these will find much use when I am using my mouse. I can easily press them using my right hand modifiers, which receive singular functionality for the sake of speed and collision reduction.

Notably: I can't press any right-hand layer-1 key with a single hand. I think this is only inconvenient for `enter`, `backspace`, and `esc`, so I created keystroke combos for them on the home layer using the bottom row of alphabet letters as alternatives. There is no good picture; `;qjk` maps to `enter`, `;qj` maps to `esc`, and `qjk` maps to `backspace`.

Notably: I can't modify any left-hand layer-1 keys with the `Meta` modifier with a single hand. I use `Meta+[arrow]` to resize windows (GNOME key shortcut), so that's why I assigned `Meta+left arrow` and `Meta+right arrow` to their own keys on layer 1. I can only take a few liberties like this if I want to keep my keyboard layout at 4 total layers, and I think this is worth it.

Notably: I also take the liberty to assign tmux and vim their own prefix keys. I don't use them very often, but I intend to. This does provide extra convenience, because `ctrl+b` and `shift+;` are not the easiest keys to press. If I use them a lot, I think it will be rewarding to have their own keys.

## Layer 2: numbers and symbols 
![[Screenshot from 2024-08-21 10-25-29.png]]

This layer speaks for itself, mostly.

Notably: this layer is why I have the right shift key on the bottom, and not as a homerow modifier. I want brackets and parenthases to be on the right hand because I almost never need to use them with a single hand. Other symbols, like \`, `/`, `\`, `-`, and `=` will frequently be used in keyboard shortcuts, but `9`, `0`, `[`, and `]` will probably not. Placing parenthases and brackets on the right hand side compromises the right shift homerow modifier for better layout organization, and it's a worthwhile compromise because having a constant shift modifier at all times adds a lot of versatility, as I discussed in layer 0.

## Layer 3: fn-keys

![[Screenshot from 2024-08-21 10-40-08.png]]
The fn-key layer follows the number layer scheme for cohesiveness. It goes up to f20, simply because that's all that conveniently fits and because I don't think I'll ever need f-keys higher than that.

---

A note about getting stuck on layers. This happens sometimes, probably as a glitch in the firmware. It's good to account for this without having to unplug the keyboard. I have a blank extra layer (in this case, layer 6 after unused, unaccessible gaming layers that I should probably just store somewhere else or get rid of entirely) that I can get to from any layer, and which sends my keyboard back to layer 0 with the same key. So double tapping the top left key from any layer will automatically send the keyboard to layer 1.

Zach 8/21/24