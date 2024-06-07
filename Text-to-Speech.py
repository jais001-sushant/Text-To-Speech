import gtts
import playsound    #(playsound==1.2.2)
import os

def speak(text):
    print(f"\n==> Smilodon AI: {text}\n")
    speech = gtts.gTTS(text, lang="en")
    speech_path = "temp.mp3"
    speech.save(speech_path)
    playsound.playsound("temp.mp3")
    os.remove(speech_path)

def main():
    while True:
        text = input("Enter TTS : ")
        if text.lower() == 'exit' or text.lower() == 'quit':
            speak("Goodbye!\nExiting...")
            break
        speak(text)

if __name__ == "__main__":
    main()