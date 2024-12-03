package java;

// 피보나치 수열
public class Dp {

    public static long[] dp = new long[100];

    public static long topBottom(int x){
        // 종료 조건
        if(x==1 || x==2) return 1;
        // 이미 계산한 적이 있으면 그대로 반환
        if(dp[x]!=0) return dp[x];
        // 접화식으로 계산
        dp[x]=topBottom(x-1)+topBottom(x-2);
        return dp[x];
    }

    // bottomTop
    public static void main(String[] args){
        dp[1]=1;
        dp[2]=1;
        
        int x = 50;

        for(int i=3;i<=x;i++){
            dp[i]=dp[i-1]+dp[i-2];
        }
        System.out.println(dp[x]);

    }
}
