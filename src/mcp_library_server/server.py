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

@mcp.resource("library://authors")
def list_authors() -> str:
    """
    Retorna a lista de autores disponíveis.
    """
    return """
        Robert C. Martin
        Martin Fowler
        Erich Gamma
        Kent Beck
        """

def main():
    print("Iniciando Library Server...")
    print(mcp.__dict__)
    mcp.run()