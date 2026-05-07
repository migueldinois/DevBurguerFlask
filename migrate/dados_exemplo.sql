INSERT INTO produtos (produto, descricao, preco, destaque, foto, disponibilidade) VALUES
('Classic Cheese', 'Pão brioche, carne 180g e muito queijo cheddar derretido.', 22.00, 1, 'https://images.pexels.com/photos/1639557/pexels-photo-1639557.jpeg', 1),
('Bacon Blast', 'Hambúrguer bovino com fatias crocantes de bacon e molho barbecue.', 28.50, 1, 'https://images.pexels.com/photos/1251198/pexels-photo-1251198.jpeg', 1),
('Veggie aaaaaa', 'Hambúrguer de grão-de-bico com maionese de ervas e alface fresca.', 26.00, 0, 'https://images.pexels.com/photos/3607284/pexels-photo-3607284.jpeg', 1);


INSERT INTO itens_carrinho (cod_carrinho, cod_produto, quantidade) 
VALUES (1, 1, 1);

INSERT INTO carrinhos(usuario,finalizado)VALUES('patofivem2@gmail.com', 1)