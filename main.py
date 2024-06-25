import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import pyaudio

def speak(audio):
    engine = pyttsx3.init()
    # getter method(gets the current value     # of engine property)
    voices = engine.getProperty('voices')

    # setter method .[0]=male voice and
    # [1]=female voice in set Property.
    engine.setProperty('voice', voices[0].id)

    # Method for the speaking of the assistant
    engine.say(audio)

    # Blocks while processing all the currently
    # queued commands
    engine.runAndWait()


def Take_query():
    # calling the Hello function for making it more interactive
    Hello()

    # This loop is infinite as it will take our queries continuously until and unless we do not say bye to exit or terminate the program
    while (True):

        # taking the query and making it into lower case so that most of the times query matches and we get the perfect output
        query = takeCommand().lower()
        if "open geeksforgeeks" in query:
            speak("Opening GeeksforGeeks ")

            # in the open method we just to give the link
            # of the website and it automatically open
            # it in your default browser
            webbrowser.open("www.geeksforgeeks.com")
            continue

        elif "open google" in query:
            speak("Opening Google ")
            webbrowser.open("www.google.com")
            search()
            continue

        elif "open wikipedia" in query:
            speak("Opening wikipedia ")
            webbrowser.open("www.wikipedia.com")
            search()
            continue


        # this will exit and terminate the program
        elif "bye" in query:
            speak("Bye. See you soon")
            exit()

        elif "from wikipedia" in query:

            # if any one wants to have a information from wikipedia
            speak("Checking the wikipedia ")
            query = query.replace("wikipedia", "")

            # it will give the summary of 4 lines from wikipedia we can increase and decrease also.
            result = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            speak(result)

        elif "tell me your name" in query:
            speak("I am Jim. Your desktop Assistant")


# this method is for taking the commands and recognizing the command from the speech_Recognition module we will use the recongizer method for recognizing
def takeCommand():
    r = sr.Recognizer()

    # from the speech_Recognition module we will use the Microphone module for listening the command
    with sr.Microphone() as source:
        print('Listening')
        # seconds of non-speaking audio before phrase is considered complete
        r.pause_threshold = 0.7
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        # Now we will be using the try and catch
        # method so that if sound is recognized
        # it is good else we will have exception
        # handling
        try:
            print("Recognizing")
            Query = r.recognize_google(audio, language='en-in')
            print("the command is printed=", Query)

        except Exception as e:
            print(e)
            speak("Say that again sir")
            return "None"

        return Query



def Hello():
#This function is for when the assistant is called it will say hello and then take query
	speak("hello sir I am your desktop assistant.Tell me how may I help you")


if __name__ == '__main__':
#  Main method for executing the functions
    Take_query()

def search():
    search_string = speak("Input the URL or string you want to search for:")
    print(search_string)
    search_string = search_string.replace(' ', '+')
    browser = webdriver.Chrome('chromedriver')
    for i in range(1):
        matched_elements = browser.get("https://www.google.com/search?q=" + search_string + "&start=" + str(i))

