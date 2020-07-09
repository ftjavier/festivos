from datetime import datetime
from datetime import timedelta
import pandas as pd
import sys

# Parámetros de entrada :
# Fecha inicial : DD/MM/YYYY
# Número de días hábiles a contabilizar
# Municipio del cálculo : PPMMM  ( PP = Provincia + MMM = Municipio)

# Determina si es festivo nacional
def festivoEstatal(df,fec):
    valor=fec.strftime('%d/%m/%Y')
    kk = df[(df['ambito']=='estatal') & (df['fecha']==valor) ]
    return kk.shape[0]

# Determina si es festivo autonómico
def festivoAutonomico(df,fec):
    valor=fec.strftime('%d/%m/%Y')
    kk = df[(df['ambito']=='autonómico') & (df['fecha']==valor) ]
    return kk.shape[0]

# Determina si es festivo local
def festivoLocal(df,fec,mun):
    valor=fec.strftime('%d/%m/%Y')
    kk = df[(df['ambito']=='Local') & (df['fecha']==valor) & (df['id_mun']==mun) ]
    return kk.shape[0]

# Determinar si es festivo (global)
def festivo(df,fec,mun):
   
    if (festivoEstatal(df,fec) == 1):
        print(fec.strftime('%d/%m/%Y') + " es festivo estatal")
        return 1

    if (festivoAutonomico(df,fec) == 1):
        print(fec.strftime('%d/%m/%Y') + " es festivo autonómico")
        return 1  

    if (festivoLocal(df,fec,mun) == 1):
        print(fec.strftime('%d/%m/%Y') + " es festivo local en el municipio "  + str(mun))
        return 1  
    else:
        return 0

def main():
    fecha_str = sys.argv[1]
    fecha  = datetime.strptime(fecha_str, '%d/%m/%Y')
    numero = int(sys.argv[2])
    mun = int(sys.argv[3])

    conta = 0
    df= pd.read_csv('calendario_lab.csv',sep=';')

    while (conta < numero):
        if ((fecha.weekday() < 6) & (festivo(df,fecha,mun)==0)):
            conta=conta+1
            
        if (conta<numero):
            fecha = fecha + timedelta(days=1)

    print(fecha)

if __name__ == "__main__":
	main()
