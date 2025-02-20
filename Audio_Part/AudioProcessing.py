import re
import pyttsx3

engine = pyttsx3.init() #create engine object.

#setting property for announcement.
engine.setProperty("volume",1.0)
engine.setProperty("rate",150)

def sainai_annoncement():
    
    #Alphabets
    thai_consonants = "ก-ฮ"
    thai_vowels = " ะาำิีึืุูเแโใไ็่้๊๋ั์"
    lower_eng_alphabets = "a-z"
    upper_eng_alphabets = "A-Z" 
    
    bus_number = input() #Input : Bus Number from detection.
     
    #In case : Thai Consonants or Vowels and English Alphabets.
    if re.match(f"[{thai_consonants},{thai_vowels},{lower_eng_alphabets},{upper_eng_alphabets}]",bus_number):
        error_detection_announcement()

    #In case : Bus number have only one digit.
    elif len(bus_number) == 1:
        if bool(int(bus_number)) == True:
            change_to_thai_language()
        
            engine.say("รถเมล์สาย {} กำลังจะมาถึงป้ายหยุดรถ ขอให้ท่านผู้โดยสาร โปรดเตรียมตัว".format(bus_number[0]))
            engine.runAndWait()
        
            bus_stop_announcement()
    
    #In case : Bus number have only two digits.
    elif len(bus_number) == 2:
        if bool(int(bus_number)) == True:
            change_to_thai_language()
        
            engine.say("รถเมล์สาย {} {} กำลังจะมาถึงป้ายหยุดรถ ขอให้ท่านผู้โดยสาร โปรดเตรียมตัว".format(bus_number[0], bus_number[1]))
            engine.runAndWait()
        
            bus_stop_announcement()
   
    #In case : Bus number have only three digits.
    elif len(bus_number) == 3:
        if bool(int(bus_number)) == True:
            change_to_thai_language()
        
            engine.say("รถเมล์สาย {} {} {} กำลังจะมาถึงป้ายหยุดรถ ขอให้ท่านผู้โดยสาร โปรดเตรียมตัว".format(bus_number[0], bus_number[1], bus_number[2]))
            engine.runAndWait()
        
            bus_stop_announcement()
    
    #In case : Bus number have three digits and have a special alphabet for annonce route.
    elif len(bus_number) == 4:
        if bus_number[3] == "L" or bus_number[3] == "l":
            change_to_thai_language()
        
            engine.say("รถเมล์สาย {} {} {} {} กำลังจะมาถึงป้ายหยุดรถ ขอให้ท่านผู้โดยสาร โปรดเตรียมตัว".format(bus_number[0], bus_number[1], bus_number[2],"วนซ้าย"))
            engine.runAndWait()
        
            bus_stop_announcement()
            
        '''else:  #In case Handle Error : Detection has a swapping index between alphabet and number.
            error_detection_announcement()'''
            
        if bus_number[3] == "R" or bus_number[3] == "r":
            change_to_thai_language()
        
            engine.say("รถเมล์สาย {} {} {} {} กำลังจะมาถึงป้ายหยุดรถ ขอให้ท่านผู้โดยสาร โปรดเตรียมตัว".format(bus_number[0], bus_number[1], bus_number[2],"วนขวา"))
            engine.runAndWait()
        
            bus_stop_announcement()
            
        '''else:  #In case Handle Error : Detection has a swapping index between alphabet and number.
            error_detection_announcement()'''
            
    '''else:
        error_detection_announcement()'''
        
#Future Plan : Link with YOLO MODEL
def bus_stop_announcement():
    engine.say("รถเมล์ของท่านมาถึงแล้ว")
    engine.runAndWait()
    engine.say("โปรดระมัดระวังขณะขึ้นขบวนรถ")
    engine.runAndWait()
        
def error_detection_announcement():
    #Set to default language
    voices = engine.getProperty("voices")
    engine.setProperty("voices",voices[0].id)
    #Error announcement
    engine.say("Error, Cannot detection bus number")
    engine.runAndWait()
    engine.say("Please try again")
    engine.runAndWait()

def change_to_thai_language():
    TH_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_THAI"
    engine.setProperty("voice",TH_voice_id)
    
try:
    sainai_annoncement()
except Exception as error:
    print("From this shit part :",error)
    error_detection_announcement()