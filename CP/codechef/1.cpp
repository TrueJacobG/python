#include <iostream>
#include <iomanip>

using namespace std;

int x;
float y;

int main()
{
		cin >> x >> y;
		
		if(x < y && x % 5 == 0){
			cout<<fixed<<setprecision(2)<<y-x-0.50;
		}else{
			cout<<fixed<<setprecision(2)<<y;
		}
		
		return 0;
}	
