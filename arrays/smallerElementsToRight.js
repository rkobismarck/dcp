/*
    Given an array of integers, return a new array where each element in the new array
    is the number of smaller elements to the right of that element in the original input
    array.

    For example, given the array [3, 4, 9, 6, 1] it will return [1, 1, 2, 1, 0].
*/ 

// Is it possible to improve this O(n2) solution?
function smallerElementsToRight(numbers){
    let output          = []
    for(outerIndex=0; outerIndex<numbers.length; outerIndex++){
        currentOuter    = numbers[outerIndex];
        summarizer      = 0;  
        for(innerIndex=outerIndex+1; innerIndex<numbers.length; innerIndex++){
            currentIner = numbers[innerIndex];
            if(currentOuter>currentIner){
                summarizer = summarizer + 1;
            }
        }
        output.push(summarizer)
    }
    return output;
};

const arr = [3,4,9,6,1];
let output = smallerElementsToRight(arr);
console.log(output);
