$(document).ready(function() {

	$('#dataNascimento').mask('00/00/0000');

	$("#contatoForm").validate({
		rules : {
			nome : {
				required : true
			},
			telCelular1 : {
				required : true
			},
			email : {
				required : true,
				email : true
			},
			comentario : {
				required : true
			}
		},
		messages : {
			nome : {
				required : "Campo obrigatório."
			},
			telCelular1 : {
				required : "Campo obrigatório."
			},
			email : {
				required : "Campo obrigatório.",
				email : "E-mail inválido."
			},
			comentario : {
				required : "Campo obrigatório."
			}
		}
	});

	$("#inscricaoParticipanteForm").validate({
		rules : {
			nome : {
				required : true
			},
			dataNascimento : {
				required : true,
				dateBR : true
			},
			sexo : {
				required : true
			},
			identidade : {
				required : true
			},
			logradouro : {
				required : true
			},
			cidade : {
				required : true
			},
			bairro : {
				required : true
			},
			uf : {
				required : true
			},
			telCelular1 : {
				required : true
			},
			email : {
				required : true
			},
			nomeContato : {
				required : true
			},
			telCelular1Contato : {
				required : true
			}
		},
		messages : {
			nome : {
				required : "Campo obrigatório."
			},
			dataNascimento : {
				required : "Campo obrigatório.",
				dateBR : "Data de nascimento inválida."
			},
			sexo : {
				required : "Campo obrigatório."
			},
			identidade : {
				required : "Campo obrigatório."
			},
			logradouro : {
				required : "Campo obrigatório."
			},
			cidade : {
				required : "Campo obrigatório."
			},
			bairro : {
				required : "Campo obrigatório."
			},
			uf : {
				required : "Campo obrigatório."
			},
			telCelular1 : {
				required : "Campo obrigatório."
			},
			email : {
				required : "Campo obrigatório.",
				email : "E-mail inválido."
			},
			nomeContato : {
				required : "Campo obrigatório."
			},
			telCelular1Contato : {
				required : "Campo obrigatório."
			}
		}
	});

	$("#inscricaoServicoForm").validate({
		rules : {
			nome : {
				required : true
			},
			dataNascimento : {
				required : true,
				dateBR : true
			},
			sexo : {
				required : true
			},
			logradouro : {
				required : true
			},
			cidade : {
				required : true
			},
			bairro : {
				required : true
			},
			uf : {
				required : true
			},
			telCelular1 : {
				required : true
			},
			email : {
				required : true
			},
			nomeContato : {
				required : true
			},
			telCelular1Contato : {
				required : true
			}
		},
		messages : {
			nome : {
				required : "Campo obrigatório."
			},
			dataNascimento : {
				required : "Campo obrigatório.",
				dateBR : "Data de nascimento inválida."
			},
			sexo : {
				required : "Campo obrigatório."
			},
			logradouro : {
				required : "Campo obrigatório."
			},
			cidade : {
				required : "Campo obrigatório."
			},
			bairro : {
				required : "Campo obrigatório."
			},
			uf : {
				required : "Campo obrigatório."
			},
			telCelular1 : {
				required : "Campo obrigatório."
			},
			email : {
				required : "Campo obrigatório.",
				email : "E-mail inválido."
			},
			nomeContato : {
				required : "Campo obrigatório."
			},
			telCelular1Contato : {
				required : "Campo obrigatório."
			}
		}
	});
});