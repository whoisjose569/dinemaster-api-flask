# Projeto de Estudo - DineMaster

Este é um projeto de estudo focado no desenvolvimento de uma API para um sistema de gerenciamento de restaurante. A ideia principal é entender como implementar funcionalidades de controle de mesas, pedidos e itens do cardápio utilizando boas práticas de arquitetura, como **MVC** e **Clean Architecture**.

## Funcionalidades Iniciais

### Modelos (Models)
- **Mesas**: Tabela para armazenar informações sobre as mesas.
- **Pedidos**: Tabela para registrar os pedidos feitos, com status e associando-os às mesas.
- **Itens do Cardápio**: Tabela para listar os itens do cardápio disponíveis no restaurante.
- **Flask-SQLAlchemy** será utilizado para mapear as tabelas no banco de dados.

### Controladores (Controllers)
- **Rotas** para:
  - Criar, editar e remover **itens do cardápio**.
  - **Gerenciar pedidos** (criar novos pedidos, atualizar status e associar mesas).
  - **Atualizar status das mesas** (ocupada, reservada, livre).
  
### Visualizações (Views)
- Uso do Flask para retornar respostas **JSON**.
- Respostas organizadas de acordo com os padrões de uma API **RESTful**.

### Autenticação
- Implementação de **JWT token** para autenticação de usuários e segurança nas rotas.

## Objetivo

Este projeto tem o objetivo de estudar os seguintes conceitos:

- **MVC** (Model-View-Controller)
- **JWT Authentication**
- **Estrutura de API RESTful**
- **Boas práticas de refatoração e organização de código**

## Tecnologias Usadas

- **Flask**: Framework web utilizado.
- **Flask-SQLAlchemy**: Para interação com o banco de dados.
- **Marshmallow**: Para validação e serialização de dados.
- **JWT**: Para autenticação de usuários.


## Contribuições

Este projeto está sendo desenvolvido como parte de um **projeto de estudo**, com o objetivo de aprender e aplicar boas práticas de desenvolvimento de software.
