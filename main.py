from flask import Flask, render_template,send_from_directory

app = Flask(__name__)

@app.route('/style/<path:filename>')
def serve_style(filename):
    return send_from_directory('style', filename)

@app.route('/')
def home():
    return render_template('home.html')

# Rotas para as outras páginas (vamos criar esses templates mais tarde)
@app.route('/servicos')
def quem_somos():
    return render_template('servicos.html')

@app.route('/projetos')
def meus_projetos():
    return render_template('projetos.html')

@app.route('/contato')
def meus_contato():
    return render_template('contato.html')

@app.route('/consultoria')
def solicitar_servicos():
    return render_template('consultoria.html')

@app.route('/privacidade')
def politica_de_privacidade():
    return render_template('politica_de_privacidade.html')

# Página de transformação com dados

@app.route('/previsao-de-demanda')
def previsao_demanda():
    return render_template('/transforcao_com_dados/previsao_demanda.html')

@app.route('/ia-de-atendimento')
def inteligencia_artificial():
    return render_template('/transforcao_com_dados/ia_atendimento.html')

@app.route('/otimizacao-de-portifolio')
def otimizacao_portifolio():
    return render_template('/transforcao_com_dados/otimizacao_portifolio.html')

# Página dos artigos
@app.route('/artigos')
def meus_artigos():
    return render_template('artigos.html')

@app.route('/artigos/como-ia-esta-mudando-o-mundo')
def meus_artigos1():
    return render_template('/publicacoes artigos/como-ia-esta-mudando-o-mundo.html')

@app.route('/artigos/machine-learning-otimizacoes')
def meus_artigos2():
    return render_template('/publicacoes artigos/machine-learning-otimizacoes.html')

@app.route('/artigos/analise-quantitativa-mercado-financeiro')
def meus_artigos3():
    return render_template('/publicacoes artigos/analise-quantitativa-mercado-financeiro.html')


if __name__ == '__main__':
    app.run(debug=True)
