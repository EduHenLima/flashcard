ALTER TABLE `flashcards`.`categorias`
CHANGE COLUMN `id_categoria` `id_categoria` INT NOT NULL AUTO_INCREMENT ;

ALTER TABLE `flashcards`.`cards`
CHANGE COLUMN `id_cards` `id_cards` INT NOT NULL AUTO_INCREMENT ;

ALTER TABLE `flashcards`.`pergunta`
CHANGE COLUMN `id_pergunta` `id_pergunta` INT NOT NULL AUTO_INCREMENT ;

ALTER TABLE `flashcards`.`resposta`
CHANGE COLUMN `id_resposta` `id_resposta` INT NOT NULL AUTO_INCREMENT ;

ALTER TABLE `flashcards`.`usuarios`
CHANGE COLUMN `id_usuário` `id_usuário` INT NOT NULL AUTO_INCREMENT ;

ALTER TABLE `flashcards`.`assuntos`
CHANGE COLUMN `id_assunto` `id_assunto` INT NOT NULL AUTO_INCREMENT ;
