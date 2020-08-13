#Trabajo generando un nuevo archivo
import os

path_origen = 'actualizar_paquetes_pip/requirements_actual.txt'
path_dest = 'actualizar_paquetes_pip/requirements.txt'

os.system('pip freeze --> ' + path_origen)

pack_origen = open(path_origen,mode='r',encoding='utf-8')
pack_dest = open(path_dest,mode='w',encoding='utf-8')

for linea in pack_origen.readlines():        
    #Muestro los paquetes a actualizar
    print(linea.replace('==','>='))
    #Grabo en el archivo de salida los cambios
    pack_dest.write(linea.replace('==','>='))

pack_dest.close()
pack_origen.close()

os.system('pip install -r ' + path_dest + ' --upgrade')

