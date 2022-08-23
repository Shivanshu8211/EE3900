#include <stdio.h>
int main(){
    FILE* fp;
    int x[] = {1,2,3,4,2,1};
    int k = 15;
    float y[15];
    for(int i = 0; i<15; i++){
        y[i] = 0;
    }
    y[0] = x[0];
    y[1] = -0.5*y[0]+x[1];

    for(int n = 2; n<k-1; n++){
	if (n < 6){
		y[n] = -0.5*y[n-1]+x[n]+x[n-2];}
	else if (n > 5 && n < 8){
		y[n] = -0.5*y[n-1]+x[n-2];}
	else{
		y[n] = -0.5*y[n-1];}
    }
    
    fp = fopen("xnyn.dat","w");
    for(int i=0;i<15;i++){
        fprintf(fp,"%f\n",y[i]);
    }
    fclose(fp);
}