import datetime
import os, shutil

data_atual = datetime.date.today()
path = '/home/sophia/DesafioIndicium/indicium/indicium_output/'
newPath = '/home/sophia/DesafioIndicium/indicium/data/csv'
files = os.listdir(path)
for file in files:
    txtfile = file[:-4:]
    os.makedirs(f'{newPath}/{txtfile}/'+data_atual.strftime('%Y-%m-%d'))
    os.replace(f'/home/sophia/DesafioIndicium/indicium/indicium_output/{file}',f"{newPath}/{txtfile}/"+data_atual.strftime('%Y-%m-%d')+ f'/{file}')