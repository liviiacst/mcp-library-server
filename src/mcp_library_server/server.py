from mcp.server.fastmcp import FastMCP

# Criamos o servidor MCP
mcp = FastMCP("Library Server")

# Decorator (Servidor, registre a próxima função como uma Tool)
@mcp.tool()
def say_hello(name: str) -> str:
    """
    Retorna uma saudação para o usuário.
    """
    return f"Olá, {name}! Bem-vindo ao MCP."


def main():
    print("Iniciando Library Server...")
    print(mcp.__dict__)
    mcp.run()