#Sin resolver :c
for i in range(int(input())):
    vector = [0.00 for i in range(5)]
    length = 0
    for j in input():
        length+=1
        if j=='a':vector[0]+=1
        elif j=='e':vector[1]+=1
        elif j=='i':vector[2]+=1
        elif j=='o':vector[3]+=1
        elif j=='u':vector[4]+=1
    print(f"Caso {i+1}:\na= {round((vector[0]/length*100),2):.2f}\ne= {round((vector[1]/length*100),2):.2f}\ni= {round((vector[2]/length*100),2):.2f}\no= {round((vector[3]/length*100),2):.2f}\nu= {round((vector[4]/length*100),2):.2f}")