from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Boolean, Date
from sqlalchemy.orm import relationship
from db import Base # Importação sem ponto

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    nome_ong = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    cnpj = Column(String(18), unique=True, index=True, nullable=False)
    endereco = Column(String(255))
    area_especializacao = Column(String(100))
    password_hash = Column(String(128), nullable=False)
    tfa_enabled = Column(Boolean, default=False) 
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relacionamento com Prontuarios
    prontuarios = relationship("Prontuario", back_populates="owner")

# MUDAMOS O MODELO 'Report' PARA 'Prontuario'
class Prontuario(Base):
    __tablename__ = "prontuarios" # Novo nome da tabela

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="prontuarios")
    
    # --- Campos da Ficha de Observações (image_9527f3.png) ---
    nome_paciente = Column(String(200), nullable=False, index=True) # Usaremos este para ordem alfabética
    idade = Column(Integer)
    endereco_paciente = Column(String(255))
    bairro = Column(String(100))
    cidade = Column(String(100))
    profissao = Column(String(100))
    telefone = Column(String(20))
    convenio = Column(String(100))
    
    # --- Campo Principal de Acompanhamento ---
    observacoes_medicas = Column(Text) # Campo grande para o médico escrever

    # --- Campos da Ficha de Anamnese (image_94d0dd.png) ---
    data_nascimento = Column(Date)
    tipo_sanguineo = Column(String(10))
    contato_emergencia_nome = Column(String(200))
    contato_emergencia_telefone = Column(String(20))
    tem_seguro = Column(String(10))
    fumante = Column(String(10))
    tem_alergia = Column(String(10))
    alergia_descricao = Column(Text)
    alimento_restricao = Column(Text)
    tem_medicamento = Column(String(10))
    medicamento_descricao = Column(Text)
    condicao_fisica = Column(String(50))
    
    created_at = Column(DateTime, default=datetime.utcnow)