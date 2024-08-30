create database cadastro_cliente; -- criando o banco de dados cadastro cliente
use cadastro_cliente; -- alterando para usável



create table estado (
id_estado int auto_increment primary key, -- adicionei auto_increment para ter sempre um id próprio da tabela estado
Estado varchar (100) -- criação do elemennto Estado para os nomes dos Estados: 100 caracteres para justa posição
);

create table cidade (
id_cidade int auto_increment primary key, -- adicionei auto_increment para ter sempre um id próprio da tabela cidade
Cidade varchar (100), -- criação do elemento Cidade para os nomes das Cidades: 100 caracteres para justa posição
id_estado int,
foreign key fk_estado (id_estado) references estado (id_estado) -- criando a chave estrageira para sua atribuição de cidades e estados
);

create table sexo (
id_sexo int auto_increment primary key, -- adicionei auto_increment para ter sempre um id próprio da tabela sexo
Sexo varchar (12) -- criação do elemento Sexo para os tipos de sexo existentes: 12 caracteres para justa posição
);

create table nacionalidade (
id_nacionalidade int auto_increment primary key, -- adicionei auto_increment para ter sempre um id próprio da tabela nacionalidade
Nacionalidade varchar (12) -- criação do elemento Nacionalidade para exemplificar sua nacionalidade: 12 caracteres para justa posição
);

create table raca (
id_raca int auto_increment primary key, -- adicionei auto_increment para ter sempre um id próprio da tabela raça
Raca varchar (12) -- criação do elemento Raça para os tipos de raças existentes: 12 caracteres para justa posição
);

create table escolaridade (
id_escolaridade int auto_increment primary key, -- adicionei auto_increment para ter sempre um id próprio da tabela escolaridade
Escolaridade varchar (32) -- criação do elemento Escolaridade para o tipo de escolaridade: 32 digitos para justa posição
);
create table cliente (
id_cliente int auto_increment primary key, -- adicionei auto_increment para ter sempre um id próprio da tabela cliente
cpf varchar (14), -- criei o elemento cpf: 11 caracteres para justa posição 
nome varchar (50), -- criei o elemento nome: 50 caracteres para justa posição
rg varchar (12), -- criei o elemento rg: 9 caracteres para justa posição
id_cidade int null,
id_estado int null,
id_sexo int null,
id_nacionalidade int null,
id_raca int null,
id_escolaridade int null,
foreign key id_estado (id_estado) references cidade (id_estado),
foreign key id_cidade (id_cidade) references cidade (id_cidade), -- chave estrageira de cidades
foreign key id_sexo (id_sexo) references sexo (id_sexo), -- chave estrangeira de tipos de sexo
foreign key id_nacionalidade (id_nacionalidade) references nacionalidade (id_nacionalidade), -- chave estrangeira de nacionalidade
foreign key id_raca (id_raca) references raca (id_raca), -- chave estrangeira de tipos de raças
foreign key id_escolaridade (id_escolaridade) references escolaridade (id_escolaridade) -- chave estrangeira para matricula escolar
);

show tables;

INSERT INTO cliente (cpf, nome, rg, id_cidade, id_sexo, id_nacionalidade, id_raca, id_escolaridade)
VALUES 
('123.456.789-01', 'Alek Vinicius Correia', '1.234.567', 1, 1, 1, 2, 4),  -- Cidade: Rio Branco, Sexo: Masc, Nacionalidade: Brasileira, Raça: Branco, Escolaridade: Superior (Graduação)
('234.567.890-12', 'Ana Vasques', '2.345.678', 2, 2, 1, 1, 3),  -- Cidade: Maceió, Sexo: Fem, Nacionalidade: Brasileira, Raça: Preta, Escolaridade: Médio
('345.678.901-23', 'Davi Bueno', '3.456.789', 3, 1, 2, 3, 1),  -- Cidade: Macapá, Sexo: Masc, Nacionalidade: Estrangeira, Raça: Parda, Escolaridade: Fundamental
('456.789.012-34', 'Rafaela Camposano', '4.567.890', 4, 2, 1, 4, 5),  -- Cidade: Manaus, Sexo: Fem, Nacionalidade: Brasileira, Raça: Amarela, Escolaridade: Pós-Graduação
('567.890.123-45', 'Elias Oliveira', '5.678.901', 5, 1, 1, 5, 6),  -- Cidade: Salvador, Sexo: Masc, Nacionalidade: Brasileira, Raça: Indígena, Escolaridade: Mestrado
('678.901.234-56', 'Juliana Almeida', '6.789.012', 6, 2, 2, 1, 3),  -- Cidade: Fortaleza, Sexo: Fem, Nacionalidade: Estrangeira, Raça: Preta, Escolaridade: Médio
('789.012.345-67', 'Paulo Silva', '7.890.123', 7, 1, 1, 2, 4),  -- Cidade: Brasília, Sexo: Masc, Nacionalidade: Brasileira, Raça: Branco, Escolaridade: Superior (Graduação)
('890.123.456-78', 'Fernanda Lima', '8.901.234', 8, 2, 2, 3, 1),  -- Cidade: Vitória, Sexo: Fem, Nacionalidade: Estrangeira, Raça: Parda, Escolaridade: Fundamental
('901.234.567-89', 'Lucas Martins', '9.012.345', 9, 1, 1, 4, 6),  -- Cidade: Goiânia, Sexo: Masc, Nacionalidade: Brasileira, Raça: Amarela, Escolaridade: Mestrado
('012.345.678-90', 'Mariana Souza', '0.123.456', 10, 2, 1, 5, 5),  -- Cidade: São Luís, Sexo: Fem, Nacionalidade: Brasileira, Raça: Indígena, Escolaridade: Pós-Graduação
('123.654.789-01', 'Gabriel Fernandes', '1.234.567', 11, 1, 2, 1, 2),  -- Cidade: Cuiabá, Sexo: Masc, Nacionalidade: Estrangeira, Raça: Preta, Escolaridade: Médio
('234.765.890-12', 'Tatiane Rodrigues', '2.345.678', 12, 2, 1, 2, 3),  -- Cidade: Campo Grande, Sexo: Fem, Nacionalidade: Brasileira, Raça: Preta, Escolaridade: Médio
('345.876.901-23', 'Ricardo Oliveira', '3.456.789', 13, 1, 2, 3, 4),  -- Cidade: Belo Horizonte, Sexo: Masc, Nacionalidade: Estrangeira, Raça: Parda, Escolaridade: Superior (Graduação)
('456.987.012-34', 'Larissa Carvalho', '4.567.890', 14, 2, 1, 4, 5),  -- Cidade: Belém, Sexo: Fem, Nacionalidade: Brasileira, Raça: Amarela, Escolaridade: Pós-Graduação
('567.098.123-45', 'André Silva', '5.678.901', 15, 1, 2, 5, 6),  -- Cidade: João Pessoa, Sexo: Masc, Nacionalidade: Estrangeira, Raça: Indígena, Escolaridade: Mestrado
('678.109.234-56', 'Camila Rocha', '6.789.012', 16, 2, 1, 1, 1),  -- Cidade: Curitiba, Sexo: Fem, Nacionalidade: Brasileira, Raça: Preta, Escolaridade: Fundamental
('789.210.345-67', 'Rodrigo Azevedo', '7.890.123', 17, 1, 2, 2, 3),  -- Cidade: Recife, Sexo: Masc, Nacionalidade: Estrangeira, Raça: Preta, Escolaridade: Médio
('890.321.456-78', 'Julio Campos', '8.901.234', 18, 2, 1, 3, 4),  -- Cidade: Teresina, Sexo: Fem, Nacionalidade: Brasileira, Raça: Parda, Escolaridade: Superior (Graduação)
('901.432.567-89', 'Tatiane Costa', '9.012.345', 19, 1, 2, 4, 5),  -- Cidade: Rio de Janeiro, Sexo: Masc, Nacionalidade: Estrangeira, Raça: Amarela, Escolaridade: Pós-Graduação
('012.543.678-90', 'Sofia Nunes', '0.123.456', 20, 2, 1, 5, 6);  -- Cidade: Natal, Sexo: Fem, Nacionalidade: Brasileira, Raça: Indígena, Escolaridade: Mestrado

INSERT INTO estado (id_estado,Estado) VALUES
(null, 'Acre'),
(null, 'Alagoas'),
(null, 'Amapá'),
(null, 'Amazonas'),
(null, 'Bahia'),
(null, 'Ceará'),
(null, 'Distrito Federal'),
(null, 'Espírito Santo'),
(null, 'Goiás'),
(null, 'Maranhão'),
(null, 'Mato Grosso'),
(null, 'Mato Grosso do Sul'),
(null, 'Minas Gerais'),
(null, 'Pará'),
(null, 'Paraíba'),
(null, 'Paraná'),
(null, 'Pernambuco'),
(null, 'Piauí'),
(null, 'Rio de Janeiro'),
(null, 'Rio Grande do Norte'),
(null, 'Rio Grande do Sul'),
(null, 'Rondônia'),
(null, 'Roraima'),
(null, 'Santa Catarina'),
(null, 'São Paulo'),
(null, 'Sergipe'),
(null, 'Tocantins');

-- Acre (ID fictício: 1)
INSERT INTO cidade VALUES (null, "Rio Branco", 1);
INSERT INTO cidade VALUES (null, "Cruzeiro do Sul", 1);
INSERT INTO cidade VALUES (null, "Sena Madureira", 1);
INSERT INTO cidade VALUES (null, "Tarauacá", 1);
INSERT INTO cidade VALUES (null, "Feijó", 1);

-- Alagoas (ID fictício: 2)
INSERT INTO cidade VALUES (null, "Maceió", 2);
INSERT INTO cidade VALUES (null, "Arapiraca", 2);
INSERT INTO cidade VALUES (null, "Palmeira dos Índios", 2);
INSERT INTO cidade VALUES (null, "Penedo", 2);
INSERT INTO cidade VALUES (null, "São Miguel dos Campos", 2);

-- Amapá (ID fictício: 3)
INSERT INTO cidade VALUES (null, "Macapá", 3);
INSERT INTO cidade VALUES (null, "Santana", 3);
INSERT INTO cidade VALUES (null, "Laranjal do Jari", 3);
INSERT INTO cidade VALUES (null, "Oiapoque", 3);
INSERT INTO cidade VALUES (null, "Porto Grande", 3);

-- Amazonas (ID fictício: 4)
INSERT INTO cidade VALUES (null, "Manaus", 4);
INSERT INTO cidade VALUES (null, "Parintins", 4);
INSERT INTO cidade VALUES (null, "Itacoatiara", 4);
INSERT INTO cidade VALUES (null, "Tabatinga", 4);
INSERT INTO cidade VALUES (null, "Tefé", 4);

-- Bahia (ID fictício: 5)
INSERT INTO cidade VALUES (null, "Salvador", 5);
INSERT INTO cidade VALUES (null, "Feira de Santana", 5);
INSERT INTO cidade VALUES (null, "Vitória da Conquista", 5);
INSERT INTO cidade VALUES (null, "Ilhéus", 5);
INSERT INTO cidade VALUES (null, "Eunápolis", 5);

-- Ceará (ID fictício: 6)
INSERT INTO cidade VALUES (null, "Fortaleza", 6);
INSERT INTO cidade VALUES (null, "Caucaia", 6);
INSERT INTO cidade VALUES (null, "Sobral", 6);
INSERT INTO cidade VALUES (null, "Juazeiro do Norte", 6);
INSERT INTO cidade VALUES (null, "Crato", 6);

-- Distrito Federal (ID fictício: 7)
INSERT INTO cidade VALUES (null, "Brasília", 7);
INSERT INTO cidade VALUES (null, "Gama", 7);
INSERT INTO cidade VALUES (null, "Taguatinga", 7);
INSERT INTO cidade VALUES (null, "Ceilândia", 7);
INSERT INTO cidade VALUES (null, "Planaltina", 7);

-- Espírito Santo (ID fictício: 8)
INSERT INTO cidade VALUES (null, "Vitória", 8);
INSERT INTO cidade VALUES (null, "Vila Velha", 8);
INSERT INTO cidade VALUES (null, "Serra", 8);
INSERT INTO cidade VALUES (null, "Cariacica", 8);
INSERT INTO cidade VALUES (null, "Colatina", 8);

-- Goiás (ID fictício: 9)
INSERT INTO cidade VALUES (null, "Goiânia", 9);
INSERT INTO cidade VALUES (null, "Anápolis", 9);
INSERT INTO cidade VALUES (null, "Rio Verde", 9);
INSERT INTO cidade VALUES (null, "Aparecida de Goiânia", 9);
INSERT INTO cidade VALUES (null, "Catalão", 9);

-- Maranhão (ID fictício: 10)
INSERT INTO cidade VALUES (null, "São Luís", 10);
INSERT INTO cidade VALUES (null, "Imperatriz", 10);
INSERT INTO cidade VALUES (null, "Caxias", 10);
INSERT INTO cidade VALUES (null, "Timon", 10);
INSERT INTO cidade VALUES (null, "Codó", 10);

-- Mato Grosso (ID fictício: 11)
INSERT INTO cidade VALUES (null, "Cuiabá", 11);
INSERT INTO cidade VALUES (null, "Várzea Grande", 11);
INSERT INTO cidade VALUES (null, "Rondonópolis", 11);
INSERT INTO cidade VALUES (null, "Sinop", 11);
INSERT INTO cidade VALUES (null, "Tangará da Serra", 11);

-- Mato Grosso do Sul (ID fictício: 12)
INSERT INTO cidade VALUES (null, "Campo Grande", 12);
INSERT INTO cidade VALUES (null, "Dourados", 12);
INSERT INTO cidade VALUES (null, "Três Lagoas", 12);
INSERT INTO cidade VALUES (null, "Corumbá", 12);
INSERT INTO cidade VALUES (null, "Ponta Porã", 12);

-- Minas Gerais (ID fictício: 13)
INSERT INTO cidade VALUES (null, "Belo Horizonte", 13);
INSERT INTO cidade VALUES (null, "Uberlândia", 13);
INSERT INTO cidade VALUES (null, "Contagem", 13);
INSERT INTO cidade VALUES (null, "Juiz de Fora", 13);
INSERT INTO cidade VALUES (null, "Montes Claros", 13);

-- Pará (ID fictício: 14)
INSERT INTO cidade VALUES (null, "Belém", 14);
INSERT INTO cidade VALUES (null, "Ananindeua", 14);
INSERT INTO cidade VALUES (null, "Santarém", 14);
INSERT INTO cidade VALUES (null, "Marabá", 14);
INSERT INTO cidade VALUES (null, "Altamira", 14);

-- Paraíba (ID fictício: 15)
INSERT INTO cidade VALUES (null, "João Pessoa", 15);
INSERT INTO cidade VALUES (null, "Campina Grande", 15);
INSERT INTO cidade VALUES (null, "Santa Rita", 15);
INSERT INTO cidade VALUES (null, "Patos", 15);
INSERT INTO cidade VALUES (null, "Bayeux", 15);

-- Paraná (ID fictício: 16)
INSERT INTO cidade VALUES (null, "Curitiba", 16);
INSERT INTO cidade VALUES (null, "Londrina", 16);
INSERT INTO cidade VALUES (null, "Maringá", 16);
INSERT INTO cidade VALUES (null, "Ponta Grossa", 16);
INSERT INTO cidade VALUES (null, "Cascavel", 16);

-- Pernambuco (ID fictício: 17)
INSERT INTO cidade VALUES (null, "Recife", 17);
INSERT INTO cidade VALUES (null, "Olinda", 17);
INSERT INTO cidade VALUES (null, "Jaboatão dos Guararapes", 17);
INSERT INTO cidade VALUES (null, "Caruaru", 17);
INSERT INTO cidade VALUES (null, "Petrolina", 17);

-- Piauí (ID fictício: 18)
INSERT INTO cidade VALUES (null, "Teresina", 18);
INSERT INTO cidade VALUES (null, "Parnaíba", 18);
INSERT INTO cidade VALUES (null, "Picos", 18);
INSERT INTO cidade VALUES (null, "Floriano", 18);
INSERT INTO cidade VALUES (null, "Oeiras", 18);

-- Rio de Janeiro (ID fictício: 19)
INSERT INTO cidade VALUES (null, "Rio de Janeiro", 19);
INSERT INTO cidade VALUES (null, "Niterói", 19);
INSERT INTO cidade VALUES (null, "Duque de Caxias", 19);
INSERT INTO cidade VALUES (null, "São Gonçalo", 19);
INSERT INTO cidade VALUES (null, "Nova Iguaçu", 19);

-- Rio Grande do Norte (ID fictício: 20)
INSERT INTO cidade VALUES (null, "Natal", 20);
INSERT INTO cidade VALUES (null, "Mossoró", 20);
INSERT INTO cidade VALUES (null, "Parnamirim", 20);
INSERT INTO cidade VALUES (null, "Santa Cruz", 20);
INSERT INTO cidade VALUES (null, "Caicó", 20);

-- Rio Grande do Sul (ID fictício: 21)
INSERT INTO cidade VALUES (null, "Porto Alegre", 21);
INSERT INTO cidade VALUES (null, "Caxias do Sul", 21);
INSERT INTO cidade VALUES (null, "Pelotas", 21);
INSERT INTO cidade VALUES (null, "Santa Maria", 21);
INSERT INTO cidade VALUES (null, "Novo Hamburgo", 21);

-- Rondônia (ID fictício: 22)
INSERT INTO cidade VALUES (null, "Porto Velho", 22);
INSERT INTO cidade VALUES (null, "Ji-Paraná", 22);
INSERT INTO cidade VALUES (null, "Vilhena", 22);
INSERT INTO cidade VALUES (null, "Ariquemes", 22);
INSERT INTO cidade VALUES (null, "Rolim de Moura", 22);

-- Roraima (ID fictício: 23)
INSERT INTO cidade VALUES (null, "Boa Vista", 23);
INSERT INTO cidade VALUES (null, "Rorainópolis", 23);
INSERT INTO cidade VALUES (null, "Caracaraí", 23);
INSERT INTO cidade VALUES (null, "Mucajaí", 23);
INSERT INTO cidade VALUES (null, "São João da Baliza", 23);

-- Santa Catarina (ID fictício: 24)
INSERT INTO cidade VALUES (null, "Florianópolis", 24);
INSERT INTO cidade VALUES (null, "Joinville", 24);
INSERT INTO cidade VALUES (null, "Blumenau", 24);
INSERT INTO cidade VALUES (null, "Criciúma", 24);
INSERT INTO cidade VALUES (null, "Chapecó", 24);

-- São Paulo (ID fictício: 25)
INSERT INTO cidade VALUES (null, "São Paulo", 25);
INSERT INTO cidade VALUES (null, "Campinas", 25);
INSERT INTO cidade VALUES (null, "São Bernardo do Campo", 25);
INSERT INTO cidade VALUES (null, "Santo André", 25);
INSERT INTO cidade VALUES (null, "São José dos Campos", 25);

-- Sergipe (ID fictício: 26)
INSERT INTO cidade VALUES (null, "Aracaju", 26);
INSERT INTO cidade VALUES (null, "Socorro", 26);
INSERT INTO cidade VALUES (null, "Itabaiana", 26);
INSERT INTO cidade VALUES (null, "Lagarto", 26);
INSERT INTO cidade VALUES (null, "Estância", 26);

-- Tocantins (ID fictício: 27)
INSERT INTO cidade VALUES (null, "Palmas", 27);
INSERT INTO cidade VALUES (null, "Araguaína", 27);
INSERT INTO cidade VALUES (null, "Gurupi", 27);
INSERT INTO cidade VALUES (null, "Porto Nacional", 27);
INSERT INTO cidade VALUES (null, "Paraíso do Tocantins", 27);

INSERT INTO sexo VALUES (null,"Masc"),
						(null,"Fem"),
                        (null,"Outros");

INSERT INTO nacionalidade VALUES (null,"Brasileira"),
								 (null,"Estrangeira");

INSERT INTO raca VALUES (null,"Preta"),
						(null,"Branco"),
                        (null,"Parda"),
                        (null,"Amarela"),
                        (null,"Indígena");

INSERT INTO escolaridade VALUES (null,"Educação Infantil"),
								(null,"Fundamental"),
                                (null,"Médio"),
                                (null,"Superior (Graduação)"),
                                (null,"Pós-Graduação"),
                                (null,"Mestrado"),
                                (null,"Doutorado"),
                                (null,"Escola");
                                

						
select cliente.nome, cidade.Cidade from cliente join cidade on cliente.id_cidade = cidade.id_cidade;
select cliente.nome, estado.Estado from cliente join cidade on cliente.id_cidade = cidade.id_cidade join estado on cidade.id_estado = estado.id_estado;
select cliente.nome, cliente.cpf, raca.Raca from cliente join raca on cliente.id_raca = raca.id_raca; 
select cliente.nome, nacionalidade.Nacionalidade from cliente join nacionalidade on cliente.id_nacionalidade = nacionalidade.id_nacionalidade;
select cliente.nome, escolaridade.Escolaridade from cliente join escolaridade on cliente.id_escolaridade = escolaridade.id_escolaridade;
select cliente.nome, cidade.Cidade, estado.Estado from cliente join cidade on cliente.id_cidade = cidade.id_cidade join estado on cidade.id_estado = estado.id_estado;
select cliente.nome, cliente.cpf, cliente.rg, cidade.Cidade, estado.Estado, sexo.Sexo, nacionalidade.Nacionalidade, raca.Raca, escolaridade.Escolaridade from cliente join cidade on 
cliente.id_cidade = cidade.id_cidade join estado on cidade.id_estado = estado.id_estado join sexo on cliente.id_sexo = sexo.id_sexo join nacionalidade on cliente.id_nacionalidade
 = nacionalidade.id_nacionalidade join raca on cliente.id_raca = raca.id_raca join escolaridade on cliente.id_escolaridade = escolaridade.id_escolaridade;




