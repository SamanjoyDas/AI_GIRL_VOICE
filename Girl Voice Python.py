import pyttsx3

friend = pyttsx3.init()
voices = friend.getProperty('voices')
friend.setProperty('voice', voices[1].id) #voice[0] => male
friend.setProperty('rate', 150)
friend.say("Samanjoy")
friend.setProperty('rate', 100)
friend.say("I Love You.")
friend.runAndWait()
friend.stop()
