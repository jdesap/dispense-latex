"""Controlli aritmetici della dispensa attiva; non sostituiscono le prove generali."""
from fractions import Fraction as F
from pathlib import Path
import json
from lezioni_19_21 import matrix as M, identity as I, product as P, transpose as T, inverse as Inv, rref, main as checks_19_21

def rank(a): return len(rref(a)[1])
def cols(*vectors): return T(M(vectors))
def join(a,b): return [x+y for x,y in zip(a,b)]
def zero(m,n): return M([[0]*n for _ in range(m)])
def kernel(a):
    reduced,pivots=rref(a); n=len(a[0]); free=[j for j in range(n) if j not in pivots]
    out=[]
    for j in free:
        x=[F(0)]*n; x[j]=1
        for row,pivot in enumerate(pivots): x[pivot]=-reduced[row][j]
        out.append(x)
    return T(out) if out else [[] for _ in range(n)]
def add(a,b): return [[x+y for x,y in zip(row,col)] for row,col in zip(a,b)]
def scale(a,c): return [[c*x for x in row] for row in a]

def main():
    results=[]
    # Assiomi e sottospazi: controesempi presentati e intersezioni.
    assert (1+0)+(0+1) != 1
    assert (-1)*1 < 0
    assert 1**2-2*F(1,2)==0 and 2**2-2*1 != 0
    results.append('01a: controesempi retta affine, quadrante, parabola e unione degli assi')
    # I coefficienti stampati per i due generatori costituiscono l'inversa esatta.
    G=M([[2,1],[-1,3]]); C=M([[F(3,7),F(-1,7)],[F(1,7),F(2,7)]])
    assert P(G,C)==I(2)
    G3=cols([1,1,-1],[2,0,1]); assert P(M([[1,-3,-2]]),G3)==zero(1,2)
    assert rank(join(G3,cols([0,1,0])))==3 and rank(G3)==2
    results.append('01b: formule dei generatori di R² e piano contenente i due generatori di R³')
    G=cols([1,1,1],[2,0,0],[4,0,0]); assert P(G,cols([0,2,-1]))==zero(3,1)
    H=cols([1,2,3],[2,0,0],[3,2,3]); assert P(H,cols([1,1,-1]))==zero(3,1)
    B=cols([1,-1],[2,1]); assert P(B,cols([F(-1,3),F(5,3)]))==cols([3,2])
    assert Inv(B)==M([[F(1,3),F(-2,3)],[F(1,3),F(1,3)]])
    results.append('01c: entrambe le relazioni in R³ e coordinate di (3,2) con formula inversa')
    U=cols([1,2,-2,0],[0,-3,-1,1]); eq=M([[2,-1,0,-3],[2,0,1,1]])
    assert rank(U)==2 and rank(eq)==2 and P(eq,U)==zero(2,2)
    G=cols([1,-1,0,2],[-1,-3,2,0],[2,0,-1,3])
    assert P(G,cols([-3,1,2]))==zero(4,1) and rank(G)==2
    assert rank(cols([1,-1,0,2],[2,0,-1,3]))==2
    W=cols([-2,0,1,0],[-1,1,0,1]); weq=M([[1,0,2,1],[0,1,0,-1]])
    assert rank(W)==2 and P(weq,W)==zero(2,2)
    ceq=M([[1,1,2,0],[0,2,3,1]])
    assert rank(ceq)==2 and P(ceq,G)==zero(2,3)
    results.append('01d–01e: basi, indipendenza e uguaglianza fra descrizioni parametriche e cartesiane in R⁴')
    # Esempio del quoziente: proiezione y; complementari W_m per valori razionali.
    assert P(M([[0,1]]),cols([1,0]))==zero(1,1)
    for m in (F(-2),F(0),F(1),F(3,2)):
        assert rank(cols([1,0],[m,1]))==2
    # Verifica simbolica via coefficienti dell'identità (x,y)=(x-my,0)+y(m,1).
    for m in (F(-2),F(0),F(1),F(3,2)):
        assert P(cols([1,0],[m,1]),M([[1,-m],[0,1]]))==I(2)
    results.append('01f–01h: modelli del prodotto/quoziente e identità della famiglia di complementari')
    U=cols([3,0,1,-2,-2],[1,-2,3,-1,-1]); u3=cols([3,6,-7,-1,-1])
    assert P(U,cols([2,-3]))==u3 and rank(U)==2
    assert P(M([[1]*5]),join(U,u3))==zero(1,3)
    eq=M([[1,-4,-3,0,0],[0,5,4,2,0],[0,0,0,-1,1]])
    assert rank(eq)==3 and P(eq,U)==zero(3,2)
    W=cols([1,0,0,0,-1],[0,1,0,-1,0]); Z=cols([3,0,1,-2,-2],[1,0,0,0,-1],[1,0,0,0,0])
    assert rank(join(U,W))==4 and rank(W)==2 and rank(Z)==3
    assert rank(U)+rank(Z)-rank(join(U,Z))==1
    assert rank(W)+rank(Z)-rank(join(W,Z))==1
    assert rank(P(M([[1]*5]),Z))==1 # Z interseca V in dimensione 2.
    # Tutti i blocchi del metodo che conserva le relazioni.
    original=T(join(U,u3)); aug=join(original,I(3))
    aug[1]=[x-3*y for x,y in zip(aug[0],aug[1])]
    aug[2]=[x-y for x,y in zip(aug[2],aug[0])]
    assert aug==M([[3,0,1,-2,-2,1,0,0],[0,6,-8,1,1,1,-3,0],[0,6,-8,1,1,-1,0,1]])
    aug[2]=[x-y for x,y in zip(aug[2],aug[1])]
    assert aug[2]==M([[0,0,0,0,0,-2,3,1]])[0]
    results.append('01i: relazione, matrici del registro, equazioni, complementare e due intersezioni in R⁵')
    S=M([[1,1,0,0],[0,-1,1,0],[0,0,-1,1],[0,0,0,-1]])
    Sinv=M([[1,1,1,1],[0,-1,-1,-1],[0,0,-1,-1],[0,0,0,-1]])
    E=M([[1,1,1,1],[1,2,4,8]])
    B=cols([2,-3,1,0],[6,-7,0,1])
    assert P(S,Sinv)==I(4) and P(Sinv,S)==I(4)
    assert P(E,S)==M([[1,0,0,0],[1,-1,-2,-4]])
    assert P(E,B)==zero(2,2) and rank(B)==2 and rank(E)==2
    assert P(S,cols([0,2,-1,0]))==cols([2,-3,1,0])
    results.append('01j: entrambe le basi, formule inverse, due equazioni e base del sottospazio di polinomi')
    A=M([[0,1,2],[2,-1,2],[-2,3,5]]); b=cols([1,2,-6])
    assert P(A,cols([F(11,2),5,-2]))==b
    aug=join(A,b); aug[0],aug[1]=aug[1],aug[0]
    aug[2]=[x+y for x,y in zip(aug[2],aug[0])]
    assert aug==M([[2,-1,2,2],[0,1,2,1],[0,2,7,-4]])
    aug[2]=[x-2*y for x,y in zip(aug[2],aug[1])]
    assert aug==M([[2,-1,2,2],[0,1,2,1],[0,0,3,-6]])
    assert rank(M([[1,-1,0,2],[0,-4,2,2]]))==2
    results.append('02a: tutti gli stadi del sistema e della riduzione dei generatori di R⁴')
    A=M([[2,1],[-3,3]]); B=M([[1,4],[2,-1]])
    assert P(A,B)==M([[4,7],[3,-15]]) and P(B,A)==M([[-10,13],[7,-1]])
    rectangular=M([[2,1,3,0],[4,-2,1,3]])
    assert T(rectangular)==M([[2,4],[1,-2],[3,1],[0,3]])
    assert T(P(rectangular,T(rectangular)))==P(rectangular,T(rectangular))
    results.append('02b: due prodotti non commutativi e esempio rettangolare della trasposta')
    # Riduzione del parametro a: ogni entrata è una terna di coefficienti (1,a,a²).
    c=lambda x:(F(x),F(0),F(0)); a=(F(0),F(1),F(0)); a2=(F(0),F(0),F(1))
    sub=lambda x,y:tuple(t-u for t,u in zip(x,y))
    plus=lambda x,y:tuple(t+u for t,u in zip(x,y))
    timesa=lambda x:(F(0),x[0],x[1])
    A=[[c(0),c(1),c(2),c(1),c(0)],[c(1),c(2),c(2),c(1),c(1)],[c(1),c(1),a,c(0),c(1)],[c(0),a,(F(0),F(2),F(0)),a2,c(0)]]
    A[0],A[1]=A[1],A[0]; A[2]=[sub(x,y) for x,y in zip(A[2],A[0])]
    A[2]=[plus(x,y) for x,y in zip(A[2],A[1])]; A[3]=[sub(x,timesa(y)) for x,y in zip(A[3],A[1])]
    assert A==[[c(1),c(2),c(2),c(1),c(1)],[c(0),c(1),c(2),c(1),c(0)],[c(0),c(0),a,c(0),c(0)],[c(0),c(0),c(0),(F(0),F(-1),F(1)),c(0)]]
    for value,expected in [(0,2),(1,3),(2,4),(-1,4),(F(1,2),4)]:
        assert rank([[sum(coef*(value**i) for i,coef in enumerate(entry)) for entry in row] for row in A])==expected
    A=M([[1,2],[2,4]]); assert rank(A)==rank(join(A,cols([3,6])))==1
    assert rank(join(A,cols([3,7])))==2
    assert len(kernel(A)[0])==1
    results.append('02c: riduzione polinomiale simbolica per ogni a e casi 0/1/generico; sistemi compatibile/incompatibile')
    # Eccezione sul campo a due elementi.
    for v in (0,1):
        for w in (0,1):
            for a in (0,1):
                for b in (0,1): assert ((a*v+b*w)%2)**2%2==(a*v*v+b*w*w)%2
    S=M([[3,F(7,10)],[0,F(13,10)]]); Pi=P(S,P(M([[1,0],[0,0]]),Inv(S))); Sig=P(S,P(M([[1,0],[0,-1]]),Inv(S)))
    assert P(Pi,Pi)==Pi and P(Sig,Sig)==I(2) and add(I(2),Sig)==scale(Pi,2)
    assert [F(37,10),F(13,10)]==[F(3)+F(7,10),F(13,10)]
    assert [F(23,10),F(-13,10)]==[F(3)-F(7,10),-F(13,10)]
    results.append('03a–03b: eccezione F₂ e proiezione/simmetria oblique con identità dei disegni')
    B=M([[1,2],[1,-1]]); C=M([[-3,2],[1,0]]); Fm=M([[2,-1],[1,3]])
    A=M([[4,-1],[F(13,2),1]])
    assert P(Inv(C),P(Fm,B))==A and P(C,A)==M([[1,5],[4,-1]])
    Bp=M([[1,1],[1,-1]]); Cp=M([[1,0],[2,1]])
    Pc=P(Inv(Bp),B); Qc=P(Inv(Cp),C)
    assert P(Qc,P(A,Inv(Pc)))==P(Inv(Cp),P(Fm,Bp))
    assert [F(18,5)-F(3,5),F(6,5)+F(4,5)]==[3,2] # Somma delle componenti nel cambio di basi.
    results.append('03c–03d: matrice nelle due basi e formula completa del cambio di basi indipendente dal calcolo precedente')
    # Annullatori e matrice della trasposta in basi non canoniche.
    U=cols([1,2,0,1],[0,1,1,-1]); N=kernel(T(U))
    assert rank(U)==2 and rank(N)==2 and P(T(N),U)==zero(2,2)
    double=kernel(T(N)); assert rank(double)==2 and rank(join(U,double))==2
    Fm=M([[1,2],[0,3],[-1,1]]); B=M([[1,2],[1,-1]]); C=M([[1,1,0],[0,1,1],[1,0,1]])
    A=P(Inv(C),P(Fm,B))
    dual_matrix=P(T(B),P(T(Fm),T(Inv(C))))
    assert dual_matrix==T(A)
    results.append('04: doppio annullatore in R⁴ e matrice della trasposta in basi duali non canoniche')
    checks_19_21()
    report={'data':'2026-11-12','ambito':'calcoli e diagrammi della dispensa corrente; le prove generali sono state rilette separatamente','controlli':results,'controlli_19_21':'CONTROLLI_LEZIONI_19-21_2026-11-12.json','esito':'tutti superati'}
    out=Path(__file__).resolve().parents[1]/'CONTROLLI_REVISIONE_TOTALE_2026-11-12.json';out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print('\n'.join(results))

if __name__=='__main__': main()
