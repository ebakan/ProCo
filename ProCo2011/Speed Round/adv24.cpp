#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <string>

using namespace std;
int main() {
    int numVals;
    cin >> numVals;
    char* val = new char[numVals+1];
    cin >> val;
    for(int i=0;i<numVals;i++)
	cout << val[((int)val[i])-48];
    cout << endl << flush;

    return 0;
}
