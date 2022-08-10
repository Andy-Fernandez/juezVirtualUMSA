//El problema no se pudo resolver pero esto es lo que se tiene
#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin>>n;
    
    for(int i=0; i<n; i++){
        
        string cadena;
        cin>>cadena;
        
        int
        con = 0;
        
        float v[5];
        for(int j =0; j < 5; j++){
            v[j]=0;
        }
        for(char x: cadena){
            con++;
            
            switch(x) 
            {
                case 'a': 
                v[0]++;
                break;
                case 'e':
                v[1]++;
                break;
                case 'i': 
                v[2]++;
                break;
                case 'o': 
                v[3]++;
                break;
                case 'u': 
                v[4]++;
                break; 
            }
        }
        cout<<"Caso "<<(i+1)<<":\n";
            printf("a= %.2f\n",((v[0]/con)*100));
            printf("e= %.2f\n",((v[1]/con)*100));
            printf("i= %.2f\n",((v[2]/con)*100));
            printf("o= %.2f\n",((v[3]/con)*100));
            printf("u= %.2f\n",((v[4]/con)*100));
    }
    return 0;
}