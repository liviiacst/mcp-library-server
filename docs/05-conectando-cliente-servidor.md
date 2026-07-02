# Cliente e Servidor MCP

O Cliente MCP é responsável por conversar com o Servidor MCP.

O usuário conversa apenas com o Claude Desktop.

O Cliente MCP descobre automaticamente as capacidades disponibilizadas pelo servidor e pode solicitar a execução de Tools ou a leitura de Resources.

## Fluxo

Usuário

↓

Claude Desktop

↓

Cliente MCP

↓

Servidor MCP

↓

Tool ou Resource

## O que aprendi

- O usuário não conversa diretamente com o servidor.
- O Cliente MCP faz a comunicação.
- O servidor responde apenas às solicitações recebidas.