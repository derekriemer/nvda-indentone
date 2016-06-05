"""indentone: A global plugin for turning indentation into tones.
Copyright (C) Derek Riemer, 2016.
This is GPL code with no warranty. See NVDA's license for more info.
"""
import re
import globalPluginHandler
import speech
import tones
import gui
import wx
import config
from logHandler import log


#constants for level config. 
PITCH = 1
STEREO = 2

confspec = {
	"tones" : "boolean(default=True)",
	"indentUnit" : "integer(min=1, default=4)",
	"speakAndTones" : "boolean(default=False)",
	"toneType" : "integer(min=1, max=3, default=3)",
}
MAX_LEVEL = 0
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	
	def __init__(self, *args, **kwargs):
		global MAX_LEVEL
		super(globalPluginHandler.GlobalPlugin, self).__init__(*args, **kwargs)
		config.conf.spec["indentone"] = confspec
		self.oldSpeech = speech.getIndentationSpeech
		speech.getIndentationSpeech = self.myIndent
		theType = config.conf["indentone"]["toneType"]
		yesPitch = theType & PITCH
		yesStereo = theType & STEREO
		MAX_LEVEL = (18.0 if not (yesStereo and not yesPitch) else 12.0) #Stereo can't be heard well at 18 without pitch, it just souneds the same.


	def _reportIndentChange(self,  level):
		""" Reports the current level change as a tone. The first twenty levels are given distinct stereo positions, and otherwise, no tone will play.
		@var level: The level to report indents for. Only pass a homoginous set of tabs or spaces, because the length is calculated assuming each character is one indent unit.
		@type level: int
		"""
		volume = speech.getSynth().volume
		if config.conf["indentone"]["toneType"] & PITCH:
			note = 128*2**(level/MAX_LEVEL*3) #MAX_LEVEL*3 gives us 3 octaves of whole tones.
		else:
			note = 256
		#calculate stereo values. NVDA expects  values between 0 and 100 for stereo volume for each channel.
		if config.conf["indentone"]["toneType"] & STEREO:
			right = int((volume/(MAX_LEVEL-1))*level)
			left = volume-right
		else:
			left = right = 50
		tones.beep(note, 80, left=left, right=right)
		return

	def myIndent(self, indent):
		if not config.conf["indentone"]["tones"]:
			#The user has reporting of indents using tones off. Whatever, their choice.
			return self.oldSpeech(indent)
		hasChanged=False
		lchar = ""
		toneify = ""
		#Decide if there is a homoginous set of characters, or mixxed indent chars. toneify gets only the first type of indent characters (i.e. if there are two tabs and then 4 spaces, the addon sonifies the two tabs and not the spaces).
		for i in indent:
			if lchar == "":
				lchar = i
				toneify = i
			elif lchar == i:
				toneify += i
			else:
				#it's a different indent character. break   here.
				hasChanged = True
				break
		toneify = re.sub(" {{{indentSpaces}}}".format(indentSpaces = config.conf["indentone"]["indentUnit"]), 
			r"\t", toneify) 
		if not all([i == "\t" for i in toneify]):
			hasChanged = True
		level = len(toneify)
		if level > MAX_LEVEL:
			return self.oldSpeech(indent) #We can't sonify that many tabs.
		elif hasChanged: #there is more than one type of character that makes up these indents. We probably should speak it since tones alone can't do it.
			return self.oldSpeech(indent)
		else:
			self._reportIndentChange(level)
			if config.conf["indentone"]["speakAndTones"]:
				return self.oldSpeech(indent)
			else:
				return "" #the tone has us covered.



#The following lines can be used as a testing grounds.

	
		
			
				
					
						
							
								
									
										
											
												
													
														
															
																
																	
																		
																			
																				
																					
																						
																							
																								
																									
																										
																											
																												