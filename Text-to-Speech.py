def voice_speaks(output):
    c_hr, c_minu, c_m = tell_time()
    c_t = str(c_hr) + ":" + str(c_minu) + " " + str(c_m)
    print("Voice: ", output, "       ("+c_t+")")
    toSpeak = pyttsx3.init()
    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    toSpeak.setProperty('voice', voice_id)
    toSpeak.setProperty('rate', 165)
    toSpeak.setProperty('volume', 0.8)
    toSpeak.say(output)
    toSpeak.runAndWait()
