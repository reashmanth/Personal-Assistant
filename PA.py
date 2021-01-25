import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

print("I'm zara your virtual Assistant ,How can i help you ? \n")
talk("I'm zara your virtual Assistant ,How can i help you ?")


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'zara' in command:
                command = command.replace('zara','')
                print('Zara heard u as: '+command)

    except:
        print("couldn't able to get that")
        pass
    return command


def run_zara():
    command = take_command()
    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I %M %p')
        print(time)
        talk('current time is' + time)

    elif 'date' in command:
        date = datetime.date.today().strftime('%D')
        print(date)
        talk("today's date is" + date)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'how are you' in command:
        print("i'm doing good ! how about you ?")
        talk("i'm doing good ! how about you")

    elif 'tell me a joke' in command:
        talk(pyjokes.get_joke())


    else:
        print("sorry! couldn't able to understand that")
        talk("sorry! couldn't able to understand that")

while True:
    run_zara()

