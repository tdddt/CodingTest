package java;

import java.util.*;

public class Queue1 {
    public static void main(String[] args){
        Queue<Integer> q = new LinkedList<>();
        q.offer(5); // add도 사용 가능. but 큐의 용량이 가득 찼을 때, add는 IllegalStateException, offer는 false발생
        q.offer(6);
        q.offer(7);
        q.poll(); // pop사용불가
        q.offer(8);
        q.poll();
        while(!q.isEmpty()){
            System.out.println(q.poll());
        }
    }
}
