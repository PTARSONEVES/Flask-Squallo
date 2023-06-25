from sqlalchemy import create_engine, text


engine =create_engine("mysql://ptarsoneves:Strolandia1@database-1.cizel514jz3i.us-east-2.rds.amazonaws.com/py_squallo?charset=utf8m4")

def cadastra_usuario(nome,email,senha):
   with engine.connect() as conn:
      query = text(
         f"INSERT INTO users (name,email,password) VALUES (:nome,:email,:senha)"
      )
      conn.execute(
         query,{
            'name': nome,
            'email': email,
            'senha': senha
         }
      )
      print(nome)
      conn.commit()

def carrega_vagas_db():
  with engine.connect() as conn:
      resultado = conn.execute(text("SELECT * FROM vagas"))
      vagas = []
      for vaga in resultado.all():
          vagas.append(vaga._asdict())
      return vagas

def carrega_vaga_db(id):
  with engine.connect() as conn:
      resultado = conn.execute(text(f"SELECT * FROM vagas WHERE id = :val"),{"val": id})
      registro = resultado.mappings().all()
      if len(registro) == 0:
         return None
      else:
         return dict(registro[0])
      
def adiciona_inscricao(id_vaga, dados):
   with engine.connect() as conn:
      query = text(
         f"INSERT INTO inscricoes(vaga_id,nome,email,linkedin,experiencia) VALUES (:vaga_id,:nome,:email,:linkedin,:experiencia)"
      )
      conn.execute(
         query,{
            'vaga_id': id_vaga,
            'nome': dados['nome'],
            'email': dados['email'],
            'linkedin': dados['linkedin'],
            'experiencia': dados['experiencia']
         }
      )
      conn.commit()