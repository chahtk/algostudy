#include <cstdio>


using namespace std;

int main()
{
    long long n,m;
    long long get_num;
    scanf("%lld %lld",&n,&m);
    long long ans=1;
    for(int i=0;i<n;i++)
    {
        scanf("%lld",&get_num);
        if(get_num==0)
        {
            get_num=1;
        }
        ans*=get_num;
        ans%=m;

    }
    printf("%lld",ans%m);
    return 0;
}