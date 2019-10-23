#!/usr/bin/env python3
import speech_recognition as sr
import pyttsx3
import rospy
from std_msgs.msg import String
# from std_msgs.msg import String

# engine.setProperty('voice', 'english-us')

# obtain audio from the microphone
r = sr.Recognizer()
pub = rospy.Publisher('rosMsg', String, queue_size=10)

rospy.init_node('voiceEngine', anonymous=True)
engine = pyttsx3.init()
engine.setProperty('rate', 150)    # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)  # Volume 0-1
# engine.setProperty('voice', 'english-us')

def recognition():
   
    with sr.Microphone() as source:
         rospy.loginfo('voice activation')
         rospy.loginfo(source)
         r.adjust_for_ambient_noise(source)
         audio = r.listen(source,timeout=100, phrase_time_limit=2)
        
    try:
        #print("Sphinx thinks you said " + r.recognize_sphinx(audio))
        
        strText = ""
        strText = str(r.recognize_google(audio,language="ko-KR"))
        rospy.loginfo(r.recognize_google(audio,language="ko-KR",show_all=True))
        #stt = r.recognize_google(audio)
        if '안녕' in strText:
            rospy.loginfo('gotoNLUprocess')
            doNLUprocess()
 
        # else if 'rb' in strText
        doNLUprocess()

        #engine.say(r.recognize_google(audio))
        # engine.runAndWait()
        # print("voiceEngine thinks you said " + r.recognize_google(audio))
        # recognition()
    except sr.UnknownValueError:
        #print("Sphinx could not understand audio")
        # engine.say("voiceEngine do not understand audio")
        # engine.runAndWait()
        recognition()
    except sr.RequestError as e:
        # engine.say("voiceEngine do not understand audio")
        # engine.runAndWait()
        print("Sphinx error; {0}".format(e))
        recognition()

def doNLUprocess():

    with sr.Microphone() as source:
        rospy.loginfo('nlu process')
        engine.say('     Say command!')
        engine.runAndWait()
        #engine.runAndWait()
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source,timeout=100, phrase_time_limit=2)
    try:

        rospy.loginfo(r.recognize_google(audio))

        strResult = ""
        strResult = str(r.recognize_google(audio,language="ko-KR"))
        rospy.loginfo(strResult)  
        #stt = r.recognize_google(audio)
        if '호밍' in strResult:
            rospy.loginfo('send deep learning')            
            rospy.loginfo('robot will go home')            
            pub.publish(1)
            engine.say('robot will go home')
            engine.runAndWait()
            recognition()
        if '포밍' in strResult:
            rospy.loginfo('send deep learning')            
            rospy.loginfo('robot will go home')            
            pub.publish(1)
            engine.say('robot will go home')
            engine.runAndWait()
            recognition()
        if '커밍' in strResult:
            rospy.loginfo('send deep learning')            
            rospy.loginfo('robot will go home')            
            pub.publish(1)
            engine.say('robot will go home')
            engine.runAndWait()
            recognition()

        if '캔' in strResult or '펜' in strResult :
            rospy.loginfo('send deep learning')            
            rospy.loginfo('robot will find can')            
            pub.publish("CAN")
            # engine.say("robot will find can")
            # engine.runAndWait()
            recognition()
        if '박스' in strResult or '팍스' in strResult :
            rospy.loginfo('send deep learning') 
            rospy.loginfo('robot will find plastic box')           
            pub.publish("BOX")
            engine.say("robot will find box")
            engine.runAndWait()
            recognition()
        if '비닐' in strResult or '빈닐' in strResult :
            rospy.loginfo('send deep learning')
            rospy.loginfo('robot will find plastic box')            
            pub.publish("plasticbox")
            engine.say("robot will find plastic box")
            engine.runAndWait()
            recognition()
        if '그만' in strResult or '정지' in strResult :
            rospy.loginfo('send deep learning')
            rospy.loginfo('voice engine will be paused')            
            pub.publish("stop")
            engine.say("voice engine will be paused")
            engine.runAndWait()
            recognition()
        

        doNLUprocess()
    except sr.UnknownValueError:
        #print("Sphinx could not understand audio")
        engine.say("voiceEngine do not understand audio")
        engine.runAndWait()
        doNLUprocess()
    except sr.RequestError as e:
        engine.say("voiceEngine do not understand audio")
        engine.runAndWait()
        print("Sphinx error; {0}".format(e))
        doNLUprocess()

if __name__ == '__main__':
   
    recognition()
