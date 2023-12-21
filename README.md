Amigo Documentation

#INTRODUCTION:
The Project 'Amigo' initially kicked off as an attempt to replicate what virtual assistants (like Siri,Bixby,Alexa, etc.) do. Amigo (curently under development) is a virtual assistant written in Python, that like most other virtual assistants aims to make your life easier.On startup, my *amigo* (pun intended) greets you according to time of the day, and tells on what version of python amigo runs upon, and boots into the program. For commands and its features, you can refer the keywords section below. Oh, and don't worry, as far as i know, i've made exceptions for each and every task. There are list of n features (updated on 21/12/2023) currently in Amigo. Since, this is an hobbyist attempt, if any errors found or suggestions (if any you'll be duely credited in this README file), feel free to contact me.

#SPECIFICATIONS (used during development):

	- RAM Size: 3 GB
	- Processor: Intel Core 2 Duo Processor P8400
	- Operating System: Windows 10 22H2 (32-bit)
	- Python Version: 3.11.4

#CONTACT ME:

	- Instagram:thenerdguy088 
	- Reddit:u/thenerdguy088 
	- Discord:thenerdguy088
	- e-mail id: amigo_pytest@outlook.com
	
#REFERENCES:

	- freecodecamp.org: Python Project – How to Build Tony Stark's JARVIS with Python 
	- geeksforgeeks.org: Voice Assistant using python, Python Desktop Notifier using Plyer module, Wikipedia module, Performing Google Search using Python code

#UPDATES & BUG FIXES:

1. Update #1 [UPDATE TIME: 21-12-2023 14:08 IST Line Count: 321]:	
	i) External Python Libraries Used (make sure that you installed the below libraries):

		- pyttsx3 
		- googlesearch
		- wikipedia

	ii) Standard Python Libraries Used:

		- socket
		- requests
		- time
		- pickle
		- smtplib
		- sys
		- webbrowser

	iii) Keywords / Features:

		- add numbers
		- subract numbers
		- multiply numbers
		- divide numbers
		- write notes
		- display notes
		- add tasks
		- display tasks
		- delete tasks
		- web search
		- translate
		- send email
		- youtube search
		- wikipedia search
		- set timer
		- get ip address

	iv) User - Defined Functions:

		- speak(str1) & speak_fast(str1) #using pyttsx3
		- trigger_notification(title1,message1) #using plyer 
		- is_online() #using socket
		- greetuser() #using datetime & pyttsx3
		- translate(fl,sl,str1) #using google translate and webbrowser
		- search_G(str2,n) #using googlesearch
		- search_WIKI(str3,n2) & show_WIKI(wiki_page,n3) #using wikipedia 
		- set_timer(result) #using time
		- get_external_ip() #using requests
		- send_email(sender_email, sender_password, to_email, subject, body, smtp_server='smtp.example.com', smtp_port=587) #using smtplib
