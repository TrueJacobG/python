#include <iostream>

using namespace std;

int n;
int p, v, t;
int flag=0;

int main()
{
		cin >> n;
		
		while(n){
			cin>>p>>v>>t;
			if(p + v + t >= 2){
					flag++;
			}
		n--;	
		}
		cout<<flag;
}

