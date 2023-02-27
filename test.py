# import pyttsx3
# engine = pyttsx3.init()
#
# TTS_RATE = 100 # speed of tts
# # TTS_VOLUME = 1.0        # volume of tts
# TTS_GENDER = "Female"     # gender of tts (Male or Female)
# # """RATE"""
# rate = engine.getProperty('rate')   # getting details of current speaking rate
# engine.setProperty('rate', TTS_RATE)     # setting up new voice rate
# # """VOLUME"""
# # volume = engine.getProperty('volume')   # getting to know current volume level (min=0 and max=1)
# # engine.setProperty('volume', TTS_VOLUME)    # setting up volume level  between 0 and 1
# # """VOICES"""
# voices = engine.getProperty('voices')
# if TTS_GENDER == "Male":
#     voiceGenders = filter(lambda voices: voices.gender == 'VoiceGenderMale', voices)
# elif TTS_GENDER == "Female":
#     voiceGenders = filter(lambda voices: voices.gender == 'VoiceGenderFemale', voices)
# num = 0
# for voice in voiceGenders:
#     print(voice.languages)
#     if voice.languages == ['en_US']:
#         num += 1
#         engine.setProperty('voice', voice.id)
#
# print(num)
#
# # rate = engine.getProperty('rate')   # getting details of current speaking rate
# # print (rate)
# # engine.setProperty('rate', 100)
# #
# #
# # volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
# # print (volume)
# #
# #
# # voices = engine.getProperty('voices')       #getting details of current voice
# # #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
# # engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
#
# engine.say("Python is a great programming language")
# engine.runAndWait()


from os import system
system("say 'Hello World', how can i help you")