from amigo_mod import *
D='\t'*5
X='='*100
add_num=[]
ver=version[0:4]
task_list=[]
dt=str(datetime.now())
speak('Hello There')
print(str(D)+'AMIGO'+'\t'*3+'Date & Time: '+dt)
print(X)
greetuser()
speak('Amigo is currently running on Python Version "{}"'.format(ver))
while True:
    command=input('<< $ ')
    if ('hi' in command):
        greetuser()
        speak("I'm Amigo and I am here to help you today. My objective is to supporting you with your daily activities, and I'm capable of handling a wide range of tasks and inquiries. Rest assured, I am here to serve you to the best of my abilities.")
        print(">>> I'm Amigo and I am here to help you today. My objective is to supporting you with your daily activities, and I'm capable of handling a wide range of tasks and inquiries. Rest assured, I am here to serve you to the best of my abilities.")
        print(X)
    elif ('add numbers' in command) or ('add numbers'.upper() in command) or ('add numbers'.capitalize() in command) or ('add numbers'.title() in command):
        speak('Enter the number of values to sum')
        n=int(input("<< Enter the number of values to sum: "))
        for i in range(n):
            speak('Enter Number')
            try:
                element=int(input("<< Please enter a number: "))
                add_num.append(element)
            except ValueError:
                speak('Invalid input. Please enter a valid number.')
                print('>>> Invalid input. Please enter a valid number.')
        result=sum(add_num)
        speak('{} is the sum'.format(result))
        print('>>>', result, 'is the sum.')
        print(X)
        add_num.clear()
    elif ('subract numbers' in command) or ('subract numbers'.upper() in command) or ('subract numbers'.capitalize() in command) or ('subract numbers'.title() in command):
    	try:
    		speak('Enter the first number')
    		n1=int(input("<< Please enter the first number: "))
    		speak('Enter the second number')
    		n2=int(input("<< Please enter the second number: "))
    		result_1=n1-n2
    		print('>>>', result_1, 'is the difference between', n1, 'and', n2, '.')
    		speak('{} is the difference between {} and {}'.format(result_1,n1,n2))
    		print(X)
    	except ValueError:
    		speak("Invalid input Please enter a valid integer")
    		print(">>> Invalid input. Please enter a valid integer.")
    		print(X)
    	except Exception as e:
    		speak("An error occurred: {e}")
    		print(f"An error occurred: {e}")
    		print(X)
    elif ('multiply numbers' in command) or ('multiply numbers'.upper() in command) or ('multiply numbers'.capitalize() in command) or ('multiply numbers'.title() in command):
    	try:
    		speak('Enter the first number')
    		n3=int(input("<< Please enter the first number: "))
    		speak('Enter the second number')
    		n4=int(input("<< Please enter the second number: "))
    		result_1=n3*n4
    		print('>>>', result_1, 'is the product of', n3, 'and', n4, '.')
    		speak('{} is the product of {} and {}'.format(result_1, n3, n4))
    		print(X)
    	except ValueError:
    		speak("Invalid input Please enter a valid integer")
    		print(">>> Invalid input. Please enter a valid integer.")
    		print(X)
    	except Exception as e:
    		speak("An error occurred: {e}")
    		print(f"An error occurred: {e}")
    		print(X)
    elif ('divide numbers' in command) or ('divide numbers'.upper() in command) or ('divide numbers'.capitalize() in command) or ('divide numbers'.title() in command):
    	try:
    		speak('Enter the first number')
    		n5=int(input("<< Please enter the first number: "))
    		speak('Enter the second number')
    		n6=int(input("<< Please enter the second number: "))
    		if n6 == 0:
    			speak('Division by zero is not possible')
    			print('>>> Division by zero is not possible.')
    			print(X)
    		else:
    			if n5 > n6:
    				result_3=n5 / n6
    				print('>>>', result_3, 'is the quotient of', n5, 'and', n6, '.')
    				speak('{} is the quotient of {} and {}'.format(result_3, n5, n6))
    				print(X)
    			else:
    				result_3=n6 / n5
    				print('>>>', result_3, 'is the quotient of', n6, 'and', n5, '.')
    				speak('{} is the quotient of {} and {}'.format(result_3, n6, n5))
    				print(X)
    	except ValueError:
    		speak("Invalid input Please enter a valid integer")
    		print(">>> Invalid input. Please enter a valid integer.")
    		print(X)
    	except Exception as e:
    		speak("An error occurred: {e}")
    		print(f"An error occurred: {e}")
    		print(X)
    elif ('write notes' in command) or ('write notes'.upper() in command) or ('write notes'.capitalize() in command) or ('write notes'.title() in command):
        f=open('amigo_notes.txt','a')
        f.write(dt)
        speak('Enter Notes')
        notes=input("<< Please enter your notes: ")
        f.write('\n'+notes)
        f.close()
        speak('Notes were successfully writen into amigo_notes.txt')
        print('>>> Notes were successfully writen into amigo_notes.txt')
        print(X)
    elif ('display notes' in command) or ('display notes'.upper() in command) or ('display notes'.capitalize() in command) or ('display notes'.title() in command):
        f=open('amigo_notes.txt',"r")
        x3=f.read()
        y=x3.split()
        for i in y:
            print(i,end=' ')
            speak_fast(i)
        print(X)
    elif ('add tasks' in command) or ('add tasks'.upper() in command) or ('add tasks'.capitalize() in command) or ('add tasks'.title() in command):
    	try:
    		f=open('tasks.bin', 'ab')
    		speak('Enter Number Of Tasks')
    		n=int(input('<< Enter Number Of Tasks: '))
    		for i in range(n):
    			speak('Enter Task')
    			task=input('<< Enter Task: ')
    			task_list.append(task.lower())
    			pickle.dump(task_list, f)
    		f.close()
    		print('>>>', n, 'tasks have been successfully added to the list.')
    		speak('"{}" tasks have been successfully added to the list'.format(n))
    		print(X)
    	except ValueError:
    		speak("Invalid input Please enter a valid integer")
    		print(">>> Invalid input. Please enter a valid integer.")
    		print(X)
    	except Exception as e:
    		speak("An error occurred: {e}")
    		print(f"An error occurred: {e}")
    		print(X)
    elif ('display tasks' in command) or ('display tasks'.upper() in command) or ('display tasks'.capitalize() in command) or ('display tasks'.title() in command):
    	try:
    		c=0
    		with open('tasks.bin', 'rb') as f:
    			task_list=pickle.load(f)
    			speak('Tasks were loaded successfully.')
    			print('>>> Tasks loaded successfully.',)
    			for i in task_list:
    				c+=1
    				speak('Task "{}" is "{}"'.format(c,i))
    				print('>>> Task',c,':',i)
    			print(X)
    	except FileNotFoundError:
    		speak('It seems that the file tasks.bin has not been created, use add tasks to create.')
    		print('>>> ERROR: The file "tasks.bin" does not exist.')
    		print(X)
    	except EOFError:
    		speak('It seems that the file "tasks.bin" is empty or not in the expected format.')
    		print('>>> ERROR: The file "tasks.bin" is empty or not in the expected format.')
    		print(X)
    	except Exception as e:
    		speak('An unexpected error occurred.')
    		print('An unexpected error occurred:', e)
    		print(X)
    elif ('delete tasks' in command) or ('delete tasks'.upper() in command) or ('delete tasks'.capitalize() in command) or ('delete tasks'.title() in command):
    	try:
    		with open('tasks.bin', 'wb+') as f:
    			task_list1=pickle.load(f)
    			speak('Enter Task to delete')
    			task=input('<< Enter Task:')
    			if task.lower() in task_list1:
    				task_list1.remove(task)
    				pickle.dump(task_list, f)
    				speak("'{}' was deleted from the list.".format(task))
    				print('>>>',task,'was deleted from the list')
    			else:
    				speak("'{}' does not exist in the list.".format(task))
    				print('>>>',task,'does not exist in the list.')
    	except FileNotFoundError:
    		speak('It seems that the file tasks.bin has not been created, use add tasks to create.')
    		print('>>> ERROR: The file "tasks.bin" does not exist.')
    		print(X)
    	except EOFError:
    		speak('It seems that the file "tasks.bin" is empty or not in the expected format.')
    		print('>>> ERROR: The file "tasks.bin" is empty or not in the expected format.')
    		print(X)
    	except Exception as e:
    		speak('An unexpected error occurred.')
    		print('An unexpected error occurred:', e)
    		print(X)
    elif ('web search' in command) or ('web search'.upper() in command) or ('web search'.capitalize() in command) or ('web search'.title() in command):
        if is_online()==True:
            speak('What would you like to search today')
            search_str=input('<< What would you like to search today?: ')
            search_G(search_str,5)
            print(X)
        else:
            trigger_notification('No Internet Available','Connect your device to internet.')
            speak('Connect your device to internet.')
            print('>>> Connect your device to internet.')
            print(X)
    elif ('translate' in command) or ('translate'.upper() in command) or ('translate'.capitalize() in command) or ('translate'.title() in command):
        if is_online()==True:
            speak('Enter what you would like to translate')
            txt=input('<< Enter Text: ')
            speak("What's the First Language, if not known just click enter")
            print('>>> If you do not know what language it is from,just click enter.')
            L_1=input('<< Enter First Language: ')
            speak("What's the second language that you would want to translate")
            L_2=input('<< Enter Second Language: ')
            translate(L_1,L_2,txt)
            print(X)
        else:
        	trigger_notification('No Internet Available','Connect your device to internet.')
        	speak('Connect your device to internet.')
        	print('>>> Connect your device to internet.')
        	print(X)
    elif ('send email' in command) or ('send email'.upper() in command) or ('send email'.capitalize() in command) or ('send email'.title() in command):
    	if is_online()==True:
    		speak('Enter the sender email address')
    		sender_email=input('<< Enter the sender email address: ')
    		speak('Enter the sender email password')
    		sender_password=input('<< Enter the sender email password: ')
    		speak('Enter the recipient email address')
    		to_email=input('<< Enter the recipient email address: ')
    		speak('Enter the subject of the email')
    		subject=input('<< Enter the subject: ')
    		speak('Enter the body of the email')
    		body=input('<< Enter the body: ')
    		speak('Enter the SMTP server (press Enter for default)')
    		smtp_server=input('<< Enter the SMTP server (press Enter for default): ') or 'smtp.example.com'
    		speak('Enter the SMTP port (press Enter for default)')
    		smtp_port=input('<< Enter the SMTP port (press Enter for default): ') or 587
    		send_email(sender_email, sender_password, to_email, subject, body, smtp_server, smtp_port)
    		print(X)
    	else:
    		trigger_notification('No Internet Available','Connect your device to internet.')
    		speak('Connect your device to internet.')
    		print('>>> Connect your device to internet.')
    		print(X)
    elif ('youtube search' in command) or ('youtube search'.upper() in command) or ('youtube search'.capitalize() in command) or ('youtube search'.title() in command):
        if is_online()==True:
            speak('What are you planning to watch today on YouTube')
            search_str=input('<< What are you planning to watch today on YouTube?: ')
            speak('What type of content are you browsing')
            search_type=input('<< Enter the type of content to browse (Video/Music/Playlist/Podcast/Shorts/Channel)?: ')
            results=int(input('How many Videos to be scraped?: '))
            search_G(search_str.lower()+str(search_type.lower())+'- youtube.com',results)
            print(X)
        else:
            trigger_notification('No Internet Available','Connect your device to internet.')
            speak('Connect your device to internet.')
            print('>>> Connect your device to internet.')
            print(X)
    elif ('wikipedia search' in command) or ('wikipedia search'.upper() in command) or ('wikipedia search'.capitalize() in command) or ('wikipedia search'.title() in command):
        if is_online()==True:
            try:
                speak('Enter the wikipedia article to search')
                wiki_page=input("<< Enter Article to Search on Wikipedia: ")
                X1=search_WIKI(wiki_page,10)
                speak('Enter the Number Of Sentences to be displayed from the article')
                sents=input("<< Enter the Number Of Sentences to be displayed from the article: ")
                show_WIKI(X1,sents)
                print(X)
            except ValueError:
                speak("Invalid input Please enter a valid integer")
                print(">>> Invalid input. Please enter a valid integer.")
                print(X)
            except Exception as e:
                speak("An error occurred: {e}")
                print(f"An error occurred: {e}")
                print(X)
        else:
            trigger_notification('No Internet Available','Connect your device to internet.')
            speak('Connect your device to internet.')
            print('>>> Connect your device to internet.')
            print(X)
    elif ('set timer' in command) or ('set timer'.upper() in command) or ('set timer'.capitalize() in command) or ('set timer'.title() in command):
    	try:
    		speak('Enter the number of minutes to set the timer')
    		m=int(input('<< Enter the number of minutes to set the timer: '))
    		speak('Enter the number of seconds to set the timer')
    		s=int(input('<< Enter the number of seconds to set the timer: '))
    		speak("The timer has been set for '{}' minutes '{}' seconds".format(m,s))
    		print(">>> The timer has been set for",m,"minutes",s,"seconds")
    		result=m*60+s
    		set_timer(result)
    		speak('Timer Completed')
    		print('>>> Timer Completed!')
    		print(X)
    	except ValueError:
    		speak("Invalid input Please enter a valid integer")
    		print(">>> Invalid input. Please enter a valid integer.")
    		print(X)
    	except KeyboardInterrupt:
    		speak('Timer setting interrupted by the user')
    		print("Timer setting interrupted by the user.")
    		print(X)
    	except Exception as e:
    		speak("An error occurred: {e}")
    		print(f"An error occurred: {e}")
    		print(X)
    elif ('get ip address' in command) or ('get ip address'.upper() in command) or ('get ip address'.capitalize() in command) or ('get ip address'.title() in command):
    	if is_online()==True:
    		ext_ip=get_external_ip()
    		speak("Your IP Address is {}".format(ext_ip))
    		print("Your IP Address is",ext_ip)
    		print(X)
    	else:
    		trigger_notification('No Internet Available','Connect your device to internet.')
    		speak('Connect your device to internet.')
    		print('>>> Connect your device to internet.')
    		print(X)
    elif ('exit' in command) or ('exit'.upper() in command) or ('exit'.title() in command) or ('exit'.capitalize() in command):
        speak('Goodbye')
        print(X)
        exit()
    else:
        speak("I kindly apologize for any confusion. Please provide further clarification for better understanding of what you are trying to say.")
        print(">>> I kindly apologize for any confusion. Please provide further clarification for better understanding of what you are trying to say.")
        print(X)
