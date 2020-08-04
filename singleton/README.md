# Problema(s)
1. Única instância.
2. Única interface de acesso à instância.

```
a = A()
b = A()

id(a) == id(b)
```

# Exemplos
- Carrinho de compras.
- Acesso banco de dados/arquivo.
- Manter informações sobre jogo.