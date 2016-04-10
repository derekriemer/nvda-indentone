# How to use:

## Installation

Install this addon by pressing enter or double clicking it from the file manager. Then tell NVDA to install it by following the prompts.

## Using.

When in an edit window, this addon should activate. If it doesn't, please contact me.
This addon will detect changes in indent level and beep to inform you that an indent occurred. When the text you are reading is more indented than the last text you were reading, it beeps farther to your right than it did before. When the text is less indented than it was before (assuming it was already indented) NVDA will make a beep farther to the left than the previous beep. An example of this is NVDA beeping to your far left represents no indent. NVDA beeping slightly to your left may represent 4 spaces. If NVDA beeps to your far right that currently means 10 indent units. An indent unit is either four spaces, or one tab. After 10 indent units, NVDA reverts to speaking the number of indent units. I am open to playing around with the number of indent units, however the more indent units I add beeps for, the less space there is in the stereo field per beep. This means that it will be harder to detect each beep unit's difference.

## Future work.

I may play around with panning the audio dynamically. This would allow me to start the beep at your left, and move it 1 indent unit over a time of about 200 milleseconds. The advantage of this is you could judge the difference in indentation that just occurred, while in parrellell hearing the code you are currently editing.  
Techhnically, this will probably have to use separate audio libraries, because I do not think tones.beep is going to let me dynamically create an audio buffer. I probably will have to ship something like libaudioverse with this addon to do this, or write a custom library in c++. If anyone knows of the best way I should do this, I would like to talk to you real quick. Especially if you know how I could do it in python without shipping any audio library and using NVDA internals such as NVWave.