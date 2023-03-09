import speech_recognition as sr
import subprocess as sub
import pyttsx3, pywhatkit, wikipedia, datetime, keyboard, colors, os
from pygame import mixer

name = "juanita"
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)
engine.setProperty('rate', 145)

sites={
    'google':'google.com',
    'youtube':'youtube.com',
    'facebook':'facebook.com',
    'whatsapp':'web.whatsapp.com',
    'cursos':'freecodecamp.org/learn'
}

files = {
    'documento':'SALUDO.docx',
    'cédula':'Con papeleta de votación.pdf',
    'imagen':'SPIDER-MAN-PS5_3840x2160.jpg'
}

programs = {
    'matlab': r"C:\Program Files\MATLAB\R2022b\bin\matlab.exe",
    'zoom': r"C:\Users\ALEJANDRO\AppData\Roaming\Zoom\bin\Zoom.exe",
    'word': r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
    'excel': r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",
    'steam': r"C:\Program Files (x86)\Steam\steam.exe"
}

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Te escuchando...")
            pc = listener.listen(source)
            rec = listener.recognize_google(pc, language = "es")
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name,'')

    except:
        pass
    return rec

def run_juanita():
    while True:
        rec = listen()
        if 'reproduce' in rec:
            music = rec.replace('reproduce','')
            print("Reproduciendo " + music)
            talk("Reproduciendo " + music)
            pywhatkit.playonyt(music)
        elif 'busca' in rec:
            search = rec.replace('busca','')
            wikipedia.set_lang("es")
            wiki = wikipedia.summary(search, 1)
            print(search +": " + wiki)
            talk(wiki)
        elif 'alarma' in rec:
            num = rec.replace('alarma','')
            num = num.strip()
            talk("Alarma activada a las "+num+ " horas")
            while True:
                if datetime.datetime.now().strftime('%H:%M') == num:
                    print("Despierta!!!")
                    mixer.init()
                    mixer.music.load("alarma.mp3")
                    mixer.music.play()
                    if keyboard.read_key() == "s":
                        mixer.music.stop()
                        break
        elif 'colores' in rec:
            talk('Enseguida')
            colors.capture()
        elif 'abre' in rec:
            for site in sites:
                if site in rec:
                    sub.call(f'start chrome.exe {sites[site]}', shell=True)
                    talk(f'Abriendo {site}')
            for app in programs:
                if app in rec:
                    talk(f'Abriendo {app}')
                    os.startfile(programs[app])
        elif 'archivo' in rec:
            for file in files:
                if file in rec:
                    sub.Popen([files[file]], shell=True)
                    talk(f'Abrindo {file}')
        elif 'escribe' in rec:
            try:
                with open("nota.txt", 'a') as f:
                    write(f)
            except FileNotFoundError as e:
                file = open("nota.txt", 'a')
                write(file)
        elif 'termina' in rec:
            talk('Fue un placer ayudarte.Adiós!')
            break



def write(f):
    talk("¿Qué quieres que escriba?")
    rec_write = listen()
    f.write(rec_write + os.linesep)
    f.close()
    talk("Listo, puedes revisarlo")
    sub.Popen("nota.txt", shell=True)

    


if __name__ == '__main__':
    run_juanita()

