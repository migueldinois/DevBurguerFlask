    CREATE DATABASE IF NOT EXISTS DevBurguer;
    USE DevBurguer;

    CREATE TABLE IF NOT EXISTS produtos (
        codigo int AUTO_INCREMENT PRIMARY KEY,
        produto varchar(60) NOT NULL,
        descricao varchar(1000),
        preco float,
        destaque bool default 0,
        foto varchar(256),
        disponibilidade bool default 1
    );

CREATE TABLE IF NOT EXISTS usuarios (
    codigo INT AUTO_INCREMENT,
    nome VARCHAR(60) NOT NULL,
    usuario VARCHAR(32) NOT NULL PRIMARY KEY,
    senha VARCHAR(60) NOT NULL,
    UNIQUE KEY (codigo)
);

CREATE TABLE IF NOT EXISTS carrinhos (
	cod_carrinho INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(20),
    data datetime default current_timestamp,
    finalizado bool,
    constraint fk_carrinho_usuario FOREIGN KEY (usuario) REFERENCES usuarios(usuario)
);
    
CREATE TABLE IF NOT EXISTS itens_carrinho (
	cod_itens_carrinho INT AUTO_INCREMENT PRIMARY KEY,
    cod_carrinho int,
    cod_produto int,
    quantidade int default 1,
    constraint fk_carrinho_carrinhos foreign key (cod_carrinho) references carrinhos(cod_carrinho),
    constraint fk_itens_carrinho_itens foreign key (cod_produto) references produtos (codigo)
);
