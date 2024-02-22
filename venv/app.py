from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def get_list_characters():
    url = 'https://rickandmortyapi.com/api/character/'
    response = urllib.request.urlopen(url)
    characters_json = response.read()
    characters_dict = json.loads(characters_json)
    
    characters = []
    for character in characters_dict['results']:
        character_info = {
            'name': character['name'],
            'gender': character['gender'],
            'species': character['species'],
            'status': character['status']
        }
        characters.append(character_info)

    return {'characters': characters}

# Rota para listar as localizações
@app.route('/locations')
def locations():
    # Faz uma requisição à API para obter os dados das localizações
    response = requests.get('https://rickandmortyapi.com/api/location')
    # Verifica se a requisição foi bem sucedida
    if response.status_code == 200:
        # Extrai os dados das localizações da resposta JSON
        locations_data = response.json()['results']
        # Renderiza o template locations.html passando os dados das localizações
        return render_template('locations.html', locations=locations_data)
    else:
        # Se houver erro na requisição, retorna uma mensagem de erro
        return "Erro ao obter dados das localizações"

# Rota para listar os episódios
@app.route('/episodes')
def episodes():
    # Faz uma requisição à API para obter os dados dos episódios
    response = requests.get('https://rickandmortyapi.com/api/episode')
    # Verifica se a requisição foi bem sucedida
    if response.status_code == 200:
        # Extrai os dados dos episódios da resposta JSON
        episodes_data = response.json()['results']
        # Renderiza o template episodes.html passando os dados dos episódios
        return render_template('episodes.html', episodes=episodes_data)
    else:
        # Se houver erro na requisição, retorna uma mensagem de erro
        return "Erro ao obter dados dos episódios"

# Rota para exibir o perfil da localização
@app.route('/location/<int:id>')
def location(id):
    # Faz uma requisição à API para obter os dados da localização específica
    response = requests.get(f'https://rickandmortyapi.com/api/location/{id}')
    # Verifica se a requisição foi bem sucedida
    if response.status_code == 200:
        # Extrai os dados da localização da resposta JSON
        location_data = response.json()
        # Renderiza o template location.html passando os dados da localização
        return render_template('location.html', location=location_data)
    else:
        # Se houver erro na requisição, retorna uma mensagem de erro
        return f"Erro ao obter dados da localização {id}"

# Rota para exibir o perfil do episódio
@app.route('/episode/<int:id>')
def episode(id):
    # Faz uma requisição à API para obter os dados do episódio específico
    response = requests.get(f'https://rickandmortyapi.com/api/episode/{id}')
    # Verifica se a requisição foi bem sucedida
    if response.status_code == 200:
        # Extrai os dados do episódio da resposta JSON
        episode_data = response.json()
        # Renderiza o template episode.html passando os dados do episódio
        return render_template('episode.html', episode=episode_data)
    else:
        # Se houver erro na requisição, retorna uma mensagem de erro
        return f"Erro ao obter dados do episódio {id}"
    # Rota para o favicon.ico
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    app.run(debug=True)









