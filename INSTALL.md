# **Instruções de Instalação - Perfect BOT**

Este guia irá ajudá-lo a configurar e executar o **Perfect BOT** diretamente em seu ambiente de desenvolvimento, caso o executável não funcione ou você prefira usar o código fonte em Python. 

---

## **Pré-requisitos**

Antes de começar, você precisará garantir que os seguintes programas estejam instalados em seu computador:

1. **Python 3.x**: O bot foi desenvolvido utilizando a linguagem Python. Você pode baixar a versão mais recente do Python no site oficial:

   [Baixar Python](https://www.python.org/downloads/)

2. **Pip**: O **pip** é o gerenciador de pacotes do Python, que você utilizará para instalar as dependências necessárias. O **pip** já deve ser instalado junto com o Python.

---

## **Passo 1: Clonando o Repositório**

Primeiro, você precisa clonar o repositório do bot para o seu computador. Abra o terminal ou o prompt de comando e execute o seguinte comando:

```bash
git clone https://github.com/k4rr7/PXG-OTP-BOT-2025.git

Passo 2: Instalando as Dependências
Após clonar o repositório, navegue até a pasta do projeto e instale as dependências necessárias. Execute os seguintes comandos:

No terminal (Linux/macOS) ou no Prompt de Comando (Windows):

cd Bot-Hunt-e-Pesca-PXG
pip install -r requirements.txt

Este comando irá instalar todas as bibliotecas necessárias para que o bot funcione corretamente. Caso o pip não esteja instalado, você pode instalá-lo com:

python -m ensurepip --upgrade


Passo 3: Executando o Bot
Agora que as dependências estão instaladas, você pode executar o bot. Escolha qual bot deseja rodar (Hunt ou Pesca):

Para o Bot de Caçada (Hunt): python bot_hunt.py
Para o Bot de Pesca: python bot_pesca.py

Passo 4: Problemas Comuns
Caso você tenha problemas ao executar o bot, aqui estão algumas dicas:

Certifique-se de que o Python esteja corretamente instalado: Execute o comando python --version no terminal para verificar se o Python está instalado. Caso não apareça a versão, siga as instruções do passo 1 para instalar o Python.

Instalar o PyAutoGUI manualmente: Caso o comando pip install -r requirements.txt falhe, tente instalar o PyAutoGUI manualmente com o seguinte comando: pip install pyautogui

Erros de dependências adicionais: Se aparecerem outros erros relacionados a pacotes, instale-os individualmente usando o pip. Por exemplo:

pip install pygetwindow
pip install pillow

Contribuições
Se você encontrou um bug ou tem sugestões para melhorar o bot, fique à vontade para abrir uma issue ou enviar um pull request no GitHub.

Autor: Karr7
GitHub: https://github.com/k4rr7



