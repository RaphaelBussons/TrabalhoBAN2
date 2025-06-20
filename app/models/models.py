from .database import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from flask_login import UserMixin


class Bibliotecario(UserMixin,db.Model):

    __tablename__ = 'bibliotecario'

    id_bibliotecario: Mapped[int]=  mapped_column(primary_key=True)
    cpf: Mapped[str]= mapped_column (nullable=False, unique=True)
    nome:Mapped[str] = mapped_column (nullable=False)
    endereco: Mapped[str] = mapped_column (nullable=False)
    telefone: Mapped[str]  = mapped_column ()
    senha: Mapped[str] = mapped_column(nullable=False)

  
    def get_id(self): 
        return self.id_bibliotecario
    
    def __repr__(self):
        return f"{self.id_bibliotecario, self.cpf, self.nome, self.endereco, self.telefone}"


class Usuario(UserMixin,db.Model): 
    id_usuario:Mapped[int] = mapped_column(primary_key=True)
    cpf: Mapped[str] = mapped_column(nullable=False, unique=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    num_emprestimos: Mapped[int] = mapped_column(default=0,nullable=False)
    endereco: Mapped[str] = mapped_column(nullable=False)
    telefone: Mapped[str] = mapped_column()
    id_categoria:Mapped[int] = mapped_column(nullable=False, default=1)
    senha: Mapped[int] =  mapped_column(nullable= False)

    def get_id(self): 
        return self.id_usuario


# class Livro(db.Model):
#     id_livro:Mapped[int] = mapped_column(primary_key=True)
#     isbn: Mapped[str] = mapped_column(nullable=False, unique=True)
#     id_colecao: Mapped[int] = mapped_column(nullable=False)
#     id_editora: Mapped[int] = mapped_column(nullable=False)

#     def __repr__(self):
#         return f"{self.id_livro, self.isbn, self.id_colecao, self.id_editora}"



# class Exemplar(db.Model): 
#     id_exemplar:Mapped[int] = mapped_column(primary_key=True)
#     eh_reserva: Mapped[bool] = mapped_column(nullable=False, unique=True)
#     esta_emprestado: Mapped[bool] = mapped_column(nullable=False)
#     id_livro: Mapped[int] = relationship("Livro", primaryjoin="and_(Exemplar.id_livro == Livro.id_livro)")
    

#     def __repr__(self):
#         return f"{self.id_exemplar, self.eh_reserva, self.esta_emprestado, self.id_livro}"

# class Assistente(db.Model):

#   __tablename__ = 'assistente'

#   id_assistente: Mapped[int]=  mapped_column(primary_key=True)
#   id_bibliotecario: Mapped[int]= mapped_column(ForeignKey("bibliotecario.id"))    
#   nome:Mapped[str] = mapped_column (nullable=False)
#   endereco: Mapped[str] = mapped_column (nullable=False)
#   telefone: Mapped[str] = mapped_column()
#   senha: Mapped[str] = mapped_column(nullable=False)



