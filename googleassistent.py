import pyttsx3
import pywhatkit
import datetime
import wikipedia

machine = pyttsx3.init()

def talk(text):
    print("Response:", text)   # Print response in terminal
    machine.say(text)          # Speak response
    machine.runAndWait()

def input_instruction():
    # Instead of microphone, take typed input
    instruction = input("Type your command here: ")
    return instruction.lower()

def play_John():
    instruction = input_instruction()
    if instruction == "":
        print("No instruction detected.")
        return

    print("Instruction:", instruction)

    if "play" in instruction:
        song = instruction.replace("play", "").strip()
        talk("Playing " + song)
        pywhatkit.playonyt(song)

    elif "time" in instruction:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk("Current time is " + time)

    elif "date" in instruction:
        date = datetime.datetime.now().strftime("%d/%m/%Y")
        talk("Today's date is " + date)

    elif "how are you" in instruction:
        talk("I am fine, how about you?")

    elif "what is your name" in instruction:
        talk("I am John, your assistant.")

    elif "who is" in instruction:
        human = instruction.replace("who is", "").strip()
        try:
            info = wikipedia.summary(human, sentences=1)
            talk(info)
        except Exception as e:
            talk("Sorry, I couldn't find information on that.")
            print("Error:", e)

    elif "stop" in instruction or "quit" in instruction:
        talk("Goodbye!")
        exit()

    else:
        talk("Please repeat")

while True:
    play_John()
