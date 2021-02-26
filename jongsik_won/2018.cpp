#include <cstdio>

int main()
{
    int n;
    scanf("%d",&n);
    int ans=0;
    for(int i=1;i<n;i++)
    {
        if(i%2==0)
        {
            if(n%i==i/2)
            {
                if(n/i>=i/2)
                {
                    ans++;
                }
            }
        }
        else{
            if(n%i==0)
            {
                if(n/i>i/2)
                {

                    ans++;
                }
            }
        }
    }
    if(n==1)
    {
        printf("1");
        return 0;
    }
    printf("%d",ans);
    return 0;
}