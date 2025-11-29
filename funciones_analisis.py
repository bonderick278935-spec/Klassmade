import pandas as pd
import numpy as np

# Eliminación de decimanes

def eliminaDecimales(df: pd.DataFrame, col: str) -> pd.DataFrame:
    
    if col not in df.columns:
        raise KeyError(f"La columna '{col}' no se encuentra en el DataFrame.")
        
    new_col_name = f"{col}_sin_decimales"
    
    # np.trunc() trunca los valores, eliminando la parte decimal.
    df[new_col_name] = np.trunc(df[col])
    
    return df

# Cálculo del Ratio

def calculaRatio(df: pd.DataFrame, col1: str, col2: str) -> pd.DataFrame:
    
    if col1 not in df.columns or col2 not in df.columns:
        missing_col = [c for c in [col1, col2] if c not in df.columns]
        raise KeyError(f"Faltan las siguientes columnas en el DataFrame: {missing_col}")

    ratio_col_name = f"ratio_{col1}_a_{col2}"
    
    # Calcular el ratio
    df[ratio_col_name] = df[col1] / df[col2]
    
    if (df[ratio_col_name] > 1).any():
        raise ValueError(f"Al menos un valor en el ratio {ratio_col_name} es mayor que 1. Excepción generada según lo solicitado.")
        
    return df