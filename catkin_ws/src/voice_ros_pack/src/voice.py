#!/usr/bin/env python3
import speech_recognition as sr
import pyttsx3
import rospy
from std_msgs.msg import String
engine = pyttsx3.init()
engine.setProperty('rate', 150)    # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)  # Volume 0-1
# obtain audio from the microphone

def recognition():
    r = sr.Recognizer()
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    with sr.Microphone() as source:
        print("Say something!")
        
        
        engine.say("     Say something!")
        engine.runAndWait()
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source,timeout=10, phrase_time_limit=10)

    try:
        #print("Sphinx thinks you said " + r.recognize_sphinx(audio))
        rospy.loginfo(r.recognize_google(audio))
        pub.publish(r.recognize_google(audio))
        engine.say(r.recognize_google(audio))
        engine.runAndWait()
        print("voiceEngine thinks you said " + r.recognize_google(audio))
        recognition()
    except sr.UnknownValueError:
        #print("Sphinx could not understand audio")
        engine.say("voiceEngine do not understand audio")
        engine.runAndWait()
        recognition()
    except sr.RequestError as e:
        engine.say("voiceEngine do not understand audio")
        engine.runAndWait()
        print("Sphinx error; {0}".format(e))
        recognition()


if __name__ == '__main__':
    recognition()
