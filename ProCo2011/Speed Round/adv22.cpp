#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <string>

using namespace std;
bool sameVal(int* vals, int numVals) {
    int start=vals[0];
    for(int i=1;i<numVals;i++) {
	if(vals[i]!=start)
	    return false;
    }
    return true;
}

int main() {
    int numVals;
    cin >> numVals;
    int* vals = new int[numVals];
    for(int i=0;i<numVals;i++)
	cin >> vals[i];
    while(!sameVal(vals,numVals)) {
	int* newVals = new int[numVals-1];
	for(int i=0;i<numVals-1;i++) {
	    newVals[i]=vals[i+1]-vals[i];
	}
	delete vals;
	vals=newVals;
	numVals--;
    }

    cout << vals[0] << endl << flush;

    return 0;
}
