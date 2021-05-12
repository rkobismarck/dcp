/*
    Given an array, find the maximum sum any contiguous subarray of
    the array. For example, given the array [34, -50, 42, 14, -5, 86],
    the maximum sum would be 137, since we would take the elements 
    42, 14, -5, 86. Given the array [-5, -1, -8, -9], the maximum sum
    would be 0, since we would choose nor to take any elements.

    Do this in O(n) time.

*/


//[34,-2,-1,56,51,136]
function calculateMaxiumSubarraySum(numbers){
    let max_seen = 0;
    for(let index = 0; index<numbers.length; index++){
        let currentValue    = numbers[index];
        let prev_max_seen   = max_seen;
        
        max_seen = max_seen + currentValue;
        if(currentValue<0){
            if(Math.abs(currentValue)>=prev_max_seen){
                max_seen=0;
            }
        }
    }
    return max_seen;
}

const arr = [34, -50, -1, 150, -15, -15, -10, 86];
let output = calculateMaxiumSubarraySum(arr);
console.log(output);