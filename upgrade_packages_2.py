#Trabajo sobre el mismo archivo generado
import os

path = 'actualizar_paquetes_pip/requirements.txt'

os.system('pip freeze --> ' + path)

pack = open(path,mode='r',encoding='utf-8')
data = pack.read()
data = data.replace('==','>=')
pack.close()

pack = open(path,mode='w',encoding='utf-8')
pack.write(data)
pack.close()

os.system('pip install -r ' + path + ' --upgrade')



