package java;

import java.io.BufferedReader;
import java.util.*;
import java.io.*;

class Node implements Comparable<Node>{
    private int index;
    private int distance;

    public Node(int index, int distance){
        this.index = index;
        this.distance = distance;
    }

    public int getIndex(){
        return this.index;
    }

    public int getDist(){
        return this.distance;
    }

    // 거리가 짧은 게 높은 우선순위를 가지도록 설정
    @Override
    public int compareTo(Node other){
        if(this.distance < other.distance){
            return -1;
        }
        return 1;
    }
}

// 한 정점에서 다른 모든 정점으로의 최단 거리
public class Dijkstra {
    public static final int INF = (int)1e9;
    public static int n,m,start; // 노드,간선,목표 정점
    public static ArrayList<ArrayList<Node>> graph = new ArrayList<ArrayList<Node>>();
    public static int[] d = new int[100001]; // 최단 거리 테이블

    public static void dijkstra(int start){
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(start,0));
        d[start] = 0;

        while(!pq.isEmpty()){
            Node node = pq.poll();
            int dist = node.getDist();
            int now = node.getIndex();
            if(d[now]<dist) continue; // 이미 처리된 노드라면 무시
            // 인접 노드 확인
            for(int i=0;i<graph.get(now).size();i++){
                int cost = d[now]+graph.get(now).get(i).getDist();
                // 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                if (cost < d[graph.get(now).get(i).getIndex()]) {
                    d[graph.get(now).get(i).getIndex()] = cost;
                    pq.offer(new Node(graph.get(now).get(i).getIndex(), cost));
                }
            }

        }
    }

    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");
        start = Integer.parseInt(temp[0]);
        n = Integer.parseInt(temp[1]);
        m = Integer.parseInt(temp[2]);

        // 그래프 초기화
        for (int i=0;i<=n;i++){
            graph.add(new ArrayList<Node>());
        }

        // 최단거리 테이블 초기화
        Arrays.fill(d,INF);

        // 간선 입력
        for (int i=0;i<m;i++){
            String[] mm = br.readLine().split(" ");
            int a = Integer.parseInt(mm[0]);
            int b = Integer.parseInt(mm[1]);
            int c = Integer.parseInt(mm[2]);
            graph.get(a).add(new Node(b,c));
        }

        dijkstra(start);
    }
}
