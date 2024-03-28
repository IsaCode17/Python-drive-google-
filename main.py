import requests
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Función para descargar el archivo desde el enlace
def descargar_archivo(url, nombre_archivo):
    response = requests.get(url)
    with open(nombre_archivo, 'wb') as f:
        f.write(response.content)

# Función para subir el archivo a Google Drive
def subir_a_google_drive(nombre_archivo):
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)

    file = drive.CreateFile({'title': nombre_archivo})
    file.SetContentFile(nombre_archivo)
    file.Upload()

    print("Archivo subido a Google Drive con éxito.")

if __name__ == "__main__":
    url_archivo = "http://6e12df52d69342.lhr.life/Archivoh0.zip"
    nombre_archivo = "archivo_descargado.zip"

    # Descargar el archivo desde el enlace
    descargar_archivo(url_archivo, nombre_archivo)

    # Subir el archivo a Google Drive
    subir_a_google_drive(nombre_archivo)
