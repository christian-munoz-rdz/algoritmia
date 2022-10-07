import numpy as np
import pandas as pd

def simplex():
    #Funcion objetivo
    Z = np.array([1,-10,-20])

    #restricciones
    A = np.array([[4,2],
                  [8,8],
                  [0,2]])

    #coeficientes de las restricciones
    b = np.array([[20],
                  [20],
                  [10]])

    #Matriz de olgura
    S = np.array([[1,0,0],
                  [0,1,0],
                  [0,0,1]])

    indexes = np.array([["s1"],
                      ["s2"],
                      ["s3"],
                      ["z"],])
    z = np.zeros((3,1),dtype=int)
    df = pd.DataFrame(np.hstack((z,A,S,b)), columns=['z','x1','x2','s1','s2','s3','CR'])
    df = df.append(pd.Series(np.hstack((Z,[0,0,0,0])), index=df.columns), ignore_index=True)
    df = pd.DataFrame(np.hstack((indexes)), columns=["b_var"]).join(df)
    df.set_index("b_var", inplace=True)
    print(df)
    pivot_col = df.loc["z"].idxmin()
    pivot_row = (df.loc[df[pivot_col] > 0, "CR"]/df.loc[df[pivot_col] > 0, pivot_col]).idxmin()
    pivot_element = df.loc[pivot_row, pivot_col]
    print(pivot_row, pivot_col, pivot_element)

    #tabla simplex 2
    df.loc[pivot_row] = df.loc[pivot_row]/pivot_element
    for i in df.index:
        if i != pivot_row:
            df.loc[i] = df.loc[i] - df.loc[i, pivot_col]*df.loc[pivot_row]
    #confirmacion de solucion optima
    if df.loc["z"].min() >= 0:
        print("solucion optima encontrada")
        print(df)
    
    else:
        print("solucion no optima")
        print(df)
        simplex()
    
    #resultado
    print("x1 = ", df.loc["s1", "CR"])
    print("x2 = ", df.loc["s2", "CR"])
    print("z = ", df.loc["z", "CR"])



if __name__ == "__main__":
    simplex()

