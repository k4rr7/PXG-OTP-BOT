Descrição do Projeto

Este repositório foi criado para automações desenvolvidas em Python utilizando a biblioteca PyAutoGUI. O objetivo principal é automatizar tarefas específicas dentro do jogo de computador Pokexgames - PXG (Pokémon), e o OTPokemon, proporcionando uma experiência mais fluida e eficiente para os jogadores.

Funcionalidades do Bot

Bot de Hunt (Caçada)

O bot de Hunt automatiza a função de caçar dentro do jogo, permitindo que o personagem principal percorra toda a hunt (área de caça) e vença os mobs no caminho.
Utiliza as habilidades do Pokémon que o personagem carrega, coletando itens durante a jornada e utilizando poké-bolas para capturar os Pokémons encontrados.
Após completar o percurso, o bot retorna à posição inicial, aguarda alguns segundos e repete o ciclo até ser interrompido pelo usuário.

Bot de Pesca

O Bot de Pesca automatiza todo o processo de pesca no jogo, desde a escolha do local adequado até a captura do Pokémon aquático.
O bot realiza o minigame da pesca, utiliza as habilidades do Pokémon do personagem e coleta os itens dos Pokémons capturados, usando poké-bolas para a captura.
Caso o Pokémon que o personagem carrega sofra danos e tenha sua vida reduzida para o nível crítico, o bot utiliza automaticamente uma poção de recuperação.
Se o Pokémon morrer, o bot usa uma poção de reviver e continua o processo.
O ciclo de pesca é repetido até o usuário interromper a execução.

Requisitos
Sistema Operacional: Funciona em Windows 7, Windows 10 e Windows 11.
Bibliotecas: Utiliza a poderosa biblioteca PyAutoGUI para automação.
Como Usar
Instale o Python em seu computador.

Execute e seja feliz. Caso o programa não inicie, siga o tutorial para utilizar o bot atravez dos scripts Python!

Clone ou baixe este repositório para o seu ambiente local:

bash
Copiar
Editar
git clone https://github.com/k4rr7/Bot-Hunt-e-Pesca-PXG.git
Instale as dependências necessárias:

bash
Copiar
Editar
pip install -r requirements.txt
Execute o bot:

Para o bot de caçada (Hunt):

bash
Copiar
Editar
python bot_hunt.py
Para o bot de pesca:

bash
Copiar
Editar
python bot_pesca.py
Contribua com o Projeto
Estamos sempre trabalhando para melhorar e atualizar o Bot-Hunt-e-Pesca-PXG. Se você gostou do projeto ou tem sugestões para melhorias, não hesite em deixar uma estrela ⭐ no repositório. Isso nos motiva a continuar o desenvolvimento e trazer novas funcionalidades!

Se você deseja contribuir ou tem melhorias a sugerir, sinta-se à vontade para abrir uma issue ou enviar um pull request.
