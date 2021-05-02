class Solution {
    public int subarraysDivByK(int[] A, int K) {
        int[] arr = new int[K];
        arr[0] = 1;
        int sum = 0;
        int result = 0;
        for (int n : A) {
            sum = (sum + n) % K;
            if (sum < 0) sum = sum += K;
            result += arr[sum];
            arr[sum]++;
        }
        
        return result;        
    }
}