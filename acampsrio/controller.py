from datetime import date
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import RequestHandler, template
from google.appengine.ext.webapp.util import run_wsgi_app
from model import Participante, Servico, Contato, Familia, Onibus
import csv
from google.appengine._internal.django.utils.encoding import smart_str


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
    
        try:
            contato = Contato()
            contato.nome = self.request.get('nome')
            contato.telCelular1 = self.request.get('telCelular1')
            contato.email = self.request.get('email')
            contato.comentario = self.request.get('comentario')
            
            contato.put() 
            contato.enviarEmail()
        except Exception:
            self.response.out.write(template.render('pages/errointerno.html', {}))
            return
        
        return self.redirect('/#contato')
        
class AdoteUmJovemHandler(RequestHandler):
    def get(self):
        self.response.out.write(template.render('pages/adoteUmJovem.html', {}))

class TermoCompromissoHandler(RequestHandler):
    def get(self):
        self.response.out.write(template.render('pages/termocompromisso.html', {}))

class RealizarPagamentoHandler(RequestHandler):
    def get(self):
        self.response.out.write(template.render('pages/realizarPagamento.html', {}))

class RealizarPagamentoServicoHandler(RequestHandler):
    def get(self):
        self.response.out.write(template.render('pages/realizarPagamentoServico.html', {}))

class InscricaoServicoHandler(RequestHandler):
    def get(self):
        self.response.out.write(template.render('pages/inscricaoServico.html', {}))
    
    def post(self):
    
        try:
            servico = Servico()
            servico.nome = self.request.get('nome').strip().upper()
            servico.dataNascimento = self.request.get('dataNascimento')
            servico.sexo = self.request.get('sexo')
            servico.identidade = self.request.get('identidade')
            
            servico.logradouro = self.request.get('logradouro')
            servico.complemento = self.request.get('complemento')
            servico.cidade = self.request.get('cidade').strip().upper()
            servico.uf = self.request.get('uf')
            servico.bairro = self.request.get('bairro').strip().upper()
            
            servico.telCelular1 = self.request.get('telCelular1')
            servico.telCelular2 = self.request.get('telCelular2')
            servico.telResidencial = self.request.get('telResidencial')
            servico.email = self.request.get('email')
            
            servico.alergias = self.request.get('alergias')
            servico.medicamentos = self.request.get('medicamentos')
            
            servico.nomeContato = self.request.get('nomeContato')
            servico.telCelular1Contato = self.request.get('telCelular1Contato')
            servico.telCelular2Contato = self.request.get('telCelular2Contato')
            servico.telResidencialContato = self.request.get('telResidencialContato')
            servico.telComercialContato = self.request.get('telComercialContato')
            
            servico.put() 
        except Exception, e:
            self.response.out.write(template.render('pages/errointerno.html', {}))
            return e
        
        return self.redirect('/realizarPagamentoServico')

class InscricaoParticipanteHandler(RequestHandler):
    def get(self):
        self.response.out.write(template.render('pages/inscricaoParticipante.html', {}))
    def post(self):
        
        try:
            participante = Participante()
            participante.nome = self.request.get('nome').strip().upper()
            participante.dataNascimento = self.request.get('dataNascimento')
            participante.sexo = self.request.get('sexo')
            participante.identidade = self.request.get('identidade')
            
            participante.logradouro = self.request.get('logradouro')
            participante.complemento = self.request.get('complemento')
            participante.cidade = self.request.get('cidade').strip().upper()
            participante.uf = self.request.get('uf')
            participante.bairro = self.request.get('bairro').strip().upper()
            
            participante.telCelular1 = self.request.get('telCelular1')
            participante.telCelular2 = self.request.get('telCelular2')
            participante.telResidencial = self.request.get('telResidencial')
            participante.email = self.request.get('email')
            
            participante.alergias = self.request.get('alergias')
            participante.medicamentos = self.request.get('medicamentos')
            
            participante.nomeContato = self.request.get('nomeContato')
            participante.telCelular1Contato = self.request.get('telCelular1Contato')
            participante.telCelular2Contato = self.request.get('telCelular2Contato')
            participante.telResidencialContato = self.request.get('telResidencialContato')
            participante.telComercialContato = self.request.get('telComercialContato')
            participante.termoCompromisso = self.request.get('termoCompromisso')
            participante.ficouSabendo = self.request.get_all('ficouSabendo')
            
            participante.put()
        except Exception, e:
            self.response.out.write(template.render('pages/errointerno.html', {}))
            return e
        
        return self.redirect('/realizarPagamento')

class LoginHandler(RequestHandler):
    def get(self):
        
        user = users.get_current_user()
        if user and users.is_current_user_admin():
            self.response.out.write(template.render('pages/admin.html', {'usuarioLogado':user.nickname()}))
        else:
            self.redirect(users.create_login_url(self.request.uri))
            
class LogoutHandler(RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            return self.redirect(users.create_logout_url('/'))
        else:
            self.response.out.write(template.render('pages/index.html', {}))
            
class RelacaoParticipantesInscritosHandler(RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user and users.is_current_user_admin():
            results = Participante.all().order('nome')
            
            self.response.out.write(template.render('pages/reports/relacaoParticipantesInscritos.html',
                                                    {'listaItens':results, 'total':results.count()}))
        
class RelacaoServicosInscritosHandler(RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user and users.is_current_user_admin():
            results = Servico.all().order('nome')
            
            self.response.out.write(template.render('pages/reports/relacaoServicosInscritos.html',
                                                    {'listaItens':results, 'total':results.count()}))
        else:
            self.response.out.write(template.render('pages/index.html', {}))
            
class RelacaoCrachasParticipantesHandler(RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user and users.is_current_user_admin():
            results = Participante.all()
            
            self.response.out.write(template.render('pages/reports/relacaoCrachasParticipantes.html',
                                                    {'listaItens':results}))
        else:
            self.response.out.write(template.render('pages/index.html', {}))
            
class RelacaoEstatisticaParticipantesInscritosHandler(RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user and users.is_current_user_admin():
            
            totalParticipantes = Participante.all().count()
            totalFeminino = Participante.all().filter('sexo = ', 'F').count()
            totalMasculino = totalParticipantes - totalFeminino
            
            participantesPorBairro = dict()
            for participante in Participante.all().filter('cidade = ', 'RIO DE JANEIRO').order('bairro'):
                qtde = participantesPorBairro.get(participante.bairro)
                if qtde:
                    participantesPorBairro[participante.bairro] = qtde + 1
                else:
                    participantesPorBairro[participante.bairro] = 1
            
            participantesPorOutrasCidades = dict()
            for participante in Participante.all().filter('cidade != ', 'RIO DE JANEIRO'):
                qtde = participantesPorOutrasCidades.get(participante.cidade + '/' + participante.bairro)
                if qtde:
                    participantesPorOutrasCidades[participante.cidade + '/' + participante.bairro] = qtde + 1
                else:
                    participantesPorOutrasCidades[participante.cidade + '/' + participante.bairro] = 1
                    
            participantesPorIdade = dict()
            for participante in Participante.all():
                today = date.today()
                idade = today.year - int(participante.dataNascimento.split('/')[2])
                qtde = participantesPorIdade.get(idade)
                if qtde:
                    participantesPorIdade[idade] = qtde + 1
                else:
                    participantesPorIdade[idade] = 1
            
            self.response.out.write(template.render('pages/reports/relacaoEstatisticaParticipantesInscritos.html',
                                                    {'totalParticipantes':totalParticipantes,
                                                     'totalFeminino':totalFeminino,
                                                     'totalMasculino':totalMasculino,
                                                     'participantesPorBairro':participantesPorBairro,
                                                     'participantesPorOutrasCidades':participantesPorOutrasCidades,
                                                     'participantesPorIdade':participantesPorIdade
                                                     }))
        else:
            self.response.out.write(template.render('pages/index.html', {}))
            
class RelacaoParticipantesPorFamiliaHandler(RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user and users.is_current_user_admin():
            participantes = Participante.all()
            
            familias = list()
            for x in ['Vermelha', 'Branca', 'Preta', 'Verde', 'Azul', 'Coral', 'Amarela']:
                familia = Familia()
                familia.cor = x
                familia.filhos = participantes
                familia.total = participantes.count()
                familias.append(familia)
            
            self.response.out.write(template.render('pages/reports/relacaoParticipantesPorFamilia.html',
                                                    {'familias':familias}))
        else:
            self.response.out.write(template.render('pages/index.html', {}))
            
class RelacaoPessoasPorOnibusHandler(RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user and users.is_current_user_admin():
            listaOnibus = list()
            listaPassageiro = list()
            countPassageiro = 0
            countOnibus = 1
            for participante in Participante.all().order('nome'):
                if countPassageiro < 46:
                    listaPassageiro.append(participante)
                    countPassageiro += 1
                else:
                    onibus = Onibus()
                    onibus.numero = countOnibus
                    onibus.pessoas = listaPassageiro
                    onibus.total = listaPassageiro.__len__()
                    listaOnibus.append(onibus)
                    
                    listaPassageiro = list() 
                    listaPassageiro.append(participante)
                    countPassageiro = 1
                    countOnibus += 1
                    
            onibus = Onibus()
            onibus.numero = countOnibus
            onibus.pessoas = listaPassageiro
            onibus.total = listaPassageiro.__len__()
            listaOnibus.append(onibus)
            
            self.response.out.write(template.render('pages/reports/relacaoPessoasPorOnibus.html',
                                                    {'listaOnibus':listaOnibus}))
        else:
            self.response.out.write(template.render('pages/index.html', {}))

class ExportarParticipantesHandler(RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user and users.is_current_user_admin():
            self.response.headers['Content-Type'] = 'application/csv'
            self.response.headers['Content-Disposition'] = 'attachment; filename=participantes.csv'
            writer = csv.writer(self.response.out, delimiter=';', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(["Nome", "Data de Nascimento", "Sexo", "Identidade",
                             "Logradouro", "Complemento", "Cidade", "UF", "Bairro",
                             "Tel Celular1", "Tel Celular2", "Tel Residencial", "Email",
                             "Alergias", "Medicamentos",
                             "Nome do Contato",
                             "Tel Celular1 Contato", "Tel Celular2 Contato", "Tel Residencial Contato", "Tel Comercial Contato"])
            
            for participante in Participante.all().order('nome'):
                writer.writerow([smart_str(participante.nome, encoding='ISO-8859-1'),
                                 smart_str(participante.dataNascimento, encoding='ISO-8859-1'),
                                 smart_str(participante.sexo, encoding='ISO-8859-1'),
                                 smart_str(participante.identidade, encoding='ISO-8859-1'),
                                 smart_str(participante.logradouro, encoding='ISO-8859-1'),
                                 smart_str(participante.complemento, encoding='ISO-8859-1'),
                                 smart_str(participante.cidade, encoding='ISO-8859-1'),
                                 smart_str(participante.uf, encoding='ISO-8859-1'),
                                 smart_str(participante.bairro, encoding='ISO-8859-1'),
                                 smart_str(participante.telCelular1, encoding='ISO-8859-1'),
                                 smart_str(participante.telCelular2, encoding='ISO-8859-1'),
                                 smart_str(participante.telResidencial, encoding='ISO-8859-1'),
                                 smart_str(participante.email, encoding='ISO-8859-1'),
                                 smart_str(participante.alergias, encoding='ISO-8859-1'),
                                 smart_str(participante.medicamentos, encoding='ISO-8859-1'),
                                 smart_str(participante.nomeContato, encoding='ISO-8859-1'),
                                 smart_str(participante.telCelular1Contato, encoding='ISO-8859-1'),
                                 smart_str(participante.telCelular2Contato, encoding='ISO-8859-1'),
                                 smart_str(participante.telResidencialContato, encoding='ISO-8859-1'),
                                 smart_str(participante.telComercialContato, encoding='ISO-8859-1')])
        
class ExportarServicoHandler(RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user and users.is_current_user_admin():
            self.response.headers['Content-Type'] = 'application/csv'
            self.response.headers['Content-Disposition'] = 'attachment; filename=servos.csv'
            writer = csv.writer(self.response.out, delimiter=';', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(["Nome", "Data de Nascimento", "Sexo", "Identidade",
                             "Logradouro", "Complemento", "Cidade", "UF", "Bairro",
                             "Tel Celular1", "Tel Celular2", "Tel Residencial", "Email",
                             "Alergias", "Medicamentos",
                             "Nome do Contato",
                             "Tel Celular1 Contato", "Tel Celular2 Contato", "Tel Residencial Contato", "Tel Comercial Contato"])
            
            for servico in Servico.all().order('nome'):
                writer.writerow([smart_str(servico.nome, encoding='ISO-8859-1'),
                                 smart_str(servico.dataNascimento, encoding='ISO-8859-1'),
                                 smart_str(servico.sexo, encoding='ISO-8859-1'),
                                 smart_str(servico.identidade, encoding='ISO-8859-1'),
                                 smart_str(servico.logradouro, encoding='ISO-8859-1'),
                                 smart_str(servico.complemento, encoding='ISO-8859-1'),
                                 smart_str(servico.cidade, encoding='ISO-8859-1'),
                                 smart_str(servico.uf, encoding='ISO-8859-1'),
                                 smart_str(servico.bairro, encoding='ISO-8859-1'),
                                 smart_str(servico.telCelular1, encoding='ISO-8859-1'),
                                 smart_str(servico.telCelular2, encoding='ISO-8859-1'),
                                 smart_str(servico.telResidencial, encoding='ISO-8859-1'),
                                 smart_str(servico.email, encoding='ISO-8859-1'),
                                 smart_str(servico.alergias, encoding='ISO-8859-1'),
                                 smart_str(servico.medicamentos, encoding='ISO-8859-1'),
                                 smart_str(servico.nomeContato, encoding='ISO-8859-1'),
                                 smart_str(servico.telCelular1Contato, encoding='ISO-8859-1'),
                                 smart_str(servico.telCelular2Contato, encoding='ISO-8859-1'),
                                 smart_str(servico.telResidencialContato, encoding='ISO-8859-1'),
                                 smart_str(servico.telComercialContato, encoding='ISO-8859-1')])

application = webapp.WSGIApplication(
                                     [('/', HomeHandler),
                                      ('/inscricaoParticipante', InscricaoParticipanteHandler),
                                      ('/inscricaoServico', InscricaoServicoHandler),
                                      ('/inscricaoservico', InscricaoServicoHandler),
                                      ('/termoCompromisso', TermoCompromissoHandler),
                                      ('/login', LoginHandler),
                                      ('/logout', LogoutHandler),
                                      ('/contato', ContatoHandler),
                                      ('/exportarParticipante', ExportarParticipantesHandler),
                                      ('/exportarServico', ExportarServicoHandler),
                                      ('/realizarPagamento', RealizarPagamentoHandler),
                                      ('/realizarPagamentoServico', RealizarPagamentoServicoHandler),
                                      ('/relacaoParticipantesInscritos', RelacaoParticipantesInscritosHandler),
                                      ('/relacaoServicosInscritos', RelacaoServicosInscritosHandler),
                                      ('/relacaoCrachasParticipantes', RelacaoCrachasParticipantesHandler),
                                      ('/relacaoEstatisticaParticipantesInscritos', RelacaoEstatisticaParticipantesInscritosHandler),
                                      ('/relacaoPessoasPorOnibus', RelacaoPessoasPorOnibusHandler),
                                      ('/relacaoParticipantesPorFamilia', RelacaoParticipantesPorFamiliaHandler)
                                     ],
                                     debug=True)
def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
