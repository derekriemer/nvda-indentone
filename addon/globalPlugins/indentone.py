"""indentone: A global plugin for turning indentation into tones.
Copyright (C) Derek Riemer, 2016.
This is GPL code with no warranty. See NVDA's license for more info.
"""
import globalPluginHandler
import api
import re
import speech
import textInfos
import tones
import controlTypes
import inputCore
from NVDAObjects.window import Window
from NVDAObjects.IAccessible.scintilla import Scintilla
from NVDAObjects.behaviors import EditableText
from logHandler import log

MAX_LEVEL = 18.0
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	
	def __init__(self, *args, **kwargs):
		super(globalPluginHandler.GlobalPlugin, self).__init__(*args, **kwargs)
		self.oldSpeech = speech.getIndentationSpeech
		speech.getIndentationSpeech = self.myIndent


	def _reportIndentChange(self, text):
		""" Reports the current level change as a tone. The first twenty levels are given distinct stereo positions, and otherwise, no tone will play.
		@var text: The text to report indents for. Only pass a homoginous set of tabs or spaces, because the length is calculated assuming each character is one indent unit.
		@type text: string
		@returns: Indent level.
		"""
		level = len(text) #assume 1 indent unit per character.
		if level > MAX_LEVEL:
			return level
		volume = speech.getSynth().volume
		note = 128*2**(level/MAX_LEVEL*3) #MAX_LEVEL*3 gives us 3 octaves of whole tones.
		#calculate stereo values. NVDA expects  values between 0 and 100 for stereo volume for each channel.
		right = int((volume/(MAX_LEVEL-1))*level)
		left = volume-right
		tones.beep(note, 80, left=left, right=right)
		return level

	def myIndent(self, indent):
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
				#it's different. break it all here.
				hasChanged = True
				break
		toneify = re.sub(r" {1,4}", r"\t", toneify)
		level = self._reportIndentChange(toneify)
		if level > MAX_LEVEL:
			return self.oldSpeech(indent)
		elif hasChanged: #there is more than one type of character that makes up these indents. We probably should speak it since tones alone can't do it.
			return self.oldSpeech(indent)
		else:
			return "" #the tone has us covered.



 #The following lines can be used as a testing grounds.

	
		
			
				
					
						
							
								
									
										
											
												
													
														
															
																
																	
																		
																			
																				
																					
																						
																							
																								
																									
																										
																											
																												