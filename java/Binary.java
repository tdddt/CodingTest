package java;

// 이진탐색
public class Binary {

    // 재귀
    public static int binaryIter(int[] arr, int target, int start, int end){
        if (start>end) return -1;
        int mid = (start+end)/2;
        if(mid==target) return mid;
        else if (mid>target) return binaryIter(arr,target,start,mid-1);
        else return binaryIter(arr,target,mid+1,end);
    }

    // 순차
    public static int binaryRecur(int[] arr, int target, int start, int end){
        while(start<=end){
            int mid = (start+end)/2;
            if(mid==target) return mid;
            else if(mid>target) end=mid-1;
            else start=mid+1;
        }
        return -1;
    }


    public static void main(String[] args){

    }
    
}
