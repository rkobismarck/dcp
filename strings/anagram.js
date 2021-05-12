


/*
    Given a word w and a string s, find all indices in s 
    which are the starting locationsof anagrams of w. 
    For example, given w is ab and s is abxaba return [0, 3, 4]
*/



function delIfZero(dict,char){
    if(dict[char] == 0){
        delete dict[char]
    }
    return dict
}
    

function anagramIndices(word,s){
    results = []
    freq = {}

    for( index=0; index<word.length; index++){  
        currentValue = word[index]
        freq[currentValue] = freq[currentValue] == undefined ? 1: freq[currentValue]+1
    }  
    
    freq_mutable = Object.assign({}, freq); 
    for ( i = 0; i< s.length; i++){
        currentValue = s[i]
        if(freq[currentValue]  && freq_mutable[currentValue]){
            freq_mutable[currentValue] = freq_mutable[currentValue] - 1
            delIfZero(freq_mutable,currentValue)
            if(Object.keys(freq_mutable) == 0 ){
                freq_mutable = Object.assign({}, freq);
                freq_mutable[currentValue] = freq_mutable[currentValue] - 1
                delIfZero(freq_mutable,currentValue) 
                results.push(i - word.length + 1)
            }
        }
        else{
            freq_mutable = Object.assign({}, freq);
            if(freq_mutable[currentValue]){
                freq_mutable[currentValue] = freq_mutable[currentValue] - 1
                delIfZero(freq_mutable,currentValue)
            }
        }
       
    }
    return results;
}


const word      = 'ab'
const string    = 'abxaba'
let output      = anagramIndices(word,string);
console.log(output);