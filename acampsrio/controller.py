from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import RequestHandler
from google.appengine.ext.webapp.util import run_wsgi_app
from model import Participante
import datetime

class HomeHandler(RequestHandler):
    def get(self):
        self.response.out.write(template.render('pages/index.html', {}))
        
class AcampamentoHandler(RequestHandler):
    def get(self):
        self.response.out.write(template.render('pages/acampamento.html', {}))

class FotoVideoHandler(RequestHandler):
    def get(self):
        self.response.out.write(template.render('pages/fotoVideo.html', {}))

class TestemunhoHandler(RequestHandler):
    def get(self):
        self.response.out.write(template.render('pages/testemunho.html', {}))

class ContatoHandler(RequestHandler):
    def get(self):
        self.response.out.write(template.render('pages/contato.html', {}))
        
class AdoteUmJovemHandler(RequestHandler):
    def get(self):
        self.response.out.write(template.render('pages/adoteUmJovem.html', {}))

class InscricaoParticipanteHandler(RequestHandler):
    
    def get(self):
        self.response.out.write(template.render('pages/inscricaoParticipante.html', {}))

    def post(self):
        
        
        participante = Participante()
        participante.nome = self.request.get('nome')
        participante.dataNascimento = self.request.get('dataNascimento')
        participante.sexo = self.request.get('sexo')
        participante.cpf = self.request.get('cpf')
        participante.identidade = self.request.get('identidade')
        
        participante.logradouro = self.request.get('logradouro')
        participante.complemento = self.request.get('complemento')
        participante.cidade = self.request.get('cidade')
        participante.uf = self.request.get('uf')
        participante.bairro = self.request.get('bairro')
        
        participante.telCelular1 = self.request.get('telCelular1')
        participante.telCelular2 = self.request.get('telCelular2')
        participante.telResidencial = self.request.get('telResidencial')
        participante.email = self.request.get('email')
        
        participante.alergias = self.request.get('alergias')
        participante.medicamentos = self.request.get('medicamentos')
        
        participante.nomeContato = self.request.get('nomeContato')
        participante.telCelular1Contato = self.request.get('telCelular1Contato')
        participante.telCelular2Contato = self.request.get('telCelular2Contato')
        participante.telResidenciaContato = self.request.get('telResidenciaContato')
        participante.telComercialContato = self.request.get('telComercialContato')
        
        participante.dataInscricao = datetime.datetime.now()
        
        participante.put() 
        
        return self.redirect('/inscricaoParticipante')


application = webapp.WSGIApplication(
                                     [('/', HomeHandler),
                                      ('/inscricaoParticipante', InscricaoParticipanteHandler)
                                     ],
                                     debug=True)
def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
