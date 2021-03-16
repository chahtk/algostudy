#import<iostream>

int m,n;
int add[1400]={0};
int dp[700][700]={0};
int main()
{
    scanf("%d %d",&m,&n);
    for(int t=0;t<n;t++)
    {
        int a,b,c;
        scanf("%d %d %d",&a,&b,&c);
        for(int i=a;i<a+b;i++)
        {
            add[i]+=1;
        }
        for(int i=a+b;i<a+b+c;i++)
        {
            add[i]+=2;
        }
    }
    for(int i=0;i<m;i++)
    {
        dp[0][m-1-i]=add[i]+1;
    }
    for(int i=1;i<m;i++)
    {
        dp[i][0]=add[m-1+i]+1;
    }
    for(int i=1;i<m;i++)
    {
        for(int j=1;j<m;j++)
        {
            if(dp[i][j]<dp[i-1][j-1])
            {
                dp[i][j]=dp[i-1][j-1];
            }
            if(dp[i][j]<dp[i][j-1])
            {
                dp[i][j]=dp[i][j-1];
            }
            if(dp[i][j]<dp[i-1][j])
            {
                dp[i][j]=dp[i-1][j];
            }
        }
    }
    for(int i=0;i<m;i++)
    {
        for(int j=0;j<m;j++)
        {
            printf("%d ",dp[j][i]);
        }
        printf("\n");
    }
}