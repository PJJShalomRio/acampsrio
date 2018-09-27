import collections
import csv
from datetime import date

from google.appengine._internal.django.utils.encoding import smart_str
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import RequestHandler, template
from google.appengine.ext.webapp.util import run_wsgi_app

from model import Participante, Servico, Contato, Indicacao


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

class InformacoesImportantesHandler(RequestHandler):
    def get(self):
        self.response.out.write(template.render('pages/informacoesImportantes.html', {}))

class RealizarPagamentoHandler(RequestHandler):
    def get(self):
        self.response.out.write(template.render('pages/realizarPagamento.html', {}))

class RealizarPagamentoServicoHandler(RequestHandler):
    def get(self):
        self.response.out.write(template.render('pages/realizarPagamentoServico.html', {}))

class PreInscricaoServicoHandler(RequestHandler):
    def get(self):
        self.response.out.write(template.render('pages/preInscricaoServico.html', {}))

class InscricaoServicoHandler(RequestHandler):
    def get(self):
        self.response.out.write(template.render('pages/inscricaoServico.html', {}))
    
    def post(self):
    
        try:
            servico = Servico()
            servico.nome = self.request.get('nome').strip().upper()
            servico.dataNascimento = self.request.get('dataNascimento')
            servico.sexo = self.request.get('sexo')
            servico.equipeServico = self.request.get('equipeServico')
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
            servico.linkRedeSocial = self.request.get('linkRedeSocial')
            
            servico.problemaSaude = self.request.get('problemaSaude')
            servico.restricaoAtividadeFisica = self.request.get('restricaoAtividadeFisica')
            servico.temAlgumaAlergia = self.request.get('temAlgumaAlergia')
            servico.tomaAlgumMedicamento = self.request.get('tomaAlgumMedicamento')
            
            servico.nomeContato = self.request.get('nomeContato')
            servico.telCelular1Contato = self.request.get('telCelular1Contato')
            servico.telCelular2Contato = self.request.get('telCelular2Contato')
            servico.telResidencialContato = self.request.get('telResidencialContato')
            servico.telComercialContato = self.request.get('telComercialContato')
            
            servico.setorParticipa = self.request.get('setorParticipa')
            servico.nomeGrupoOracao = self.request.get('nomeGrupoOracao')
            servico.nomePastor = self.request.get('nomePastor')
            servico.tipoMembro = self.request.get('tipoMembro')
            
                
            servicoJaExiste = Servico.all().filter('nome = ', servico.nome).count()
            if servicoJaExiste is None or servicoJaExiste == 0: 
                servico.put()
             
        except Exception, e:
            self.response.out.write(template.render('pages/errointerno.html', {}))
            return e
        
        return self.redirect('/realizarPagamentoServico')

class InscricaoParticipanteHandler(RequestHandler):
    def get(self):
        self.response.out.write(template.render('pages/inscricaoParticipante.html', {}))
    def post(self):
        familiaDict = {
                       "SUL": "Laranja e Roxo",
                       "NORTE": "Azul e Verde",
                       "OESTE": "Preto e Branco",
                       "CENTRAL": "Laranja e Roxo",
                       "BAIXADA": "Marrom e vermelho",
                       "OUTRAS": "Marrom e vermelho"
                       }
        
        try:
            participante = Participante()
            participante.nome = self.request.get('nome').strip().upper()
            participante.dataNascimento = self.request.get('dataNascimento')
            participante.sexo = self.request.get('sexo')
            participante.barraca = self.request.get('barraca')
            participante.identidade = self.request.get('identidade')
            
            participante.logradouro = self.request.get('logradouro')
            participante.complemento = self.request.get('complemento')
            participante.cidade = self.request.get('cidade').strip().upper()
            participante.uf = self.request.get('uf')
            participante.bairro = self.request.get('bairro').strip().upper()
            participante.zona = self.request.get('zona')
            
            participante.telCelular1 = self.request.get('telCelular1')
            participante.telCelular2 = self.request.get('telCelular2')
            participante.telResidencial = self.request.get('telResidencial')
            participante.email = self.request.get('email')
            
            participante.problemaSaude = self.request.get('problemaSaude')
            participante.restricaoAtividadeFisica = self.request.get('restricaoAtividadeFisica')
            participante.temAlgumaAlergia = self.request.get('temAlgumaAlergia')
            participante.tomaAlgumMedicamento = self.request.get('tomaAlgumMedicamento')
            
            participante.nomeContato = self.request.get('nomeContato')
            participante.telCelular1Contato = self.request.get('telCelular1Contato')
            participante.telCelular2Contato = self.request.get('telCelular2Contato')
            participante.telResidencialContato = self.request.get('telResidencialContato')
            participante.telComercialContato = self.request.get('telComercialContato')
            participante.termoCompromisso = self.request.get('termoCompromisso')
            participante.ficouSabendo = self.request.get_all('ficouSabendo')

            participante.familia = familiaDict[participante.zona]
            
            participanteJaExiste = Participante.all().filter('nome = ', participante.nome).count()
            if participanteJaExiste is None or participanteJaExiste == 0: 
                participante.put()
                
                indicacao = Indicacao()
                indicacao.nome = self.request.get('nome').strip().upper()    
                indicacao.nomeIndicacao = self.request.get('nomeIndicacao').strip().upper()
                indicacao.telCelularIndicacao = self.request.get('telCelularIndicacao')
                indicacao.telResidencialIndicacao = self.request.get('telResidencialIndicacao')
                indicacao.emailIndicacao = self.request.get('emailIndicacao')
                if indicacao.nomeIndicacao != '':
                    indicacao.put()
                
            
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
            
class RelacaoEstatisticaParticipantesInscritosHandler(RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user and users.is_current_user_admin():
            
            totalParticipantes = Participante.all().count()
            totalFeminino = Participante.all().filter('sexo = ', 'F').count()
            totalMasculino = totalParticipantes - totalFeminino
            
            totalPaticipantesPagouInscricao = Participante.all().filter('pagouInscricao = ', 'S').count()
            totalPaticipantesNaoPagouInscricao = totalParticipantes - totalPaticipantesPagouInscricao
            
            participantesPorBairro = dict()
            for participante in Participante.all().filter('cidade = ', 'RIO DE JANEIRO').order('bairro'):
                qtde = participantesPorBairro.get(participante.bairro)
                if qtde:
                    participantesPorBairro[participante.bairro] = qtde + 1
                else:
                    participantesPorBairro[participante.bairro] = 1
            participantesPorBairro = collections.OrderedDict(sorted(participantesPorBairro.items()))
            
            participantesPorOutrasCidades = dict()
            for participante in Participante.all().filter('cidade != ', 'RIO DE JANEIRO'):
                qtde = participantesPorOutrasCidades.get(participante.cidade + '/' + participante.bairro)
                if qtde:
                    participantesPorOutrasCidades[participante.cidade + '/' + participante.bairro] = qtde + 1
                else:
                    participantesPorOutrasCidades[participante.cidade + '/' + participante.bairro] = 1
            participantesPorOutrasCidades = collections.OrderedDict(sorted(participantesPorOutrasCidades.items()))
                    
            participantesPorIdade = dict()
            for participante in Participante.all():
                today = date.today()
                idade = today.year - int(participante.dataNascimento.split('/')[2])
                qtde = participantesPorIdade.get(idade)
                if qtde:
                    participantesPorIdade[idade] = qtde + 1
                else:
                    participantesPorIdade[idade] = 1
            participantesPorIdade = collections.OrderedDict(sorted(participantesPorIdade.items()))
            
            self.response.out.write(template.render('pages/reports/relacaoEstatisticaParticipantesInscritos.html',
                                                    {'totalParticipantes':totalParticipantes,
                                                     'totalFeminino':totalFeminino,
                                                     'totalMasculino':totalMasculino,
                                                     'participantesPorBairro':participantesPorBairro,
                                                     'participantesPorOutrasCidades':participantesPorOutrasCidades,
                                                     'participantesPorIdade':participantesPorIdade,
                                                     'totalPaticipantesPagouInscricao':totalPaticipantesPagouInscricao,
                                                     'totalPaticipantesNaoPagouInscricao':totalPaticipantesNaoPagouInscricao
                                                     }))
        else:
            self.response.out.write(template.render('pages/index.html', {}))

class ExportarParticipantesHandler(RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user and users.is_current_user_admin():
            self.response.headers['Content-Type'] = 'application/csv'
            self.response.headers['Content-Disposition'] = 'attachment; filename=participantes.csv'
            writer = csv.writer(self.response.out, delimiter=';', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(["Nome", "Data de Nascimento", "Sexo", "Identidade", "Familia",
                             "Logradouro", "Complemento", "Cidade", "UF", "Bairro", "Zona",
                             "Tel Celular1", "Tel Celular2", "Tel Residencial", "Email",
                             "Problema de Saude", "Restricao Atividade Fisica", "Tem Alguma Alergia", "Toma Algum Medicamento",
                             "Nome do Contato",
                             "Tel Celular1 Contato", "Tel Celular2 Contato", "Tel Residencial Contato", "Tel Comercial Contato",
                             "Familia", "Vai Levar Barraca"])
            
            for participante in Participante.all().order('nome'):
                writer.writerow([smart_str(participante.nome, encoding='ISO-8859-1'),
                                 smart_str(participante.dataNascimento, encoding='ISO-8859-1'),
                                 smart_str(participante.sexo, encoding='ISO-8859-1'),
                                 smart_str(participante.identidade, encoding='ISO-8859-1'),
                                 smart_str(participante.familia, encoding='ISO-8859-1'),
                                 smart_str(participante.logradouro, encoding='ISO-8859-1'),
                                 smart_str(participante.complemento, encoding='ISO-8859-1'),
                                 smart_str(participante.cidade, encoding='ISO-8859-1'),
                                 smart_str(participante.uf, encoding='ISO-8859-1'),
                                 smart_str(participante.bairro, encoding='ISO-8859-1'),
                                 smart_str(participante.zona, encoding='ISO-8859-1'),
                                 smart_str(participante.telCelular1, encoding='ISO-8859-1'),
                                 smart_str(participante.telCelular2, encoding='ISO-8859-1'),
                                 smart_str(participante.telResidencial, encoding='ISO-8859-1'),
                                 smart_str(participante.email, encoding='ISO-8859-1'),
                                 smart_str(participante.problemaSaude, encoding='ISO-8859-1'),
                                 smart_str(participante.restricaoAtividadeFisica, encoding='ISO-8859-1'),
                                 smart_str(participante.temAlgumaAlergia, encoding='ISO-8859-1'),
                                 smart_str(participante.tomaAlgumMedicamento, encoding='ISO-8859-1'),
                                 smart_str(participante.nomeContato, encoding='ISO-8859-1'),
                                 smart_str(participante.telCelular1Contato, encoding='ISO-8859-1'),
                                 smart_str(participante.telCelular2Contato, encoding='ISO-8859-1'),
                                 smart_str(participante.telResidencialContato, encoding='ISO-8859-1'),
                                 smart_str(participante.telComercialContato, encoding='ISO-8859-1'),
                                 smart_str(participante.familia, encoding='ISO-8859-1'),
                                 smart_str(participante.barraca, encoding='ISO-8859-1')
                                 ])
        
class ExportarServicoHandler(RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user and users.is_current_user_admin():
            self.response.headers['Content-Type'] = 'application/csv'
            self.response.headers['Content-Disposition'] = 'attachment; filename=servos.csv'
            writer = csv.writer(self.response.out, delimiter=';', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(["Nome", "Data de Nascimento", "Sexo", "Equipe",
                             "Logradouro", "Complemento", "Cidade", "UF", "Bairro",
                             "Tel Celular1", "Tel Celular2", "Tel Residencial", "Email", "Rede Social",
                             "Problema de Saude", "Restricao Atividade Fisica", "Tem Alguma Alergia", "Toma Algum Medicamento",
                             "Nome do Contato",
                             "Tel Celular1 Contato", "Tel Celular2 Contato", "Tel Residencial Contato", "Tel Comercial Contato",
                             "Setor que Participa", "Nome Grupo de Oracao", "Nome do Pastor", "Tipo de Membro"])
            
            for servico in Servico.all().order('nome'):
                writer.writerow([smart_str(servico.nome, encoding='ISO-8859-1'),
                                 smart_str(servico.dataNascimento, encoding='ISO-8859-1'),
                                 smart_str(servico.sexo, encoding='ISO-8859-1'),
                                 smart_str(servico.equipeServico, encoding='ISO-8859-1'),
                                 smart_str(servico.logradouro, encoding='ISO-8859-1'),
                                 smart_str(servico.complemento, encoding='ISO-8859-1'),
                                 smart_str(servico.cidade, encoding='ISO-8859-1'),
                                 smart_str(servico.uf, encoding='ISO-8859-1'),
                                 smart_str(servico.bairro, encoding='ISO-8859-1'),
                                 smart_str(servico.telCelular1, encoding='ISO-8859-1'),
                                 smart_str(servico.telCelular2, encoding='ISO-8859-1'),
                                 smart_str(servico.telResidencial, encoding='ISO-8859-1'),
                                 smart_str(servico.email, encoding='ISO-8859-1'),
                                 smart_str(servico.linkRedeSocial, encoding='ISO-8859-1'),
                                 smart_str(servico.problemaSaude, encoding='ISO-8859-1'),
                                 smart_str(servico.restricaoAtividadeFisica, encoding='ISO-8859-1'),
                                 smart_str(servico.temAlgumaAlergia, encoding='ISO-8859-1'),
                                 smart_str(servico.tomaAlgumMedicamento, encoding='ISO-8859-1'),
                                 smart_str(servico.nomeContato, encoding='ISO-8859-1'),
                                 smart_str(servico.telCelular1Contato, encoding='ISO-8859-1'),
                                 smart_str(servico.telCelular2Contato, encoding='ISO-8859-1'),
                                 smart_str(servico.telResidencialContato, encoding='ISO-8859-1'),
                                 smart_str(servico.telComercialContato, encoding='ISO-8859-1'),
                                 smart_str(servico.setorParticipa, encoding='ISO-8859-1'),
                                 smart_str(servico.nomeGrupoOracao, encoding='ISO-8859-1'),
                                 smart_str(servico.nomePastor, encoding='ISO-8859-1'),
                                 smart_str(servico.tipoMembro, encoding='ISO-8859-1')
                                 ])

class RelacaoIndicaoesHandler(RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user and users.is_current_user_admin():
            results = Indicacao.all().filter('nomeIndicacao !=', '').order('nomeIndicacao')
            
            self.response.out.write(template.render('pages/reports/relacaoIndicacoes.html',
                                                    {'listaItens':results}))


class ExportarIndicaoesHandler(RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user and users.is_current_user_admin():
            self.response.headers['Content-Type'] = 'application/csv'
            self.response.headers['Content-Disposition'] = 'attachment; filename=indicacoes.csv'
            writer = csv.writer(self.response.out, delimiter=';', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(["Nome", "Telefone Celular", "Telefone Residencial", "Email", "Indicado por"])
            
            for indicacao in Indicacao.all().filter('nomeIndicacao !=', '').order('nomeIndicacao'):
                writer.writerow([smart_str(indicacao.nomeIndicacao, encoding='ISO-8859-1'),
                                 smart_str(indicacao.telCelularIndicacao, encoding='ISO-8859-1'),
                                 smart_str(indicacao.telResidencialIndicacao, encoding='ISO-8859-1'),
                                 smart_str(indicacao.emailIndicacao, encoding='ISO-8859-1'),
                                 smart_str(indicacao.nome, encoding='ISO-8859-1')
                                 ])


application = webapp.WSGIApplication(
                                     [('/', HomeHandler),
                                      ('/inscricaoParticipante', InscricaoParticipanteHandler),
                                      ('/inscricaoServico', InscricaoServicoHandler),
                                      ('/informacoesImportantes', InformacoesImportantesHandler),
                                      ('/login', LoginHandler),
                                      ('/logout', LogoutHandler),
                                      ('/contato', ContatoHandler),
                                      ('/exportarParticipante', ExportarParticipantesHandler),
                                      ('/exportarServico', ExportarServicoHandler),
                                      ('/realizarPagamento', RealizarPagamentoHandler),
                                      ('/realizarPagamentoServico', RealizarPagamentoServicoHandler),
                                      ('/relacaoParticipantesInscritos', RelacaoParticipantesInscritosHandler),
                                      ('/relacaoServicosInscritos', RelacaoServicosInscritosHandler),
                                      ('/relacaoEstatisticaParticipantesInscritos', RelacaoEstatisticaParticipantesInscritosHandler),
                                      ('/relacaoIndicoes', RelacaoIndicaoesHandler),
                                      ('/exportarIndicacoes', ExportarIndicaoesHandler)
                                     ])
def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
