# Teste de Lógica - WAAC

Leia primeiro toda a proposta, faça sua estimativa de horas do planejamento a ser realizado, explique a estratégia a ser seguida de acordo com as tecnologias que escolheu e envie um e-mail com o título **[Fullstack] Teste do Triângulo - Estimativa** para beawesome@waac.com.br com o link do seu git.
O primeiro commit é somente com o README.MD e esse arquivo será o seu documento técnico, portanto os processos de evolução precisam ser descritas e commitadas nesse arquivo. Tenha o hábito de commitar cada evolução ao longo da realização do projeto. Não suba o projeto no git apenas quando estiver pronto.

## O Desafio

Dado um triângulo de números, encontre o total máximo de cima para baixo.

## O triângulo

                6
            3       5
        9       7       1
    4       6       8       4    

    Nesse triângulo, o total máximo é 6 + 5 + 7 + 8 = 26.

## Requisitos

Um elemento só pode ser somando com um dos dois elementos mais próximos da próxima linha. Assim, o elemento 3 na linha 2 pode ser somado com 9 e 7, mas não com 1.

## A sua estratégia

Escolha a linguagem de programação desejada e deixo nos saber a sua estratégia por trás da eleboração do problema.

## Parâmetros de entrada e de saída

Seu código receberá uma lista multidimensional como parametro. O triangulo do exemplo receberá, então: [[6],[3,5],[9,7,1],[4,6,8,4]].

<br>

# Instalação do projeto

> - Este projeto foi construido em imagens Docker, é necessário ter o Docker instalado em sua máquina previamente.

<br>

# Como rodar o projeto: 

## Passo 1

Após clonar o projeto em sua máquina navegue até o diretório raiz do projeto:

```bash
  cd Teste-Full-Stack-Developer
```

## Passo 2

Execute o seguinte comando para buildar a imagem docker em flask:

```bash
  docker build -t triangle_app . 
```

## Passo 3

Execute o seguinte comando para rodar seu projeto na porta 5000:

```bash
   docker run -p 5000:5000 triangle_app 
```

## Pronto!!

Agora basta acessar o endereço local com a porta 5000:

```bash
   http://localhost:5000/
```