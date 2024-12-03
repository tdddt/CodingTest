package java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

// 모든 정점에서 다른 모든 정점으로의 최단 거리
public class Floyd {
    public static final int INF = (int)1e9;
    public static int n,m;
    public static int[][] graph = new int[501][501];

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        // 테이블 INF로 초기화
        for (int i=0;i<501;i++){
            Arrays.fill(graph[i],INF);
        }

        // 자기 자신은 0으로 초기화
        for (int a=1;a<=n;a++){
            for (int b=1;b<=n;b++){
                if(a==b) graph[a][b]=0;
            }
        }

        // 간선 입력
        for (int i=0;i<m;i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            graph[a][b] = c;
        }

        // 플로이드-워셜
        for(int k=1;k<=n;k++){
            for(int a=1;a<=n;a++){
                for (int b=1;b<=n;b++){
                    graph[a][b] = Math.min(graph[a][b],graph[a][k]+graph[k][b]);
                }
            }
        }
    }
}
