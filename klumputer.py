__module_name__ = "Klomputer" 
__module_version__ = "0.7" 
__module_description__ = "In-line interpreter for Klom number system by dodgems/Matt Styles (matthew.styles@bcs.org)"

print "\0034",__module_name__, __module_version__," has been loaded!\003"

import xchat 
import os 
import re

# Explicit calling of the message traversing process depending upon 
# the triggering event listener. XChat default user events list is to blame 
# for the cumbersome definitions following.

# Message received in a channel
def callfrom_ChanMsg(word, word_eol, userdata):
	nickin, messagein, modein, messageiin = word
	outputtext = interpret_message(messagein)
	xchat.get_context().command("say " + outputtext)
	return null
	
# Action received in a channel
def callfrom_ChanAction(word, word_eol, userdata):
	nickin, actionin, modein = word
	outputtext = interpret_message(actionin)
	#TODO: command
	return null
	
# Highlighted action received in a channel
def callfrom_ChanActionHi(word, word_eol, userdata):
	nickin, actionin, modein = word
	outputtext = interpret_message(actionin)
	#TODO: command
	return null

# Highlighted message received in a channel
def callfrom_ChanMsgHi(word, word_eol, userdata):
	nickin, messagein, modein, messageiin = word
	outputtext = interpret_message(messagein)
	#TODO: command
	return null
	
# Notice (direct or group) received in a channel
def callfrom_ChanNotice(word, word_eol, userdata):
	nickin, channelin, messagein = word
	outputtext = interpret_message(messagein)
	#TODO: command
	return null
	
# Private message received 
#def callfrom_PrivMsg():


# Match function - encode match and return as string
def sub_num(match):
    return str(base_encode(match.group(0)))
	
# Iterate over message replacing base10 numbers
def interpret_message(message):
	pattern = "(-?\d+)|(\+1)"
	return re.sub(pattern, sub_num, message)

# TODO: split floats into parts 
#def split_floats(float):
#	# split
#	# encode left
#	# encode right
#	# concat results
#	return null

# TODO: Test this doesn't cock up in older compilers and interpreters
# Klom alphabet (base7)
alphabet = "0-<Δ±¥*" 

# Convert base10 integer to alien number string
def base_encode(num):
    if (num == 0):
        return alphabet[0]
		
    arr = []
    base = len(alphabet)
	
    while num:
        rem = num % base
        num = num // base
        arr.append(alphabet[rem])
		
    arr.reverse()
    return ''.join(arr)

# Convert alien number string to base10 integer
def base_decode(string):
    base = len(alphabet)
    strlen = len(string)
    num = 0
    idx = 0
	
    for char in string:
        power = (strlen - (idx + 1))
        num += alphabet.index(char) * (base ** power)
        idx += 1

    return num
	
xchat.hook_print('Channel Message', callfrom_ChanMsg)
xchat.hook_print('Channel Action', callfrom_ChanAction)
xchat.hook_print('Channel Action HiLight', callfrom_ChanActionHi)
xchat.hook_print('Channel Msg Hilight', call_interpreter)
xchat.hook_print('Channel Notice', call_interpreter)
#xchat.hook_print('Private Message', call_interpreter)