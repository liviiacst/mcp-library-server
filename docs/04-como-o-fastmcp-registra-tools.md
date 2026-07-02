# Como o FastMCP registra uma Tool?

Quando o Python carrega o módulo `server.py`, o decorator `@mcp.tool()` é executado.

Esse decorator registra a função no objeto `mcp`.

Dessa forma, quando um Cliente MCP pergunta quais capacidades o servidor possui, o servidor já conhece todas as Tools registradas.

## O que aprendi

- Decorators são executados durante o carregamento do módulo.
- O Servidor MCP mantém um registro das Tools.
- Apenas funções decoradas ficam disponíveis para o Cliente MCP.