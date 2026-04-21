from typing import Generator
import pandas as pd
from pathlib import Path
#pip install openpyxl   

def extract_losses() -> Generator[tuple[pd.DataFrame, str], None, None]:

    path_value = 'ETLStuff/energy-losses.xlsx'
    
    if not path_value:
        raise ValueError("CSV_FILE_PATH environment variable is not set.")

    path = Path(path_value)

    print(path)

    # df = pd.read_excel('C:\\Users\\jonas\\OneDrive\\Documentos\\GitHub\\pythonMonoRepoTest\\ETLStuff\\energy-losses.xlsx')
    df = pd.read_excel(path)
    data_dict = df.to_dict(orient='records')
    
    # print(data_dict[1]['UF'])
    print(data_dict[1])

def extract_limits():
    path_value = 'ETLStuff/indicadores-continuidade-coletivos-limite.csv'
    
    if not path_value:
        raise ValueError("LIMITS_FILE_PATH environment variable is not set.")

    path = Path(path_value)

    df : pd.DataFrame = pd.read_csv(path, sep=";", encoding="latin-1", low_memory=False)
    data_dict = df.to_dict(orient='records')

    print(data_dict[0])

# extract_losses()
extract_limits()