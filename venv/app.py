from flask import Flask, render_template, redirect, url_for
import requests
import os  # Adicionamos a importação do módulo os para acessar variáveis de ambiente

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def index():
    return redirect(url_for('locations'))

# Rota para listar as localizações
@app.route('/locations')
def locations():
    # Faz uma requisição à API para obter os dados das localizações
    response = requests.get('https://rickandmortyapi.com/api/location')
    # Extrai os dados das localizações da resposta JSON
    locations_data = response.json()['results']
    # Renderiza o template locations.html passando os dados das localizações
    return render_template('locations.html', locations=locations_data)

# Rota para listar os episódios
@app.route('/episodes')
def episodes():
    # Faz uma requisição à API para obter os dados dos episódios
    response = requests.get('https://rickandmortyapi.com/api/episode')
    # Extrai os dados dos episódios da resposta JSON
    episodes_data = response.json()['results']
    # Renderiza o template episodes.html passando os dados dos episódios
    return render_template('episodes.html', episodes=episodes_data)

# Rota para exibir o perfil da localização
@app.route('/location/<int:id>')
def location(id):
    # Faz uma requisição à API para obter os dados da localização específica
    response = requests.get(f'https://rickandmortyapi.com/api/location/{id}')
    # Extrai os dados da localização da resposta JSON
    location_data = response.json()
    # Renderiza o template location.html passando os dados da localização
    return render_template('location.html', location=location_data)

# Rota para exibir o perfil do episódio
@app.route('/episode/<int:id>')
def episode(id):
    # Faz uma requisição à API para obter os dados do episódio específico
    response = requests.get(f'https://rickandmortyapi.com/api/episode/{id}')
    # Extrai os dados do episódio da resposta JSON
    episode_data = response.json()
    # Renderiza o template episode.html passando os dados do episódio
    return render_template('episode.html', episode=episode_data)

if __name__ == "__main__":
    # Porta obtida da variável de ambiente PORT, ou padrão 5000 se não estiver definida
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)


