# O que é um Decorator?

Um decorator é um recurso da linguagem Python que permite adicionar um comportamento a uma função sem modificar seu código.

No MCP, o decorator `@mcp.tool()` informa ao servidor que a função deve ser registrada como uma Tool.

A função continua sendo uma função Python comum, mas agora o Servidor MCP sabe que ela pode ser utilizada por um Cliente MCP.

## O que aprendi

- Decorators adicionam significado às funções.
- `@mcp.tool()` registra uma Tool no servidor.
- O decorator é executado quando o módulo é carregado.
- O Servidor MCP mantém um catálogo de Tools registradas.