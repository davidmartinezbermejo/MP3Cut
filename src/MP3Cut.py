'''
from pydub import AudioSegment

sound = AudioSegment.from_mp3("/path/to/file.mp3")

# len() and slicing are in milliseconds
halfway_point = len(sound) / 2
second_half = sound[halfway_point:]

# Concatenation is just adding
second_half_3_times = second_half + second_half + second_half

# writing mp3 files is a one liner
second_half_3_times.export("/path/to/new/file.mp3", format="mp3")
'''
import sys
import os
from pydub import AudioSegment

path_source = sys.argv[1]
path_results = sys.argv[2]

contenido = os.listdir(path_source)
for fichero in contenido:
    if os.path.isfile(os.path.join(path_source, fichero)) and fichero.endswith('.mp3'):
        path_fichero = os.path.join(path_source, fichero)
        path_base_result = path_results + fichero[:len(fichero)-4]

        sound = AudioSegment.from_mp3(path_fichero)

        minutos_partes_arg = sys.argv[3]
        minutos_partes = int(minutos_partes_arg)*60*1000

        millis = 0
        index = 0
        while millis < len(sound):
            parte = sound[millis:millis+minutos_partes]
            parte.export(path_base_result+'_'+str(index)+'.mp3', format="mp3")
            index += 1
            millis += minutos_partes
