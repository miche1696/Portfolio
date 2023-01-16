def rec(int vs, int vd, str temp, str& solution):
    if(!vs and !vd):
        solution.append(temp)
        return
    if(vs):
        temp+="("
        rec(vs-1, vd, temp, solution)
        temp=temp[0:-1]
    if(vd>vs)

if __name__=="__main__":
    n=3
    vs=n-1
    vd=n
    solution = []
    temp = "("
    while(vs and vd):
        if(vs):
            
        else if(vd):



#sol@¹
genero brute force tutte le combinazioni di parentesi e poi alla fine valido + aggiungo al vettore soluzioni
#sol@²
sol¹ ma ottimizzata con prima parentesi