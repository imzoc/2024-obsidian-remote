---
dg-publish: true
---
I have [[dmenu]] open ...certain... windows using this script:

~~~
#!/bin/bash
wmctrl -l | dmenu -w $(xdo id) -i -l 10 | awk '{print $1}' | xargs wmctrl -ia
~~~

`wmctrl -l` only lists windows managed by X11 (I think?), which does not include Firefox, frustratingly. It can open obsidian though. Strangely, if I type "obs" instead of "Obs", obsidian does not appear, despite using the `-i` flag for dmenu, which is supposed to make the search case-insensitive. Also, I had to add `-w $(xdo id)` to dmenu's arguments because I could not give dmenu inputs otherwise. I still don't know why it didn't work without specifying the current window, or why it works now. I think that `-w` "integrates" dmenu into the current window... which doesn't really make sense when I run the script using a non-interactive shell. Specifically, I have a custom keyboard shortcut in my Ubuntu settings that runs the command `quick_switch.sh` when I press `Alt+o`. I don't really know what exactly "running a command" does, but I'm guessing it just sends the text command to a non-interactive shell. I don't know how to find out, I can't find anything useful through web search. It isn't that important though. I'd like to get wmctrl and dmenu to work with firefox though. Maybe in the future.

8/24 Zach