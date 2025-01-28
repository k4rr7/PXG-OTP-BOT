# **Bot-Hunt-e-Pesca-PXG**

![Logo do Projeto](https://github.com/k4rr7/Bot-Hunt-e-Pesca-PXG/blob/main/imagens/logo.png)

**Repositório criado para automações feitas em Python utilizando a biblioteca PyAutoGUI, com o objetivo de automatizar tarefas dentro dos jogos **Pokexgames - PXG (Pokémon)** e **OTPokemon**. Este projeto visa proporcionar uma experiência mais fluida e eficiente para os jogadores.**

---

## **Funcionalidades do Bot**

### **Bot de Hunt (Caçada)**

O **Bot de Hunt** automatiza a função de caçar dentro do jogo, permitindo que o personagem principal percorra a **hunt** (área de caça) e vença todos os **mobs** no caminho. Ele utiliza as habilidades do **Pokémon** carregado pelo personagem, coleta itens durante a jornada e utiliza **poké-bolas** para capturar os **Pokémons** encontrados.

- **Processo automático**: Após completar o percurso, o bot retorna à posição inicial, aguarda alguns segundos e repete o ciclo até que o usuário decida interromper.
  
- **Compatibilidade**: Funciona em **Windows 7**, **Windows 10** e **Windows 11**.

### **Bot de Pesca**

O **Bot de Pesca** automatiza todo o processo de pesca no jogo, desde a escolha do local até a captura do **Pokémon aquático**. O bot realiza o minigame da pesca, utiliza as habilidades do Pokémon do personagem e coleta os itens dos **Pokémons** capturados, usando **poké-bolas** para a captura.

- **Recuperação automática**: Caso o Pokémon carregado sofra danos graves, o bot utiliza automaticamente uma **poção de recuperação**. 
- **Reviver Pokémon**: Se o Pokémon morrer, o bot usa uma **poção de reviver** e continua o ciclo até que o usuário interrompa.

---

## **Requisitos**

- **Sistema Operacional**: Funciona em **Windows 7**, **Windows 10** e **Windows 11**.
- **Bibliotecas**: Utiliza a poderosa biblioteca **PyAutoGUI** para automação de tarefas.

---

## **Como Usar**

### **1. Instale o Python**
Certifique-se de que o **Python** está instalado em seu computador. Se não estiver, [baixe e instale o Python aqui](https://www.python.org/downloads/).

### **2. Clone ou baixe o repositório**
Clone este repositório para o seu ambiente local:

```bash
git clone https://github.com/k4rr7/Bot-Hunt-e-Pesca-PXG.git

3. Instale as dependências necessárias
Após clonar o repositório, navegue até o diretório do projeto e instale as dependências:

cd Bot-Hunt-e-Pesca-PXG
pip install -r requirements.txt

4. Execute o bot
Para o bot de caçada (Hunt):

python bot_hunt.py

Para o bot de pesca:

python bot_pesca.py

Contribua com o Projeto
Estamos sempre trabalhando para melhorar e atualizar o Bot-Hunt-e-Pesca-PXG. Se você gostou do projeto ou tem sugestões para melhorias, deixe uma estrela ⭐ no repositório. Isso nos motiva a continuar o desenvolvimento e trazer novas funcionalidades!

Se você deseja contribuir, tem melhorias a sugerir ou encontrou algum bug, sinta-se à vontade para abrir uma issue ou enviar um pull request.
Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.

Autor: K4rr7
GitHub: https://github.com/k4rr7
