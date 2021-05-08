/*
    Given an array of integer that are out of order, determine the bounds of the smallest
    window that must be sorted in order for the entire array to be sorted. 
    
    For example:

    input: [3, 7, 5, 6, 9];
    output: (1, 3)
*/

/* Brute force solution and avoiding the performance restrictions
function findSmallestWindowToBeSorted(numbers){
    let sortedNumbers    = numbers.slice().sort(); // O(n*log(n))
    
    let right    = undefined;
    let left     = undefined;
    
    for(let index=0; index<numbers.length; index++){ //
       let valueAtSorted    = sortedNumbers[index]
       let valueAtNonSorted = numbers[index]
       
       if(valueAtSorted !== valueAtNonSorted && left == undefined){
           left = index;
       }else if(valueAtSorted !== valueAtNonSorted){
           right = index;
       }   
    }
   return [left,right];
}
*/

function findSmallesWindowToBeSortedEnhanced(numbers){
    let right       = undefined;
    let max_seen    = -Infinity;
    
    let left        = undefined;
    let min_seen    = Infinity;

    for(let index=0; index<numbers.length; index++){
        let currentValue = numbers[index];
        max_seen = Math.max(max_seen, currentValue);
        if(currentValue<max_seen){
            right = index;
        }
    }

    for(let index=numbers.length-1;index>0;index--){
        let currentValue = numbers[index];
        min_seen = Math.min(min_seen,currentValue)
        if(currentValue>min_seen){
            left=index
        }
    }
return [left,right]
}

const arr = [3, 7, 5, 6, 9];
let output = findSmallesWindowToBeSortedEnhanced(arr);
console.log(output);