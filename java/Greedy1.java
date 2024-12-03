package java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Greedy1 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] coins = new int[4];
        for (int i=0;i<4;i++){
            coins[i] = Integer.parseInt(st.nextToken());
        }

        int cnt = 0;
        for (int i=0;i<4;i++){
            int coin = coins[i];
            cnt += N/coin;
            N %= coin;
        }

        System.out.println(cnt);
    }
}
