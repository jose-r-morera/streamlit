import http.client
import urllib.parse

# URL del endpoint
url = '/meteo_granadilla/query/'
host = '127.0.0.1:8080'

# Datos a enviar en la solicitud POST
data = {
    'sql': 'SELECT * FROM meteo_granadilla limit 42;',
    'export_json': ''
}

# Codificar los datos en formato URL
params = urllib.parse.urlencode(data)
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

# Crear la conexión
conn = http.client.HTTPConnection(host, timeout=10)

# Realizar la solicitud POST
conn.request("POST", url, params, headers)

# Obtener la respuesta
response = conn.getresponse()

# Verificar si la solicitud fue exitosa
if response.status == 200:
    # Leer la respuesta
    data = response.read()
    print(data)
else:
    print(f"Error en la solicitud: {response.status}")

# Cerrar la conexión
conn.close()