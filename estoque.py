estoque = Estoque()

estoque.adicionar(Produto("Caneta", 10, 10))
estoque.adicionar(Produto("Lápis", 5, 20))

estoque.listar()

# Saída:
# Produto(nome='Caneta', preco=10, quantidade=10)
# Produto(nome='Lápis', preco=5, quantidade=20)

estoque.remover("Lápis")

estoque.listar()

# Saída:
# Produto(nome='Caneta', preco=10, quantidade=10)

estoque.atualizar_quantidade("Caneta", 20)

estoque.listar()

# Saída:
# Produto(nome='Caneta', preco=10, quantidade=20)
