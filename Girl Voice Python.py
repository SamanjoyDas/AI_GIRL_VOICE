import pyttsx3

friend = pyttsx3.init()
voices = friend.getProperty('voices')
friend.setProperty('voice', voices[1].id) #voice[0] => male
friend.setProperty('rate', 150) #150 is delay time
friend.say("MESSAGE")
friend.setProperty('rate', 100)
friend.say("MESSAGE")
friend.runAndWait()
friend.stop()
