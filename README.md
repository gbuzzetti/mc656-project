# mc656-project
Projeto de Engenharia de Software - UNICAMP, 2s2024

O projeto a ser desenvolvido é uma aplicação na área de saúde e bem-estar que auxilia no monitoramento de saúde da pessoa, fornecendo dicas nutricionais, índices de caloria, quantidade de água recomendada, etc.

## Integrantes da equipe:

* Isaac do Nascimento Oliveira, 247175
* Elton Aquino de Brito Filho, 247059
* Giovanni Mesquita Micaroni, 231702
* Guilherme Buzzetti de Souza, 235883
* Guilherme Azevedo Horn, 247127

## Diagrama de Componentes da Arquitetura do Projeto

<img src="images/Mapa conceitual.jpeg" alt="Mapa conceitual" width="700" align="center">

Para a criação desse projeto, levamos em consideraçao o Estilo Arquitetural em Camadas. Nesse modelo, o sistema é dividido em diversas camadas, onde cada camada tem uma responsabilidade bem definida e interage com as camadas adjacentes para cumprir seus objetivos.

### Descrição dos principais Componentes

1. User Interface Layer (Interface do Usuário)

    Responsabilidade: Exibir as páginas da web e permitir a interação com o usuário.
    Componentes:
        Templates:
            home.html: Página inicial do aplicativo, com informações gerais.
            calories.html: Exibe os resultados do cálculo de calorias.
            water.html: Mostra as recomendações de ingestão de água.
        Static:
            layout.css: Define o estilo visual do aplicativo.
            script.js: Contém a lógica de interação via JavaScript.

2. Logical Layer (Camada de Lógica)

    Responsabilidade: Contém a lógica central do sistema, realizando cálculos e decisões baseadas nas entradas do usuário.
    Componentes:
        Água:
            recomendacao_agua.py: Calcula a quantidade de água recomendada com base no peso e nível de atividade do usuário.
        Calorias:
            calculo_calorias_diarias.py: Realiza o cálculo das calorias diárias necessárias com base em dados do usuário (peso, altura, idade, etc.).
        IMC:
            calculo_imc.py: Calcula o Índice de Massa Corporal (IMC) com base no peso e altura do usuário.

3. Routing Layer (Roteamento)

    Responsabilidade: Gerenciar as rotas do aplicativo e redirecionar as requisições para os componentes apropriados.
    Componentes:
        routes.py: Define as rotas HTTP e conecta as páginas (templates) com as funções da lógica de negócio (features).

4. Execution Layer (Configuração e Execução)

    Responsabilidade: Configurar e executar o aplicativo, incluindo configurações iniciais e o processo de inicialização do servidor.
    Componentes:
        config.py: Contém as configurações do aplicativo, como chaves de API, configuração do banco de dados, etc.
        run.py: Inicia o aplicativo, configurando o servidor e executando a aplicação Flask.
        create_db_app.py: Inicia o Bando de Dados para o armazenamento dos Logins dos Usuários.

5. Testing Layer (Testes)

    Responsabilidade: Garantir que todas as funcionalidades estejam corretas por meio de testes unitários.
    Componentes:
        test_calculo_imc.py: Testes para a funcionalidade de cálculo do IMC.
        test_calorias.py: Testes para o cálculo de calorias diárias.
        test_rec_agua.py: Testes para as recomendações de ingestão de água.