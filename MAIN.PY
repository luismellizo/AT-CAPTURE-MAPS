import pandas as pd
import requests
import os
import time

# NOTAS# Ruta del archivo Excel
excel_file = r"D:\FOTOS\Libro2.xlsx"

# NOTAS# Directorio de destino para las imágenes
output_dir = r"D:\FOTOS"

# NOTAS# Tu clave de API de Google Maps Platform
api_key = "AIzaSyDilyA_JM6QZxUbZP2K1haYTPUBV32L8Fk"

# NOTAS# Leer el archivo Excel
df = pd.read_excel(excel_file)

# NOTAS# Crear el directorio de destino si no existe
os.makedirs(output_dir, exist_ok=True)

# NOTAS# Iterar sobre las filas del DataFrame
for _, row in df.iterrows():
    asset = str(row["ASSET"])
    latitud = str(row["LATITUD"])
    longitud = str(row["LONGITUD"])

    # NOTAS# Construir la URL de la imagen satelital
    url = f"https://maps.googleapis.com/maps/api/staticmap?center={latitud},{longitud}&zoom=18&size=800x600&maptype=satellite&key={api_key}"

    try:
        # NOTAS# Realizar la solicitud GET a la URL
        response = requests.get(url)
        response.raise_for_status()  # NOTAS# Verificar si hay errores en la respuesta

        # NOTAS# Guardar la imagen en el directorio de destino
        image_path = os.path.join(output_dir, f"{asset}.png")
        with open(image_path, "wb") as f:
            f.write(response.content)

        print(f"Imagen guardada para el asset {asset}")

    except requests.exceptions.RequestException as e:
        print(f"Error al obtener la imagen para el asset {asset}: {e}")

    # NOTAS# Agregar tiempo de espera de 5 segundos
    time.sleep(5)

print("Proceso completado.")
