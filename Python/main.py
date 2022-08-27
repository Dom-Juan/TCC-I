import numpy as np

def _LU_(Matriz):
  tamanho = Matriz.shape[0] # Pega o tamanho da matriz.
  U = Matriz.copy() # Copia a matriz original para a uper.
  L = np.eye(tamanho, dtype=np.double) # Cria uma matriz do tamanho da original para L.
  # Indo até o tamanho da matriz.
  for i in range(tamanho):
    pivo = U[i+1:,i]/U[i,i] # Calcula o Pivo
    L[i+1:,i] = pivo # A lower é composta de pivos.
    U[i+1:] -= pivo[:, np.newaxis] * U[i] # Substrai o pivo a todas as linhas da matriz com o pivo.
  return L, U # Retorna o resultado das duas matrizes.


m = np.array([
  [2, -1, 1],
  [3, 3, 9],
  [3, 3, 5]
  ], dtype='float')

L_a, U_a = _LU_(m)

print(L_a)
print(U_a)

import pandas as pd

s= pd.Series([10, 20, 30, 40, 50, 60])
print(s)