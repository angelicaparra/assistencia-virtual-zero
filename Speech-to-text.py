import speech_recognition as sr
from gtts import gTTS
import os
from datetime import datetime
import playsound
import pyjokes
import wikipedia
import webbrowser

def get_audio():
    r = sr.Recognizer()
    
    # APRIMORAMENTO 1: Ajuste fino nos limiares de voz
    r.dynamic_energy_threshold = True  # Permite que o Python adapte o ganho dinamicamente
    r.dynamic_energy_adjustment_damping = 0.15
    r.dynamic_energy_ratio = 1.5
    r.pause_threshold = 0.8  # Tempo de respiro entre as palavras
    
    # APRIMORAMENTO 2: Forçar taxa de amostragem padrão de 16000Hz (ideal para o Google)
    with sr.Microphone(sample_rate=16000) as source:
        print("\n[Assistente] Limpando ruído estático...")
        # Aumentamos para 1 segundo para uma filtragem mais pesada do ruído de fundo
        r.adjust_for_ambient_noise(source, duration=1.0)
        
        print("[Assistente] Pode falar agora, estou ouvindo em Português...")
        said = ""
        
        try:
            # Captura o áudio
            audio = r.listen(source, timeout=6, phrase_time_limit=6)
            print("[Assistente] Processando sua fala...")
            
            # Força o reconhecimento estrito em Português do Brasil
            said = r.recognize_google(audio, language='pt-BR')
            print(f"Você disse: {said}")
            
        except sr.WaitTimeoutError:
            print("[Aviso] Você não falou nada dentro do tempo limite.")
        except sr.UnknownValueError:
            print("[Erro] O Google ouviu um som, mas não reconheceu como palavras em Português.")
            speak("Não consegui entender, pode repetir de forma mais clara?")
        except sr.RequestError as e:
            print(f"[Erro] Falha na comunicação com os servidores do Google: {e}")
            speak("Estou com problemas para acessar a internet.")
            
    return said.lower()


def speak(text):
    print("Assistente: " + text)
    # Altere lang='pt' para português ou 'en' para inglês
    tts = gTTS(text=text, lang='pt', slow=False)
    filename = "voice.mp3"
    try:
        if os.path.exists(filename):
            os.remove(filename)
    except OSError:
        pass
    tts.save(filename)
    playsound.playsound(filename)

def respond(text):
    if 'youtube' in text:
        speak("O que você deseja buscar no YouTube?")
        keyword = get_audio()
        if keyword != '':
            url = f"https://www.youtube.com/results?search_query={keyword}"
            webbrowser.get().open(url)
            speak(f"Aqui está o que encontrei para {keyword} no YouTube.")
            
    elif 'pesquisar' in text or 'wikipedia' in text:
        speak("O que você quer pesquisar?")
        query = get_audio()
        if query != '':
            # Define o idioma do wikipedia para português
            wikipedia.set_lang("pt")
            try:
                result = wikipedia.summary(query, sentences=2)
                speak("De acordo com a Wikipédia:")
                speak(result)
            except wikipedia.exceptions.PageNotFoundError:
                speak("Não encontrei nenhuma página sobre isso.")
                
    elif 'piada' in text:
        # Nota: pyjokes costuma ser em inglês, mantive o padrão.
        speak("Lá vai uma piada.")
        speak(pyjokes.get_joke())
        
    elif 'horas' in text:
        strTime = datetime.today().strftime("%H:%M")
        speak(f"Agora são {strTime}")
        
    elif 'farmácia' in text or 'farmácia mais próxima' in text:
        speak("Buscando a farmácia mais próxima no Google Maps.")
        # Abre o navegador direto com o termo de busca baseado na localização do usuário
        url = "https://www.google.com/maps/search/farmacia+mais+proxima/"
        webbrowser.get().open(url)
        
    elif 'desligar' in text or 'sair' in text:
        speak("Até logo! Encerrando sistema.")
        exit()

# Inicialização do sistema
if __name__ == "__main__":
    speak("Sistema de assistência virtual iniciado.")
    while True:
        text = get_audio()
        if text != "":
            respond(text)