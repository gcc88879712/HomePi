# Home_Pi

## This project is trying to turn raspberry pi into a smart home device like Google home 

## This project are majorly divided in 5 parts 

### part1: record user audio and examine it whether contains the trigger word. 

### part2: Once hearing the trigger word, starts convert the hearing content into texts 

### part3: send converted text to search engine to get result 

### part4: collect first output result from search engine then send it to text to audio. 

### part5: play the audio 

## The major API hooking part of this project is properly done, one big problem is to analyse the returned data package from the api to identify useful information.

### currently the program have a pretty high accuracy reguards to the question that can be refered to some Wiki page. The problme performs very poor regards to the problems that does not have a clear answer to it.

### The voice activation part went into some trouble since our voice regonition is based on Google's Api, so that if the mic is on all the time to try to catch the activation word, it will goes very costy. 

### The voice recording has been set to 5 seconds. This is more than enough for some simple questions. The sound detect feature still in develop. 

### This runs poorly in Pi2 or older version of Pi since I used several nesting to try to analyse the returned data package. Still trying to figure a better way to take out the useful info from the dictionary.


