# O que é uma Tool?

Uma Tool é uma função Python registrada no Servidor MCP.

Ela representa uma capacidade que pode ser utilizada por um Modelo de Linguagem.

Uma Tool:

- recebe parâmetros;
- executa uma ação;
- retorna um resultado.

Ela não é chamada diretamente pelo usuário.

Quem a executa é o Servidor MCP, após receber uma solicitação do Cliente MCP.

## O que aprendi

- Uma Tool é uma função Python comum.
- O decorator `@mcp.tool()` registra essa função no servidor.
- O Cliente MCP solicita a execução.
- O Servidor MCP executa a Tool.