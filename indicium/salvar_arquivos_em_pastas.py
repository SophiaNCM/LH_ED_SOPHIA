import datetime
import os
import shutil

path = '/home/sophia/DesafioIndicium/indicium/csvParaIncluir'
data_atual = datetime.date.today()
Newpath = '/home/sophia/DesafioIndicium/indicium/indicium_output'
files = os.listdir(path)
for file in files:
    txtfile = file[:-4:]
    os.rename(f'/home/sophia/DesafioIndicium/indicium/csvParaIncluir/{file}',f'{Newpath}\public-{file}')