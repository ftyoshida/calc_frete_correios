import cherrypy
import urllib
import xmltodict
import json
import requests

class MyWebService(object):

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def calc_frete_correios(self):
        variables = cherrypy.request.json
        url_entrada = 'http://ws.correios.com.br/calculador/CalcPrecoPrazo.aspx?nCdEmpresa='+variables["nCdEmpresa"]+'&sDsSenha='+variables["sDsSenha"]+'&sCepOrigem='+variables["sCepOrigem"]+'&sCepDestino='+variables["sCepDestino"]+'&nVlPeso='+variables["nVlPeso"]+'&nCdFormato='+variables["nCdFormato"]+'&nVlComprimento='+variables["nVlComprimento"]+'&nVlAltura='+variables["nVlAltura"]+'&nVlLargura='+variables["nVlAltura"]+'&sCdMaoPropria='+variables["sCdMaoPropria"]+'n&nVlValorDeclarado='+variables["nVlValorDeclarado"]+'&sCdAvisoRecebimento='+variables["sCdAvisoRecebimento"]+'&nCdServico='+variables["nCdServico"]+'&nVlDiametro='+variables["nVlDiametro"]+'&StrRetorno=xml'
        my_xml = urllib.request.urlopen(url_entrada)
        return xmltodict.parse(my_xml)

if __name__ == '__main__':
    config = {'server.socket_host': '0.0.0.0'}
    cherrypy.config.update(config)
    cherrypy.quickstart(MyWebService())
