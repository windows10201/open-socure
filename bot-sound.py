
 #---------------𝗪𝗔𝗦𝗜𝗠 𝗕𝗢𝗧 𝗦𝗢𝗨𝗡𝗗--------------#



import os
os.system("pkg install play-audio")
try:
#𝗪𝗔𝗦𝗜𝗠 𝗕𝗢𝗧 𝗦𝗢𝗨𝗡𝗗
      import gtts
except:
        os.system("pip install gtts")
        import gtts
from gtts import gTTS
#𝗪𝗔𝗦𝗜𝗠 𝗕𝗢𝗧 𝗦𝗢𝗨𝗡𝗗
def create_(text,file):            #𝗪𝗔𝗦𝗜𝗠 𝗕𝗢𝗧 𝗦𝗢𝗨𝗡𝗗
       my_a=gTTS(text)
       my_a.save(file)


def play_audio(audio_file):
       os.system("play-audio "+audio_file)
#𝗪𝗔𝗦𝗜𝗠 𝗕𝗢𝗧 𝗦𝗢𝗨𝗡𝗗
def wasim(text,file):
       create_(text,file)
       play_audio(file)
       
 #---------------𝗪𝗔𝗦𝗜𝗠 𝗕𝗢𝗧 𝗦𝗢𝗨𝗡𝗗--------------#
       
       wasim("হ্যালো। কি।খবর।তোমাদের।এ।আই।ভয়েস।র্কোড।বানানো।শেষ।ভিডিও।দিবো।কেমনে।টারমাক্স।নিজের।কমান্ডে।এআই।ভয়েস।লাগাবে.","I.mp3")