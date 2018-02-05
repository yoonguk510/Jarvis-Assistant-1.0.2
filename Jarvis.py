#!/usr/bin/python
# -*- coding: utf-8 -*-
import speech_recognition as sr
from time import ctime
from gtts import gTTS
import wolframalpha
import webbrowser
import wikipedia
import subprocess
import pyperclip
import time
import os
import sys
import time
import pyvona



name = 'Yooon Goo'


def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save('audio.mp3')
    os.system('mpg321 audio.mp3')


keywd = 'keyword list'
google = 'search for'
acad = 'academic search'
sc = 'deep search'
wkp = 'wiki page for'
music = 'music'
rdds = 'read this text'
sav = 'save this text'
bkmk = 'bookmark this page'
vid = 'video for'
wtis = 'what is' 
wtar = 'what are'
whis = 'who is'
whs = "who's"
whws = 'who was'
when = 'when'
where = 'where'
how = 'how'
lsp = 'silence please'
lsc = 'resume listening'
call = 'hey Jarvis'


cl = wolframalpha.Client('7536E5-3AY9E4WQKK')  # api for wolfram alpha
tt = cl.query('Test/Attempt')
r = sr.Recognizer()  # starting the speech_recognition recognizer

while True:  # The main loop

    with sr.Microphone() as source:

        try:

            audio = r.listen(source, timeout=None)  # instantiating the Microphone, (timeout = None) can be an option
            message = str(r.recognize_google(audio))
            print('You said: ' + message)

            if wkp in message:  # what happens when wkp keyword is recognized

                try:

                    words = message.split()
                    del words[0:3]
                    st = ' '.join(words)
                    wkpres = wikipedia.summary(st, sentences=2)

                    try:

                        print('\n' + str(wkpres) + '\n')
                        speak(wkpres)
                    except UnicodeEncodeError:

                        speak(wkpres)
                except wikipedia.exceptions.DisambiguationError as e:

                    print(e.options)
                    speak('Too many results for this keyword. Please be more specific and try again'
                          )
                    continue
                except wikipedia.exceptions.PageError as e:

                    print('The page does not exist')
                    speak('The page does not exist')
                    continue
            elif sc in message:

                                                                                            # what happens when sc keyword is recognized

                try:
                    words = message.split()
                    del words[0:1]
                    st = ' '.join(words)
                    scq = cl.query(st)
                    sca = next(scq.results).text
                    print('The answer is: ' + str(sca))

                    # url='http://www.wolframalpha.com/input/?i='+st
                    # webbrowser.open(url)

                    speak('The answer is: ' + str(sca))
                except StopIteration:

                    print('Your question is ambiguous. Please try again!')
                    speak('Your question is ambiguous. Please try again!')
            elif wtis in message:

                                                                                            # what happens when wtis keyword is recognized

                try:

                    scq = cl.query(message)
                    sca = next(scq.results).text
                    print(str(sca))

                    # url='http://www.wolframalpha.com/input/?i='+st
                    # webbrowser.open(url)

                    speak(str(sca))
                except UnicodeEncodeError:

                    speak(str(sca))
                except StopIteration:

                    words = message.split()
                    del words[0:2]
                    st = ' '.join(words)
                    print('Google Results for: ' + str(st))
                    url = 'http://google.com/search?q=' + st
                    webbrowser.open(url)
                    speak('Google Results for: ' + str(st))
            elif wtar in message:

                try:

                    scq = cl.query(message)
                    sca = next(scq.results).text
                    print('The answer is: ' + str(sca))

                    # url='http://www.wolframalpha.com/input/?i='+st
                    # webbrowser.open(url)

                    speak(str(sca))
                except UnicodeEncodeError:

                    speak(str(sca))
                except StopIteration:

                    words = message.split()
                    del words[0:2]
                    st = ' '.join(words)
                    print('Google Results for: ' + str(st))
                    url = 'http://google.com/search?q=' + st
                    webbrowser.open(url)
                    speak('Google Results for: ' + str(st))
            elif whis in message:

                                                                                            # what happens when whis keyword is recognized

                try:

                    scq = cl.query(message)
                    sca = next(scq.results).text
                    print('\nThe answer is: ' + str(sca) + '\n')
                    speak(str(sca))
                except StopIteration:

                    try:

                        words = message.split()
                        del words[0:2]
                        st = ' '.join(words)
                        wkpres = wikipedia.summary(st, sentences=2)
                        print('\n' + str(wkpres) + '\n')
                        speak(wkpres)
                    except UnicodeEncodeError:

                        speak(wkpres)
                    except:

                        words = message.split()
                        del words[0:2]
                        st = ' '.join(words)
                        print('Google Results (last exception) for: ' + str(st))
                        url = 'http://google.com/search?q=' + st
                        webbrowser.open(url)
                        speak('Google Results for: ' + str(st))
                        
                        
            elif whs in message:

                                                                                            # what happens when whis keyword is recognized

                try:

                    scq = cl.query(message)
                    sca = next(scq.results).text
                    print('\nThe answer is: ' + str(sca) + '\n')
                    speak(str(sca))
                except StopIteration:

                    try:

                        words = message.split()
                        del words[0:2]
                        st = ' '.join(words)
                        wkpres = wikipedia.summary(st, sentences=2)
                        print('\n' + str(wkpres) + '\n')
                        speak(wkpres)
                    except UnicodeEncodeError:

                        speak(wkpres)
                    except:

                        words = message.split()
                        del words[0:2]
                        st = ' '.join(words)
                        print('Google Results (last exception) for: ' + str(st))
                        url = 'http://google.com/search?q=' + st
                        webbrowser.open(url)
                        speak('Google Results for: ' + str(st))
            elif whws in message:

                                                                                           

                try:

                    scq = cl.query(message)
                    sca = next(scq.results).text
                    print('\nThe answer is: ' + str(sca) + '\n')
                    speak(str(sca))
                except StopIteration:

                    try:

                        words = message.split()
                        del words[0:2]
                        st = ' '.join(words)
                        wkpres = wikipedia.summary(st, sentences=2)
                        print('\n' + str(wkpres) + '\n')
                        speak(wkpres)
                    except UnicodeEncodeError:

                        speak(wkpres)
                    except:

                        words = message.split()
                        del words[0:2]
                        st = ' '.join(words)
                        print('Google Results for: ' + str(st))
                        url = 'http://google.com/search?q=' + st
                        webbrowser.open(url)
                        speak('Google Results for: ' + str(st))
            elif when in message:

                                                                                          # what happens when 'when' keyword is recognized

                try:

                    scq = cl.query(message)
                    sca = next(scq.results).text
                    print('str(sca)\n')
                    speak(str(sca))
                except UnicodeEncodeError:

                    speak(str(sca))
                except:

                    print('Google Results for: ' + str(message))
                    url = 'http://google.com/search?q=' + str(message)
                    webbrowser.open(url)
                    speak('Google Results for: ' + str(message))
            elif where in message:

                                                                                          # what happens when 'where' keyword is recognized

                try:

                    scq = cl.query(message)
                    sca = next(scq.results).text
                    print('\nThe answer is: ' + str(sca) + '\n')
                    speak(str(sca))
                except UnicodeEncodeError:

                    speak(str(sca))
                except:

                    print('Google Results for: ' + str(message))
                    url = 'http://google.com/search?q=' + str(message)
                    webbrowser.open(url)
                    speak('Google Results for: ' + str(message))
                    
            elif music in message:
                    os.system('cd music.py directory')
                    os.system('gnome-terminal -e "python3 music.py"')
            elif how in message:

                                                                                          # what happens when 'how' keyword is recognized

                try:

                    scq = cl.query(message)
                    sca = next(scq.results).text
                    print('\nThe answer is: ' + str(sca) + '\n')
                    speak(str(sca))
                except UnicodeEncodeError:

                    speak(str(sca))
                except:

                    print('Google Results for: ' + str(message))
                    url = 'http://google.com/search?q=' + str(message)
                    webbrowser.open(url)
                    speak('Google Results for: ' + str(message))

            elif lsp in message:

                speak('Listening is paused')
                print('Listening is paused')
                r2 = sr.Recognizer()
                r2.pause_threshold = 0.7
                r2.energy_threshold = 400

                while True:

                    with sr.Microphone() as source2:

                        try:

                            audio2 = r2.listen(source2, timeout=None)
                            message2 = str(r.recognize_google(audio2))

                            if lsc in message2:
                                speak('I am listening')
                                break
                            else:

                                continue
                        except sr.UnknownValueError:

                            print("Listening is paused. Say resume listening when you're ready...")
                        except sr.RequestError:

                            speak("I'm sorry, I couldn't reach google")
                            print("I'm sorry, I couldn't reach google")
            else:
                pass
        except sr.UnknownValueError:

            print('')
        except sr.RequestError:

            speak("I'm sorry, I couldn't reach google")
            print("I'm sorry, I couldn't reach google")

    time.sleep(0.3)


def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save('audio.mp3')
    os.system('mpg321 audio.mp3')


def recordAudio():

    # Record Audio

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something!')
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition

    data = ''
    try:

        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`

        data = r.recognize_google(audio)
        print('You said: ' + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data
