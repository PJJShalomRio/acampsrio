"""
@author: matheus cardoso
 
Copyright (C) 2013 MVM Tecnologia
"""

from google.appengine.api import mail
from google.appengine.ext import db
class Participante(db.Model):
    
    nome = db.StringProperty()
    dataNascimento = db.StringProperty()
    sexo = db.StringProperty()
    barraca = db.StringProperty()
    identidade = db.StringProperty()
    
    logradouro = db.StringProperty()
    complemento = db.StringProperty()
    cidade = db.StringProperty()
    uf = db.StringProperty()
    bairro = db.StringProperty()
    zona = db.StringProperty()
    
    telCelular1 = db.StringProperty()
    telCelular2 = db.StringProperty()
    telResidencial = db.StringProperty()
    email = db.StringProperty()
    
    problemaSaude = db.StringProperty()
    restricaoAtividadeFisica = db.StringProperty()
    temAlgumaAlergia = db.StringProperty()
    tomaAlgumMedicamento = db.StringProperty()
    
    nomeContato = db.StringProperty()
    telCelular1Contato = db.StringProperty()
    telCelular2Contato = db.StringProperty()
    telResidencialContato = db.StringProperty()
    telComercialContato = db.StringProperty()
    termoCompromisso = db.StringProperty()
    ficouSabendo = db.StringListProperty()
    
    familia = db.StringProperty()
    
    dataInscricao = db.DateTimeProperty(auto_now=True, auto_now_add=True)

class Indicacao(db.Model):
    nome = db.StringProperty()
    nomeIndicacao = db.StringProperty()
    telCelularIndicacao = db.StringProperty()
    telResidencialIndicacao = db.StringProperty()
    emailIndicacao = db.StringProperty()
    
class Servico(db.Model):
    
    nome = db.StringProperty()
    dataNascimento = db.StringProperty()
    sexo = db.StringProperty()
    equipeServico = db.StringProperty()
    
    logradouro = db.StringProperty()
    complemento = db.StringProperty()
    cidade = db.StringProperty()
    uf = db.StringProperty()
    bairro = db.StringProperty()
    
    telCelular1 = db.StringProperty()
    telCelular2 = db.StringProperty()
    telResidencial = db.StringProperty()
    email = db.StringProperty()
       
    problemaSaude = db.StringProperty()
    restricaoAtividadeFisica = db.StringProperty()
    temAlgumaAlergia = db.StringProperty()
    tomaAlgumMedicamento = db.StringProperty()
    
    nomeContato = db.StringProperty()
    telCelular1Contato = db.StringProperty()
    telCelular2Contato = db.StringProperty()
    telResidencialContato = db.StringProperty()
    telComercialContato = db.StringProperty()
    linkRedeSocial = db.StringProperty()
    
    setorParticipa = db.StringProperty()
    nomeGrupoOracao = db.StringProperty()
    nomePastor = db.StringProperty()
    tipoMembro = db.StringProperty()
    
    dataInscricao = db.DateTimeProperty(auto_now=True, auto_now_add=True)
  
class Contato(db.Model):
    
    nome = db.StringProperty()
    telCelular1 = db.StringProperty()
    email = db.StringProperty()
    comentario = db.StringProperty(multiline=True)
    
    dataContato = db.DateTimeProperty(auto_now=True, auto_now_add=True)
     
    def enviarEmail(self):
            mail.send_mail(sender="tipjjriodejaneiro@gmail.com",
            to="tipjjriodejaneiro@gmail.com",
            subject="[ACAMPSRIO] - Contato",
            body="Nome: " + self.nome + "\nCelular: " + self.telCelular1 + "\nEmail: " + self.email + "\nMensagem: " + self.comentario)
            

    
