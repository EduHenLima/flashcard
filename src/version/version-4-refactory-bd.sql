ALTER TABLE assuntos
DROP COLUMN tipo;

ALTER TABLE cards
ADD respostas VARCHAR(255);

ALTER TABLE cards
ADD perguntas VARCHAR(255);

ALTER TABLE cards
DROP COLUMN id_pergunta;

ALTER TABLE cards
DROP COLUMN id_resposta;

ALTER TABLE usuarios
ADD email varchar(255);

ALTER TABLE usuarios
ADD uui integer;