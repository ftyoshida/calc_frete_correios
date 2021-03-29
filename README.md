# calc_frete_correios
Calculo de frete e prazo dos Correios


Exemplo de envio dos dados da encomenda JSON via POST:

Content-Type : application/json

{
"nCdEmpresa": "",
"sDsSenha": "",
"nCdServico": "41106",
"sCepOrigem": "04307000",
"sCepDestino": "42810280",
"nVlPeso": "10",
"nCdFormato": "1",
"nVlComprimento": "30",
"nVlAltura": "20",
"nVlLargura": "20",
"nVlDiametro": "0",
"sCdMaoPropria": "n",
"nVlValorDeclarado": "0",
"sCdAvisoRecebimento": "n"
}

Codigos de Servico (nCdServico)

Código	:	Serviço
04014	:	SEDEX à vista
04510	:	PAC à vista
04782	:	SEDEX 12 ( à vista)
04790	:	SEDEX 10 (à vista)
04804	:	SEDEX Hoje à vista

Fonte:
https://www.correios.com.br/enviar-e-receber/ferramentas/calculador-remoto-de-precos-e-prazos/pdf/manual-de-implementacao-do-calculo-remoto-de-precos-e-prazos


Exemplo de retorno dos dados do frete em JSON:

{
    "Servicos": {
        "cServico": {
            "Codigo": "41106",
            "Valor": "61,50",
            "PrazoEntrega": "6",
            "ValorSemAdicionais": "61,50",
            "ValorMaoPropria": "0,00",
            "ValorAvisoRecebimento": "0,00",
            "ValorValorDeclarado": "0,00",
            "EntregaDomiciliar": "S",
            "EntregaSabado": "N",
            "obsFim": null,
            "Erro": "0",
            "MsgErro": null
        }
    }


Criar a imagem Docker:
$ sudo docker build -t calc-frete-ws .

Executar container Docker:
$ sudo docker run -p 8080:8080 calc-frete-ws

