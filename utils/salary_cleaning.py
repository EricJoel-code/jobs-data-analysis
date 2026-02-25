import pandas as pd
from config import INTERVAL_FACTORS

# Esta clase se encarga de procesar los salarios obtenidos del scraper, transformándolos a una base anual utilizando los factores de conversión definidos en el archivo de configuración. Además, calcula el salario promedio a partir de los salarios mínimo y máximo.
class SalaryProcessor:
    def __init__(self):
        self.interval_factors = INTERVAL_FACTORS
        
    def transform_salary(self, row):
        row['max_salary'] = row['max_amount']
        row['min_salary'] = row['min_amount']
    
        factor = self.interval_factors.get(row['interval'],1)
        
        row['min_salary'] *= factor
        row['max_salary'] *= factor
        
        if row['min_salary'] > 1000000:
            row['min_salary'] /= 1000
        if row['max_salary'] > 1000000:
            row['max_salary'] /= 1000
            
        return row
    
    def clean_salaries(self, df):
        df = df.apply(self.transform_salary, axis=1)
        df['mean_salary'] = (df['min_salary'] + df['max_salary']) / 2
        
        return df
    