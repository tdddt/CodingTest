package java;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
// 1. 방문 시작 원소 삽입, 방문처리
// 2. 연결된 모든 원소 삽입
// 3. q가 빌 때까지 반복
public class BFS {
    public static boolean[] visited = new boolean[9];
    public static ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>();

    public static void bfs(int n){
        // 시작 노드
        Queue<Integer> q = new LinkedList<>();
        q.offer(n);
        visited[n]=true;

        while(!q.isEmpty()){
            int now = q.poll();
            for (int nn :graph.get(now)){
                if(!visited[nn]) {
                    visited[nn] = true;
                    q.offer(nn);
                }
            }
        }
    }
    public static void main(String[] args){
        //그래프 초기화
        for (int i=0;i<9;i++){
            graph.add(new ArrayList<Integer>());
        }

        // 노드 1에 연결된 노드
        graph.get(1).add(2);
        graph.get(1).add(3);
        graph.get(1).add(8);

        // 노드 2에 연결된 노드
        graph.get(2).add(1);
        graph.get(2).add(7);

        // 노드 3에 연결된 노드
        graph.get(3).add(1);
        graph.get(3).add(4);
        graph.get(3).add(5);
        
        // 노드 4에 연결된 노드
        graph.get(4).add(3);
        graph.get(4).add(5);
        
        // 노드 5에 연결된 노드
        graph.get(5).add(3);
        graph.get(5).add(4);
        
        // 노드 6에 연결된 노드
        graph.get(6).add(7);
        
        // 노드 7에 연결된 노드
        graph.get(7).add(2);
        graph.get(7).add(6);
        graph.get(7).add(8);
        
        // 노드 8에 연결된 노드
        graph.get(8).add(1);
        graph.get(8).add(7);

        bfs(1);
    }
}
