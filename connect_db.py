import http.client
import urllib.parse

# URL del endpoint; La ruta de bd es indiferente
url = '/sqlite_sequence/query/' # Usamos la tabla por defecto, ya que no importa qué tabla se usa para conectar
host = '192.168.21.95:8083' #'127.0.0.1:8080'

# Datos a enviar en la solicitud POST
data = {
    'sql': 'SELECT * FROM meteo_granadilla limit 42;',
    'export_json': ''
}

# Codificar los datos en formato URL
params = urllib.parse.urlencode(data)
headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}

# Crear la conexión; Timeout de 10 segundos
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