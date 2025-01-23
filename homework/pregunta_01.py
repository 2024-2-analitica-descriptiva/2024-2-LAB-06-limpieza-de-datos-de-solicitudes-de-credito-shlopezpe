"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

import pandas as pd 
import os 

def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    file_path = 'files/input/solicitudes_de_credito.csv'  # Ruta del archivo de entrada
    output_dir = 'files/output'  # Carpeta de salida
    file_name = 'solicitudes_de_credito.csv'
    
    data = pd.read_csv(file_path, sep=';')
    
    data.drop(['Unnamed: 0'], axis=1, inplace=True)  # Elimina columna no necesaria
    data.dropna(inplace=True)  # Elimina filas con valores nulos
    data.drop_duplicates(inplace=True)  # Elimina filas duplicadas
    
    #fecha de beneficio en formato 
    data[['día', 'mes', 'año']] = data['fecha_de_beneficio'].str.split('/', expand=True)
    data.loc[data['año'].str.len() < 4, ['día', 'año']] = data.loc[data['año'].str.len() < 4, ['año', 'día']].values
    data['fecha_de_beneficio'] = data['año'] + '-' + data['mes'] + '-' + data['día']
    data.drop(['día', 'mes', 'año'], axis=1, inplace=True)
    
    #limpiar columnas 
    columns = ['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'línea_credito']
    data[columns] = data[columns].apply(lambda x: x.str.lower().replace(['-', '_'], ' ', regex=True).str.strip())
    data['barrio'] = data['barrio'].str.lower().replace(['-', '_'], ' ', regex=True)

    #monto a valores numericos
    data['monto_del_credito'] = (data['monto_del_credito'].str.replace("[$, ]", "", regex=True).str.strip())
    data['monto_del_credito'] = pd.to_numeric(data['monto_del_credito'], errors='coerce').fillna(0).astype(int)
    
    #limpiar datos
    data.drop_duplicates(inplace=True)
    
    #guardar archivo 
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, file_name)
    data.to_csv(output_path, sep=';', index=False)
    print(f"Archivo guardado exitosamente en: {output_path}")

    return data.head()
    
print(pregunta_01())
    
