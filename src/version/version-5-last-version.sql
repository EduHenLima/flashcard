ALTER TABLE `flashcards`.`usuarios`
CHANGE COLUMN `id_usuaario` `id_usuario` INT NOT NULL AUTO_INCREMENT ;

ALTER TABLE `flashcards`.`categorias`
DROP FOREIGN KEY `fk_categorias_1`;
ALTER TABLE `flashcards`.`categorias`
CHANGE COLUMN `id_usuario` `id_usuario` INT NOT NULL ,
CHANGE COLUMN `nome_categoria` `nome_categoria` VARCHAR(255) NOT NULL ;
ALTER TABLE `flashcards`.`categorias`
ADD CONSTRAINT `fk_categorias_1`
  FOREIGN KEY (`id_usuario`)
  REFERENCES `flashcards`.`usuarios` (`id_usuario`);


ALTER TABLE `flashcards`.`cards`
CHANGE COLUMN `pergunta` `pergunta` VARCHAR(255) NULL DEFAULT NULL AFTER `id_assunto`,
CHANGE COLUMN `resposta` `resposta` VARCHAR(255) NULL DEFAULT NULL AFTER `pergunta`;

ALTER TABLE `flashcards`.`cards`
CHANGE COLUMN `id_cards` `id_card` INT NOT NULL AUTO_INCREMENT ;

ALTER TABLE `flashcards`.`assuntos`
DROP FOREIGN KEY `fk_assuntos_1`;
ALTER TABLE `flashcards`.`assuntos`
CHANGE COLUMN `id_categoria` `id_categoria` INT NOT NULL ;
ALTER TABLE `flashcards`.`assuntos`
ADD CONSTRAINT `fk_assuntos_1`
  FOREIGN KEY (`id_categoria`)
  REFERENCES `flashcards`.`categorias` (`id_categoria`);
