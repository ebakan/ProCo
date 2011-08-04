#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <string>

using namespace std;
int main() {
    int maxA, maxB;
    cin >> maxA >> maxB;
    int* a = new int[maxA];
    int* b = new int[maxB];
    int* out = new int[maxA+maxB];
    int currA=0,currB=0,currO=0;
    for(int i=0;i<maxA;i++)
	cin >> a[i];
    for(int i=0;i<maxB;i++)
	cin >> b[i];
    while(currA!=maxA || currB!=maxB) {
	if(currA==maxA) {
	    out[currO++]=b[currB++];
	}
	else if(currB==maxB) {
	    out[currO++]=a[currA++];
	}
	else {
	    if(a[currA]<b[currB])
		out[currO++]=a[currA++];
	    else
		out[currO++]=b[currB++];
	}
    }
    cout << out[0];
    for(int i=1;i<maxA+maxB;i++)
	cout << " " << out[i];
    cout << endl << flush;
    return 0;
}
