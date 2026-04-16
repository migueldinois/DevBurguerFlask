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
        codigo int AUTO_INCREMENT ,
        nome varchar(60) NOT NULL,
        usuario varchar(32) NOT NULL PRIMARY KEY,
        senha varchar(60) NOT NULL
    );
