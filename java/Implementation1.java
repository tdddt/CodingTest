package java;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
//import java.util.StringTokenizer;

public class Implementation1 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String[] plans = br.readLine().split(" ");
        // StringTokenizer st = new StringTokenizer(br.readLine());

        int x=1;
        int y=1;

        // LRUD
        int[] dx={0,0,-1,1};
        int[] dy={-1,1,0,0};
        char[] move = {'L','R','U','D'};

        // 이동 계획 확인
        for (int i=0; i<plans.length; i++){
            char plan = plans[i].charAt(0);

            // 이동 후 좌표
            int nx=-1;
            int ny=-1;
            for (int j=0;i<4;j++){
                if(plan==move[j]){
                    nx=x+dx[i];
                    ny=y+dy[i];
                }
            }

            // 공간을 벗어나는 겨우 무시
            if(nx<1 || ny<1 || nx>N || ny>N) continue;

            // 이동
            x=nx;
            y=ny;
        }

        System.out.println(x+" "+y);
    }    
}
