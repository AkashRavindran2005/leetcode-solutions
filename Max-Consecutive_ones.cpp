// Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

// Example 1:

// Input: nums = [1,1,0,1,1,1]
// Output: 3
// Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
// Example 2:

// Input: nums = [1,0,1,1,0,1]
// Output: 2

// Solution

class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int ind1 = 0;
        vector<int> count;
        for(int i = 0; i<nums.size(); i++){
            if (nums[i] == 1){
                ind1 += 1;
            }
            if (nums[i] == 0 || i == nums.size()-1){
                count.push_back(ind1);
                ind1 = 0;
            }
        }
        return *max_element(count.begin(), count.end());
    }
};