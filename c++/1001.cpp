#ifdef __MSDOS__
    #include <iostream.h>
    #include <stdlib.h>
#else
    #include <iostream>
    #include <cstdlib>
    using namespace std;
#endif

int main (void)
{
    float a, b, suma;
    cout << "Ingresa el valor de a: ";
    cin >> a;
    cin.get();
    cout << "Ingresa el valor de b: ";
    cin >> b;
    cin.get();
    suma=a+b;
    cout << "Valor de suma: " << suma << endl;
    cout << endl;
    system ("pause");
    return EXIT_SUCCESS;
}