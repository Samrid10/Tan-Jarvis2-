import datetime, os, time, webbrowser, pyautogui
import speech_recognition as sr
import pyttsx3
from fuzzywuzzy import fuzz

log_to_gui = None  # Will be injected from gui_server

# ---------- Speech engine ----------

engine = pyttsx3.init()

def speak(text):
    print(f"Tan: {text}")
    if log_to_gui:
        log_to_gui(f"Tan: {text}")
    engine.say(text)
    engine.runAndWait()

# ---------- Listener ----------
recognizer = sr.Recognizer()
def listen(timeout=7, phrase_time_limit=5):
    with sr.Microphone() as source:
        if log_to_gui:
            log_to_gui("Listening...")
        audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
    try:
        command = recognizer.recognize_google(audio, language="en-in")
        if log_to_gui:
            log_to_gui(f"You: {command}")
        return command.lower()
    except:
        return ""


# ---------- Wake word ----------
def wait_for_wake_word():
    while True:
        command = listen()
        if command:
            print(f"[DEBUG] Wake check: {command}")
            # Reliable wake word: "hey tan"
            if "hey tan" in command or fuzz.partial_ratio("hey tan", command) > 60:
                speak("Yes, I'm listening...")
                return

# ---------- Command handler ----------
def handle_command(command):
    command = command.lower()

    if "stop" in command or "go to sleep" in command:
        speak("Goodbye!")
        return False

    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")

    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "chrome" in command:
        speak("Opening Chrome")
        os.system("start chrome")

    elif "notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")

    elif "screenshot" in command:
        pyautogui.screenshot("screenshot.png")
        speak("Screenshot taken")

    elif "volume up" in command:
        pyautogui.press("volumeup")
        speak("Volume increased")

    elif "volume down" in command:
        pyautogui.press("volumedown")
        speak("Volume decreased")

    else:
        speak("I am not programmed for this yet.")

    return True

# ---------- Continuous Tan Loop ----------
def tan_loop():
    speak("Hello, I am Tan. Say 'Hey Tan' to wake me up.")
    while True:
        wait_for_wake_word()  # wait for "hey tan"
        active = True
        speak("I am listening for your commands now.")
        while active:
            command = listen()
            if not command:
                continue
            active = handle_command(command)

def start_ai(logger=None):
    global log_to_gui
    log_to_gui = logger
    tan_loop()

