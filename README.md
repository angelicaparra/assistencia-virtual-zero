# 🎙️ Assistente Virtual com Processamento de Linguagem Natural (PLN)

Este projeto foi desenvolvido como parte de um desafio prático da plataforma **DIO.me**, com o objetivo de construir um sistema de assistência virtual do zero utilizando Python e técnicas de Processamento de Linguagem Natural baseadas em regras.

## 🚀 Funcionalidades

O assistente interage totalmente em português (`pt-BR`) e executa as seguintes automações por comando de voz:
* **Ajuste Dinâmico de Ruído:** Calibração automática de 2 segundos para isolar barulhos de fundo do ambiente.
* **Consulta à Wikipédia:** Busca resumos de tópicos na Wikipédia e os lê em voz alta.
* **Automação no YouTube:** Pergunta o termo desejado e abre a página de busca do YouTube direto no navegador.
* **Geolocalização (Desafio):** Identifica e abre o Google Maps mostrando as farmácias mais próximas da região do usuário.
* **Informações de Tempo:** Informa o horário atualizado via áudio.

## 🛠️ Tecnologias Utilizadas

* **Python 3.12**
* **SpeechRecognition:** Para a captura e transcrição de áudio (Speech-to-Text).
* **gTTS (Google Text-to-Speech):** Para a conversão das respostas textuais em voz humana.
* **Playsound (v1.2.2):** Para a reprodução de arquivos de áudio locais de forma estável.
* **Wikipedia-API & Webbrowser:** Para pesquisas encadeadas e integração com o navegador.

## 📦 Como Executar o Projeto

### Pré-requisitos
Certifique-se de ter um microfone funcional configurado no seu sistema operacional.

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git](https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git)
   cd NOME_DO_REPOSITORIO


2. **Criar e Ativar a Máquina Virtual (venv)**

    ```bash
    python -m venv venv
    # Para ativar via Prompt de Comando (CMD):
    venv\Scripts\activate
    # Para ativar via PowerShell:
    .\venv\Scripts\Activate.ps1

3. **Instalar as Dependências**
    ```bash
    pip install -r requirements.txt

(Nota: Se houver erro de compilação no PyAudio do Windows, utilize pip install pipwin seguido de pipwin install pyaudio).

4. **Executar o Assistente**
    ```bash
    python Speech-to-text.py