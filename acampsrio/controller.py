from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp import RequestHandler
from google.appengine.ext.webapp.util import run_wsgi_app
from model import Participante, Servico, Contato

from google.appengine.api import users

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
    
    def post(self):
    
        contato = Contato()
        contato.nome = self.request.get('nome')
        contato.telCelular1 = self.request.get('telCelular1')
        contato.email = self.request.get('email')
        contato.comentario = self.request.get('comentario')
        
        contato.put() 
        
        return self.redirect('/#contato')
        
class AdoteUmJovemHandler(RequestHandler):
    def get(self):
        self.response.out.write(template.render('pages/adoteUmJovem.html', {}))

class InscricaoServicoHandler(RequestHandler):
    def get(self):
        self.response.out.write(template.render('pages/inscricaoServico.html', {}))
    
    def post(self):
    
        servico = Servico()
        servico.nome = self.request.get('nome')
        servico.dataNascimento = self.request.get('dataNascimento')
        servico.sexo = self.request.get('sexo')
        servico.cpf = self.request.get('cpf')
        servico.identidade = self.request.get('identidade')
        
        servico.logradouro = self.request.get('logradouro')
        servico.complemento = self.request.get('complemento')
        servico.cidade = self.request.get('cidade')
        servico.uf = self.request.get('uf')
        servico.bairro = self.request.get('bairro')
        
        servico.telCelular1 = self.request.get('telCelular1')
        servico.telCelular2 = self.request.get('telCelular2')
        servico.telResidencial = self.request.get('telResidencial')
        servico.email = self.request.get('email')
        
        servico.alergias = self.request.get('alergias')
        servico.medicamentos = self.request.get('medicamentos')
        
        servico.nomeContato = self.request.get('nomeContato')
        servico.telCelular1Contato = self.request.get('telCelular1Contato')
        servico.telCelular2Contato = self.request.get('telCelular2Contato')
        servico.telResidenciaContato = self.request.get('telResidenciaContato')
        servico.telComercialContato = self.request.get('telComercialContato')
        
        servico.put() 
        
        return self.redirect('/inscricaoServico')

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
        
        participante.put() 
        
        return self.redirect('/inscricaoParticipante')

class LoginHandler(RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            self.response.out.write(template.render('pages/admin.html', {'usuarioLogado':user.nickname()}))
        else:
            self.redirect(users.create_login_url(self.request.uri))

application = webapp.WSGIApplication(
                                     [('/', HomeHandler),
                                      ('/inscricaoParticipante', InscricaoParticipanteHandler),
                                      ('/inscricaoServico', InscricaoServicoHandler),
                                      ('/login', LoginHandler),
                                      ('/contato', ContatoHandler)
                                     ],
                                     debug=True)
def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
