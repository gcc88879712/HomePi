#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyaudio
import speech_recognition as sr
import pyttsx3
import wave
from serpapi.google_search_results import GoogleSearchResults


# In[2]:


def GetVoice():
    # the file name output you want to record into
    filename = "recorded.wav"
    # set the chunk size of 1024 samples
    chunk = 1024
    # sample format
    FORMAT = pyaudio.paInt16
    # mono, change to 2 if you want stereo
    channels = 1
    # 44100 samples per second
    sample_rate = 44100
    record_seconds = 5
    # initialize PyAudio object
    p = pyaudio.PyAudio()
    # open stream object as input & output
    stream = p.open(format=FORMAT,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    output=True,
                    frames_per_buffer=chunk)
    frames = []
    print("Recording...")
    for i in range(int(44100 / chunk * record_seconds)):
        data = stream.read(chunk)
        # if you want to hear your voice while recording
        # stream.write(data)
        frames.append(data)
    print("Finished recording.")
    # stop and close stream
    stream.stop_stream()
    stream.close()
    # terminate pyaudio object
    p.terminate()
    # save audio file
    # open the file in 'write bytes' mode
    wf = wave.open(filename, "wb")
    # set the channels
    wf.setnchannels(channels)
    # set the sample format
    wf.setsampwidth(p.get_sample_size(FORMAT))
    # set the sample rate
    wf.setframerate(sample_rate)
    # write the frames as bytes
    wf.writeframes(b"".join(frames))
    # close the file
    wf.close()


# In[3]:


def v2t():
    r = sr.Recognizer()
    audiofile = sr.AudioFile('recorded.wav')
    with audiofile as source:
        audio = r.record(source)
    return_text = r.recognize_google(audio)
    print(return_text)
    return return_text


# In[4]:


def GetAnswer(return_text):
    params = {
      "api_key": "609d4beab3d238843bcf22588195a5b6db5ae8490a089215eac71985ba37f654",
      "engine": "google",
      "q": return_text,
      "location": "Los Angeles, CA, California, United States",
      "google_domain": "google.com",
      "gl": "us",
      "hl": "en",
    }
    client = GoogleSearchResults(params)
    results = client.get_dict()
    #print(results['knowledge_graph'])
    while True:
        try:
            useful_output = results['knowledge_graph']
            answer = useful_output['description']
            break
        except KeyError:
            try: 
                useful_output = results['answer_box']
                answer = useful_output['type']
                break
            except KeyError:
                try:
                    useful_output = results['knowledge_graph']
                    answer = useful_output['title']
                except KeyError:
                    answer = str("I don't know, try ask me something else")#this can go on and on to increase accuracy of the answe
    print(answer)
    return answer   


# In[5]:


def Sayit(answer):
    engine = pyttsx3.init() # object creation

    """ RATE"""
    rate = engine.getProperty('rate')   # getting details of current speaking rate
    print ('the speaking rate is: 'rate)                        #printing current voice rate
    engine.setProperty('rate', 125)     # setting up new voice rate


    """VOLUME"""
    volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
    print ('the volue is (max1,min0): ',volume)                          #printing current volume level
    engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

    """VOICE"""
    voices = engine.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

    engine.say(answer)
    engine.runAndWait()
    engine.stop()


# In[8]:


promt = "what can I help"
Sayit(promt)
GetVoice()
return_text = v2t()
answer = GetAnswer(return_text)
Sayit(answer)


# In[ ]:





# In[ ]:




