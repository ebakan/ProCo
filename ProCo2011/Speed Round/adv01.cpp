#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>

using namespace std;
int main() {

    int h,l,r;
    char userChoice;

    cin >> h >> l >> r;

    while(l<7 && r<7 && h<7) {
	if(l>=r) {
	    cout << "L" << endl << flush;
	    l+=h;
	}
	else  {
	    cout << "R" << endl << flush;
	    r+=h;
	}
	if(!(l<7 && r<7 && h<7)) {
	    break;
	}

	cin >> userChoice;

	if(userChoice=='L') {
	    h+=l;
	}
	else if(userChoice=='R') {
	    h+=r;
	}
	else
	    return 1;
    }
    if(l>=7)
	cout << "L Win" << endl << flush;
    else if(r>=7)
	cout << "R Win" << endl << flush;
    else 
	cout << "Lose" << endl << flush;

    return 0;
}
