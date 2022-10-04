if __name__ == "__main__":
    segundos = 0  
    minutos = 0 
    horas = 0  

    for h in range(24): 
        for m in range(60): 
            for s in range(60): 
                print(f"{h}:{m}:{s}")