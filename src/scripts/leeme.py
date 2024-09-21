import argparse
import os
from gtts import gTTS
import PyPDF2
import pygame
from pydub import AudioSegment

def leer_archivo_texto(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        return archivo.read()
    
def leer_archivo_pdf(ruta_archivo):
    texto = ""
    with open(ruta_archivo, 'rb') as archivo:
        lector = PyPDF2.PdfReader(archivo)
        for pagina in lector.pages:
            texto += pagina.extract_text()
    return texto

def texto_a_voz(texto, idioma='es'):
    return gTTS(text=texto, lang=idioma, slow=False)

def reproducir_audio(audio):
    pygame.mixer.init()
    pygame.mixer.music.load(audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def main():
    parser = argparse.ArgumentParser(description='Convierte texto a voz desde archivos de texto o PDF.')
    parser.add_argument('archivo', help='Ruta al archivo de texto o PDF')
    parser.add_argument('-o', '--output', help='Ruta para guardar el archivo de audio MP3')
    parser.add_argument('-p', '--play', action='store_true', help='Reproducir el audio inmediatamente')
    parser.add_argument('-l', '--lang', default='es', help='Idioma del texto (código ISO 639-1, por defecto es español)')
    args = parser.parse_args()

    # Leer el archivo
    if args.archivo.lower().endswith('.pdf'):
        texto = leer_archivo_pdf(args.archivo)
    else:
        texto = leer_archivo_texto(args.archivo)

    # Convertir texto a voz
    audio = texto_a_voz(texto, args.lang)

    # Guardar o reproducir el audio
    if args.output:
        audio.save(args.output)
        print(f"Audio guardado como {args.output}")
    elif args.play:
        temp_file = "temp_audio.mp3"
        audio.save(temp_file)
        reproducir_audio(temp_file)
        os.remove(temp_file)
    else:
        print("Debe especificar -o para guardar o -p para reproducir el audio.")

if __name__ == "__main__":
    main()

'''
pip install gTTS PyPDF2 pygame pydub

python leeme.py archivo.txt -o salida.mp3

python script.py archivo.pdf -o salida.mp3

python script.py archivo.txt -p

# Para especificar un idioma distinto, por ejemplo inglés
python script.py archivo.txt -o salida.mp3 -l en

'''