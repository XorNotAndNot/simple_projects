# imports
import subprocess # open some applications
import time # to purposely delay some actions
import os # will be used to open files of specific types easily
import webbrowser # easy way to do basic web actions

# path variables for specific applications
# change the path to the respective app paths on your device
# add more as you need.
chrome_path = r'<full-path-to-chrome>'
vs_code = r'<full-path-to-vs_code-file>'
sublime = r'<full-path-to-sublime-file>'
class workspace:
	# basic functions (new tab, new window, etc)
	def new_window(self):
		subprocess.call(chrome_path)
	def new_tab(self, url):
		self.url = url
		webbrowser.open_new(url)

  # the functions below mostly work in the same way but for naming and call purposes, add or modify as you need.
	# opens an excel file
	def excel(self, file):
		self.file = file
		os.startfile(file) # open an application that handles excel files, with the given file being opened.
	# opens coding stuff
	def sublime(self, path):
		self.path = path
		subprocess.call(path)
	def vs_code(self, path):
		self.path = path
		subprocess.call(path)
 

"""
the section below is a test area. modify it as needed for your requirements.
"""
# school instance
school = workspace()
school.new_tab("www.example.com") # change to a site you use for school
time.sleep(5) # waits for 5 seconds to ccontinue; completely optional.
school.excel(r"<full-path-to-excel-file>") # change to excel a specific excel file path if needed.
school.new_window() # open a new window.
# coding instance
coding = workspace()
coding.sublime(sublime)
coding.vs_code(vs_code)
