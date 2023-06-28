from sqlalchemy import create_engine, text
from flask import jsonify
from app import login_manager
from flask_login import UserMixin
from dotenv import load_dotenv
import os

engine =create_engine("mysql://ptarsoneves:Strolandia1@database-1.cizel514jz3i.us-east-2.rds.amazonaws.com/py_squallo")

def obtem_usuario(usuario):
   with engine.connect() as conn:
      query = text(
         f"SELECT * FROM users WHERE usuario = :usuario" 
      )
      resultado = conn.execute(query,{'usuario': usuario})
      registro = resultado.mappings().all()
      num_linhas = resultado.rowcount
      if len(registro) == 0:
         return None
      else:
#         user=[]
#         user=registro.index(0)
         return registro

usuario_logado = obtem_usuario('ptarsoneves')
if usuario_logado == None:
   print("não localizado")
else:
   print(usuario_logado[0].password)
