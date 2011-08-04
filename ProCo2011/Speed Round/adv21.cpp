#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <string>

using namespace std;
int numTimes(char* s1, char c) {
    int times=0;
    char* s=s1;
    while(*s!='\00') {
	if(*s==c)
	    times++;
	s++;
    }
    return times;

}
int main() {
    char s1[20000];
    char s2[20000];
    cin.getline(s1,20000);
    cin.getline(s2,20000);

    char* s=s1;
    while(*s!='\00') {
	if(*s==' ') {
	    s++;
	    continue;
	}
	if(numTimes(s1,*s)!=numTimes(s2,*s)) {
	    cout << "NO" << endl << flush;
	    return 0;
	}
	s++;
    }

    cout << "YES" << endl << flush;
    return 0;
}

