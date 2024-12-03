package java;

import java.util.*;

public class Stack1 {
    public static void main(String[] args){
        Stack<Integer> s = new Stack<>();

        s.push(1);
        s.push(2);
        s.push(3);
        s.pop();
        s.push(4);
        s.push(5);
        s.pop();

        while(!s.isEmpty()){
            System.out.println(s.peek()); // 가리키기
            s.pop(); //없애기
        }
    }
}
