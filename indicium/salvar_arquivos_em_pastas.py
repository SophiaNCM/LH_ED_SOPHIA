import datetime
import os
import shutil

path = '/home/sophia/DesafioIndicium/indicium/csvParaIncluir'
data_atual = datetime.date.today()
Newpath = '/home/sophia/DesafioIndicium/indicium/data/csv'
files = os.listdir(path)
for file in files:
    txtfile = file[:-4:]
    os.rename(f'/home/sophia/DesafioIndicium/indicium/csvParaIncluir/{file}',f'{Newpath}/{txtfile}/'+data_atual.strftime('%Y-%m-%d')+f'/public-{file}')
