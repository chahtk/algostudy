#include <cstdio>

int len[100000];
int cost[100000];

int main()
{
    int ans=0;
    int count=0;
    scanf("%d",&count);
    for(int i=0;i<count-1;i++)
    {
        scanf("%d",&len[i]);
    }
    for(int i=0;i<count;i++)
    {
        scanf("%d",&cost[i]);
    }
    ans=cost[0]*len[0];
    for(int i=1;i<count-1;i++)
    {
        if(cost[i-1]<cost[i])
        {
            cost[i]=cost[i-1];
        }
        ans+=cost[i]*len[i];
    }
    printf("%d",ans);
}