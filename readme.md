
# How to use:

## Installation

Install this addon by pressing enter or double clicking it from the file manager. Then tell NVDA to install it by following the prompts.

## Using.

When NVDA  would normally speak indents, this addon should activate. If it doesn't, please contact me.
This addon will detect changes in indent level and beep to inform you that an indent occurred. When the text you are reading is more indented than the last text you were reading, it beeps farther to your right than it did before.
Also, the tone will play one whole tone higher  than the previous indent level would. For example, no tabs will be all the way to your left at one octave below a middle c. The first tab will cause NVDA to play a D3 (one step up), 2 tabs an E3 (two steps up), 3 tabs an fSharp3 (technically 3 steps), and so on.
The 3 tabs will be slightly farther right of the C, and a middle c would be much closer to the center of your body than the c below that.
When the text is less indented than it was before (assuming it was already indented), NVDA will do the opposite. For example, lowering the tone and moving it to the left. The farthest right tab level is 3 octaves higher than the no indent level.


## Future work.

I may play around with panning the audio dynamically. This would allow me to start the beep at your left, and move it 1 indent unit over a time of about 200 milliseconds. The advantage of this is you could judge the difference in indentation that just occurred, while in parallell hearing the code you are currently editing, even if you don't musically easily judge whole tone steps. 
I am also  experimenting with integrating this into NVDA core [Ticket in NVDA](https://github.com/nvaccess/nvda/issues/5906). I spoke about Indentone at NVDACon 2016 in a session about my add-ons. I received much great feedback, and I am excited to continue work on this. 
## Downloads:
### Download:
https://files.derekriemer.com/indentone-0.3.0.nvda-addon
### Source Code:
https://github.com/derekriemer/nvda-indentone