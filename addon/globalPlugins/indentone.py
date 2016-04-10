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

MAX_LEVEL = 22.0
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
		if level >= MAX_LEVEL:
			return level
		lev = level
		fundemental = 128
		while  lev >= 7:
			fundemental *=2 #increase the fundemental frequency by one octave so that we play the note in the correct octave.
			lev -= 7
		#calculate pitch.
		#Going up one full step per indent level.
		chords = [1, 1.125, 1.25, 1.33, 1.5, 1.666, 1.875]
		lev = (level) %7 #notes on this octave can be found by multiplying fundemental by the correct index.!
		note = chords[lev]*fundemental #NVDA never passes us a blank string.
		#calculate stereo values. NVDA expects  values between 0 and 100 for stereo volume for each channel.
		right = int((50/MAX_LEVEL)*level)
		left = 50-right
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
				continue
			else:
				#it's different. break it all here.
				hasChanged = True
				break
		toneify = re.sub(r" {1,4}", r"\t", toneify)
		#if self._detectIndentChange(toneify):
		level = self._reportIndentChange(toneify)
		if level >= MAX_LEVEL:
			return self.oldSpeech(indent)
		elif hasChanged: #there is more than one type of character that makes up these indents. We probably should speak it since tones alone can't do it.
			return self.oldSpeech(indent)
		else:
			return "" #the tone has us covered.



#The following lines encode 3 octaves of a C major scale. This shows off the entire range this plugin can support.

	
		
			
				
					
						
							
								
									
										
											
												
													
														
															
																
																	
																		
																			
																				
																					
																						
																							
																								
																									
																										
																											
																												
																													
																														
																															
																																
																																	
																																		
																																			
																																				
																																				
																																				
#The following lines encode Ode to joy in indent language. You'll have to be clever to hear it. 
									
									
										
											
											
										
									
								
							
							
								
									
									
								
								
									
									
										
											
											
										
									
								
							
							
								
									
								
							
							
								
								
									
							
								
									
										
									
							
								
									
										
									
								
							
								
				
									
									
									
										
											
											
										
									
								
							
							
								
									
								
							
							