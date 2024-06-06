# API Rest - Python - Mares

## Desenvolvedores
| Desenvolvedor | Avatar | RM |
| ------------- | ------ | -- |
| ![](https://img.shields.io/badge/DESENVOLVEDOR-JoãoVictor-blue?style=for-the-badge&logo=appveyor) | <a href="https://github.com/jota0802"><img src="https://avatars.githubusercontent.com/u/161319025?v=4" height="50" style="max-width: 100%;"></a> | RM556790 |
| ![](https://img.shields.io/badge/DESENVOLVEDOR-LuizGustavo-blue?style=for-the-badge&logo=appveyor) | <a href="https://github.com/luyz-gusta"><img src="https://avatars.githubusercontent.com/u/110852235?v=4" height="50" style="max-width: 100%;"></a> | RM558358 |
| ![](https://img.shields.io/badge/DESENVOLVEDOR-Marcello-blue?style=for-the-badge&logo=appveyor) | <a href="https://github.com/MarcelloFMoreira"><img src="https://avatars.githubusercontent.com/u/161846509?v=4" height="50" style="max-width: 100%;"></a> | RM557531 |



## Sobre

Esta API em Flask simula um sistema de monitoramento de mares, permitindo a manipulação e consulta de informações sobre diferentes mares a partir de um arquivo JSON, onde futuramente os dados virão do IoT. A API permite realizar operações CRUD (Create, Read, Update, Delete) nos dados de mares.

## Como rodar a aplicação localmente (Após a clonagem)

- 1º Instale o python (caso não tenha);
- 2º Instale o pip (caso não tenha);
- 3º Baixe as seguintes dependências:
<pre>
pip install flask
</pre>
<pre>
pip install flask-cors
</pre>
- 4º Abra o terminal e execute o comando: python app.py
- 5º Os endpoints estará disponiveis no ip: http://127.0.0.1:5000

## Endpoints

- / (GET): Retorna uma mensagem de boas-vindas em formato JSON.
- /todos_mares (GET): Retorna uma lista de todos os mares com suas informações.
- /get_mar/<int:mar_id> (GET): Retorna as informações de um mar específico pelo seu ID.
- /add_mar (POST): Adiciona um novo mar à lista de mares.
- /update_mar/<int:mar_id> (PUT): Atualiza as informações de um mar existente.
- /delete_mar/<int:mar_id> (DELETE): Remove um mar da lista de mares.

## Informações Relevantes
- Arquivo JSON: Os dados dos mares são armazenados em um arquivo mares.json, que deve estar no mesmo diretório que o arquivo app.py.


