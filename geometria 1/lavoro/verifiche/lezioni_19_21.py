"""Controlli esatti dei calcoli delle lezioni 19–21 (nessuna dipendenza esterna)."""
from fractions import Fraction as F
from pathlib import Path
import json

def matrix(rows):
    return [[F(x) for x in row] for row in rows]

def identity(n):
    return matrix([[int(i == j) for j in range(n)] for i in range(n)])

def product(a, b):
    assert len(a[0]) == len(b)
    return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]

def transpose(a):
    return [list(row) for row in zip(*a)]

def rref(a):
    a = matrix(a); row = 0; pivots = []
    for col in range(len(a[0])):
        pivot = next((i for i in range(row,len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        value = a[row][col]; a[row] = [x/value for x in a[row]]
        for i in range(len(a)):
            if i != row:
                value = a[i][col]
                a[i] = [x-value*y for x,y in zip(a[i],a[row])]
        pivots.append(col); row += 1
        if row == len(a):
            break
    return a, pivots

def inverse(a):
    n = len(a); reduced,pivots = rref([row+unit for row,unit in zip(a,identity(n))])
    assert pivots[:n] == list(range(n))
    assert [row[:n] for row in reduced] == identity(n)
    return [row[n:] for row in reduced]

def addrow(a,i,j,value):
    a[i] = [x+value*y for x,y in zip(a[i],a[j])]

def main():
    results = []
    # Esempio BA=A': verifica di entrambi gli stadi stampati e del prodotto finale.
    a = matrix([[1,3,-2],[2,5,1],[-1,0,3]])
    aug = [row+unit for row,unit in zip(a,identity(3))]
    addrow(aug,1,0,2*-1); addrow(aug,2,0,1)
    assert aug == matrix([[1,3,-2,1,0,0],[0,-1,5,-2,1,0],[0,3,1,1,0,1]])
    addrow(aug,2,1,3)
    assert aug == matrix([[1,3,-2,1,0,0],[0,-1,5,-2,1,0],[0,0,16,-5,3,1]])
    b = [row[3:] for row in aug]
    assert product(b,a) == [row[:3] for row in aug]
    results.append('Esempio BA=A′: due matrici intermedie e prodotto finale esatti')
    # Esercizio dell'inversa: ogni stadio e verifica in entrambi gli ordini.
    a = matrix([[2,-1,3],[-6,2,-5],[0,1,-3]])
    aug = [row+unit for row,unit in zip(a,identity(3))]
    addrow(aug,1,0,3)
    assert aug == matrix([[2,-1,3,1,0,0],[0,-1,4,3,1,0],[0,1,-3,0,0,1]])
    addrow(aug,2,1,1)
    assert aug == matrix([[2,-1,3,1,0,0],[0,-1,4,3,1,0],[0,0,1,3,1,1]])
    addrow(aug,1,2,-4); addrow(aug,0,2,-3)
    assert aug == matrix([[2,-1,0,-8,-3,-3],[0,-1,0,-9,-3,-4],[0,0,1,3,1,1]])
    aug[1] = [-x for x in aug[1]]; addrow(aug,0,1,1)
    assert aug == matrix([[2,0,0,1,0,1],[0,1,0,9,3,4],[0,0,1,3,1,1]])
    aug[0] = [x/2 for x in aug[0]]
    b = matrix([[F(1,2),0,F(1,2)],[9,3,4],[3,1,1]])
    assert [row[3:] for row in aug] == b
    assert product(a,b) == product(b,a) == identity(3)
    results.append('Inversa: tutti gli stadi stampati e AA⁻¹=A⁻¹A=I₃ verificati')
    # Matrici elementari su una matrice rettangolare: sinistra = righe.
    a = matrix([[1,2],[3,4],[5,6]])
    p = matrix([[0,1,0],[1,0,0],[0,0,1]])
    m = matrix([[1,0,0],[0,2,0],[0,0,1]])
    s = matrix([[1,0,0],[-3,1,0],[0,0,1]])
    assert product(p,a) == matrix([[3,4],[1,2],[5,6]])
    assert product(m,a) == matrix([[1,2],[6,8],[5,6]])
    assert product(s,a) == matrix([[1,2],[0,-2],[5,6]])
    assert product(p,p) == identity(3)
    assert product(m,matrix([[1,0,0],[0,F(1,2),0],[0,0,1]])) == identity(3)
    assert product(s,matrix([[1,0,0],[3,1,0],[0,0,1]])) == identity(3)
    results.append('Tre matrici elementari: effetto sulle righe e inverse verificate')
    # Due funzioni finite dei disegni e inverse da un solo lato.
    f = {1:1,2:2,3:3}; g = {1:1,2:2,3:3,4:1}
    assert all(g[f[x]] == x for x in f) and f[g[4]] != 4
    f = {1:1,2:2,3:3,4:3}; g = {1:1,2:2,3:3}
    assert all(f[g[x]] == x for x in g) and g[f[4]] != 4
    results.append('Mappe dei due diagrammi: identità e controesempi delle composizioni verificati')
    # Base duale non canonica: le righe della matrice inversa sono i funzionali.
    basis = matrix([[1,1,0],[0,1,1],[1,0,1]])
    dual = inverse(basis)
    assert product(dual,basis) == identity(3)
    coeff = matrix([[2],[-3],[5]]); v = product(basis,coeff)
    assert product(dual,v) == coeff
    functional = matrix([[3,2,-1]])
    values = product(functional,basis)
    assert product(values,dual) == functional
    results.append('Base duale non canonica: delta, lettura delle coordinate, espansione di un funzionale')
    # Annullatore concreto e trasposta della mappa R²→R³.
    ann = matrix([[1,-1,0],[0,0,1]])
    assert product(ann,matrix([[1],[1],[0]])) == matrix([[0],[0]])
    assert len(rref(ann)[1]) == 2
    a = matrix([[1,2],[0,3],[-1,1]])
    at = transpose(a)
    assert at == matrix([[1,0,-1],[2,3,1]])
    assert product(at,matrix([[1],[-1],[1]])) == matrix([[0],[0]])
    assert len(rref(a)[1]) == len(rref(at)[1]) == 2
    for x in (matrix([[2],[-1]]),matrix([[0],[3]])):
        for psi in (matrix([[1],[-2],[3]]),matrix([[0],[4],[-1]])):
            assert product(transpose(product(at,psi)),x) == product(transpose(psi),product(a,x))
    results.append('Annullatore di una retta; matrice trasposta; rango e identità di valutazione verificati')
    target = Path(__file__).resolve().parents[1]/'CONTROLLI_LEZIONI_19-21_2026-11-12.json'
    target.write_text(json.dumps(dict(data='2026-11-12',aritmetica='frazioni esatte',esiti=results),ensure_ascii=False,indent=2)+'\n')
    print('\n'.join(results))

if __name__ == '__main__':
    main()
