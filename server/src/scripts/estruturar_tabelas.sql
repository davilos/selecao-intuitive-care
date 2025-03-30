CREATE TABLE IF NOT EXISTS operadoras (
    Registro_ANS VARCHAR(20) PRIMARY KEY,
    CNPJ VARCHAR(14) NOT NULL UNIQUE,
    Razao_Social VARCHAR(200) NOT NULL,
    Nome_Fantasia VARCHAR(200),
    Modalidade VARCHAR(100) NOT NULL,
    Logradouro VARCHAR(200),
    Numero VARCHAR(20),
    Complemento VARCHAR(50),
    Bairro VARCHAR(100),
    Cidade VARCHAR(100),
    UF CHAR(2),
    CEP CHAR(8),
    DDD CHAR(2),
    Telefone VARCHAR(20),
    Fax VARCHAR(20),
    Endereco_eletronico VARCHAR(100),
    Representante VARCHAR(100),
    Cargo_Representante VARCHAR(100),
    Regiao_de_Comercializacao VARCHAR(10),
    Data_Registro_ANS DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS demonstracao_contabeis (
  ID INT AUTO_INCREMENT PRIMARY KEY,
  DATA DATE NOT NULL,
  REG_ANS VARCHAR(6) NOT NULL,
  CD_CONTA_CONTABIL VARCHAR(9) NOT NULL,
  DESCRICAO VARCHAR(200) NOT NULL,
  VL_SALDO_INICIAL DECIMAL(18, 2),
  VL_SALDO_FINAL DECIMAL(18, 2)
)
