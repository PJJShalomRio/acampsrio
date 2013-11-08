"""
@author: matheus cardoso
 
Copyright (C) 2013 MVM Tecnologia
"""

from google.appengine.ext import db
class Participante(db.Model):
    
    nome = db.StringProperty()
    dataNascimento = db.StringProperty()
    sexo = db.StringProperty(   )
    identidade = db.StringProperty()
    
    logradouro = db.StringProperty()
    complemento = db.StringProperty()
    cidade = db.StringProperty()
    uf = db.StringProperty()
    bairro = db.StringProperty()
    
    telCelular1 = db.StringProperty()
    telCelular2 = db.StringProperty()
    telResidencial = db.StringProperty()
    email = db.StringProperty()
    
    alergias = db.StringProperty()
    medicamentos = db.StringProperty()
    
    nomeContato = db.StringProperty()
    telCelular1Contato = db.StringProperty()
    telCelular2Contato = db.StringProperty()
    telResidenciaContato = db.StringProperty()
    telComercialContato = db.StringProperty()
    
    ficouSabendo = db.StringListProperty()
    
    termoCompromisso = db.StringProperty()
    
    foto = db.BlobProperty()
    
    dataInscricao = db.DateTimeProperty(auto_now=True, auto_now_add=True)
    
class Servico(db.Model):
    
    nome = db.StringProperty()
    dataNascimento = db.StringProperty()
    sexo = db.StringProperty()
    
    logradouro = db.StringProperty()
    complemento = db.StringProperty()
    cidade = db.StringProperty()
    uf = db.StringProperty()
    bairro = db.StringProperty()
    
    telCelular1 = db.StringProperty()
    telCelular2 = db.StringProperty()
    telResidencial = db.StringProperty()
    email = db.StringProperty()
    
    alergias = db.StringProperty()
    medicamentos = db.StringProperty()
    
    nomeContato = db.StringProperty()
    telCelular1Contato = db.StringProperty()
    telCelular2Contato = db.StringProperty()
    telResidenciaContato = db.StringProperty()
    telComercialContato = db.StringProperty()
    
    termoCompromisso = db.StringProperty()
    
    dataInscricao = db.DateTimeProperty(auto_now=True, auto_now_add=True)
    
class Contato(db.Model):
    
    nome = db.StringProperty()
    telCelular1 = db.StringProperty()
    email = db.StringProperty()
    comentario = db.StringProperty()
    
    dataContato = db.DateTimeProperty(auto_now=True, auto_now_add=True)
    