# Questions

### 1: Write a function where :

class Solution { public int solution(int[] A); }

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].



### 2: Write a function where:
    Determines the maximal 'binary gap' in an integer
    :param N: a positive integer (between 1 and maxint or 2million odd)
    :return: a count of the longest sequence of zeros in the binary representation of the integer

    Example:
        Input: 3795
        Output: 2
        Explanation: 
            Binary of 3795 is 111011010011. The longest gap is 2 because maximum number of consecutive 0's is 2.
