/*
question:
Let's have a string: abbbcacbcdce

For substring abbb, you have most frequent letter b -> 3 and least frequent letter a -> 1.
So the deviation is = most frequent - least frequent = 3 - 1 = 2. You need to look at all the substrings and find the max deviation.

Here substring cacbcdc has the max deviation.
Frequency is like below:
c -> 4, a ->1, b->1, d->1.
So max freq - min freq = 4 - 1 = 3.

Among all substrings deviation, this is the max. So need to return it.

String length is 10^4. So you can't check each substring.




Idea
We take all possible distinct as ( c1 & c2 pairs ) characters possible. eg. 'a' & 'b' , 'a' & 'c' ... 'z' & 'z'
We consider c1 as the character with maximum Freq and c2 as the character with minimum Freq
Then we construct array of only c1 and c2 from the string( coz we are only interested in max and min Freq characters).
We take 1 for c1 and -1 for c2.
Further if we have consecutive c1's we simply add their frequency.
eg. ababcccaac
c1 = 'c' and c2 = 'a'
the array formed is -1 -1 3 -1 -1 1
Now the deviation will be the length of maximum sum of subarray in the generate array.
Note : that the size of subarray should be greater than 1.
Why? In above example max subarray sum is 3( of length 1 ) but this is not correct as all characters will be same( result should be 0)
So consider subarray of size>1.




*/


#include<bits/stdc++.h>
using namespace std;

int modifiedKadane( vector<int> &arr , int k ){
    if( arr.size() < k )
        return 0;
    
    int n = arr.size();
    vector<int> maxSum(n);

    // use kadane's
    maxSum[0] = arr[0];
    for (int i = 1 ; i < arr.size(); i++) {
      maxSum[i] = max(arr[i], maxSum[i - 1] + arr[i]);
    }

    int sum = 0 ;
    for (int i = 0 ; i < k; i++) {
      sum += arr[i];
    }

    int ans = sum;
    for (int i = k ; i < arr.size(); i++) {
      sum = sum + arr[i] - arr[i - k];
      ans = max(ans, sum);
      ans = max(ans, sum + maxSum[i - k]);
    }

    return ans;
}

int maxDeviation( string str ){
    int ans = 0 ;

    for( char c1 = 'a' ; c1<='z' ; c1++ ){
        for( char c2 = 'a' ; c2<='z' ; c2++ ){
            if ( c1 == c2 )
                continue;

            vector<int> arr;
            // we consider c1 as character with maxFreq and c2 with minFreq
            for( auto c : str ){
                if( c==c1 ){
                    // We shall include all consecutive c1's in our array so we add their frequency
                    if( arr.size() && arr.back() != -1 ){
                        arr.back() += 1;
                    }
                    else{
                        arr.push_back( 1 );
                    }
                }
                else if( c==c2 ){
                    // we take distinct c2
                    arr.push_back( -1 );
                }
            }
            ans= max( ans , modifiedKadane(arr, 2) );
        }
    }
    return ans;
}
int main(){
    // string str = "abacccabab";
    string str = "baaa";
    
    cout<<maxDeviation(str)<<"\n";
    return 0;
}