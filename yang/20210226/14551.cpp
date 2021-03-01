#include<iostream>
using namespace std;
int main(){
    int N;
    int M;
    int A;
    int Q=1;
    int W;
    cin>>N>>M;

    int k[N-1];


    for(int i=0;i<N;i++)
    {
        cin>>k[i];
    }

    for(int i=0;i<N;i++)
    {
        if(k[i]==0)
        {
            k[i]=1;
        }
        Q=k[i]*Q%M;
    }

    cout<<Q;
}