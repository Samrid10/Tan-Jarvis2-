# Tan-Jarvis2
TAN - AI VOICE ASSISTANT (JARVIS-STYLE GUI)

A voice-activated desktop assistant built with Python, capable of executing real system commands, speaking, listening, and interacting with a modern web-based GUI — inspired by JARVIS.

FEATURES

Wake Word Detection — say "Hey Tan" to activate

Speech Recognition (Google Speech API)

Text-to-Speech (pyttsx3)

System Command Automation

Open YouTube, Chrome, Notepad

Take screenshots

Adjust volume

Tell current time

Fuzzy Wake Word Matching

Real-Time Web GUI using HTML, CSS, and JavaScript

WebSocket Bridge for live communication between Python and browser

Type or speak commands directly from the interface

FOLDER STRUCTURE

tan-ai/
│
├── tan_code.py → Main AI assistant (voice logic)
├── gui_server.py → WebSocket bridge between AI and GUI
├── index.html → Frontend GUI
├── style.css → GUI styling
├── script.js → GUI interactivity
└── README.txt → Project documentation

SETUP

Install dependencies:
pip install speechrecognition pyttsx3 pyautogui fuzzywuzzy python-Levenshtein websockets

Optional (for microphone input):
pip install pyaudio

Run the project:
python gui_server.py

This will:

Start the WebSocket bridge on port 6789

Launch Tan AI in the background

Open index.html in your browser.

You will see:

Connection Status

Real-time logs (You & Tan messages)

Command input box

EXAMPLE INTERACTION

You: hey tan
Tan: Yes, I’m listening...
You: open youtube
Tan: Opening YouTube

GUI will display:
Connected ✅
You: hey tan
Tan: Yes, I’m listening...
You: open youtube
Tan: Opening YouTube

TECH STACK

Core AI : Python
Voice Recognition : SpeechRecognition (Google API)
Speech Output : pyttsx3
Automation : pyautogui
GUI : HTML, CSS, JavaScript
Communication : Python WebSockets
Fuzzy Logic : fuzzywuzzy

CUSTOMIZATION

Add new commands in handle_command() inside tan_code.py

Change UI colors or fonts in style.css

Add animations or effects in script.js

FUTURE ENHANCEMENTS

Animated waveform visualizer for listening mode

Weather, mail, and API integrations

Contextual memory & conversation history

Custom voice profiles

LICENSE

None currently.

CREDITS

Developed by Sam D
Inspired by J.A.R.V.I.S — bringing AI to your desktop.

If you like this project, give it a star on GitHub!
