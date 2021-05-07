/*
    Get product of all other elements
    Given an array of integers, return a new array such that each element at index i of
    the new array is the product of all the numbers in the original array except the one
    at i.

    For example:

    input:  [1, 2, 3, 4, 5, 6]
    output: [120,60,40,30,24]

    input:  [3, 2, 1]
    output: [2, 3, 6 ]

    Follow up: What if you can't use division?

*/

/* Brute force solution and avoiding the division restriction.
function obtainProductOfAllElements(elementsArray){
    let totalizer   = 1;
    let products    = [];
    
    for (let index = 0; index < elementsArray.length; index++){
        totalizer = totalizer * elementsArray[index]; 
    } // o(n)
    
    for (let index=0; index < elementsArray.length; index++){
        products.push(totalizer/elementsArray[index]);
    } // o(n)
    
    return products;
}
*/


function obtainProductOfAllElementsEnhanced(numbers){
    let prefix  = [];
    let suffix  = [];
    let product = [];

    let originalNumbers = numbers.slice();
    let reversedNumbers = numbers.slice().reverse();
    
    
    for (let index=0; index < originalNumbers.length; index++){
        if (prefix.length == 0 ){
            prefix.push(originalNumbers[index]);
        }else{
            prefix.push(prefix[index-1]*originalNumbers[index]);
        }
    }   // O(n)

    for (let index=0; index < reversedNumbers.length; index++){
        if (suffix.length == 0 ){
            suffix.push(reversedNumbers[index]);
        }else{
            suffix.push(suffix[index-1]*reversedNumbers[index]);
        }
    }   // O(n)
    suffix.reverse()

    for (let pivot=0; pivot < originalNumbers.length; pivot++){
        let value = 0;
        if(pivot == 0 ){
            value = suffix[pivot+1]
        }
        else if(pivot == originalNumbers.length-1){
            value = prefix[pivot-1]
        }
        else{
            value = prefix[pivot-1] * suffix[pivot+1]
        }
        product.push(value);
    }  // O(n)

  return product;
}

const argsArray = [1,2,3,4,5];
let outputArray = obtainProductOfAllElementsEnhanced(argsArray);
console.log(outputArray);
