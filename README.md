# AI Voice Assistant 🎙️🤖

A simple interactive voice assistant application built using **Python**, which integrates speech-to-text conversion, processing via artificial intelligence models, and text-to-speech audio output.

---

## 🚀 Features
* **Speech-to-Text:** Listens to user input through the microphone and converts it into Arabic text.
* **AI Response Generation:** Sends the text to the (`Cohere`) AI model to generate a smart and accurate response.
* **Text-to-Speech:** Converts the AI response into a clear audio file (`gTTS`) so you can listen to it.

---

## 🛠️ Tech Stack
* Python 3
* SpeechRecognition
* Cohere API
* gTTS (Google Text-to-Speech)

---

## ⚙️ How to Run

1. Install the required libraries via the terminal:
   ```bash
   pip install SpeechRecognition gTTS cohere

 2. Add your API key inside the script.
 3. Run the application:
     python app.py
