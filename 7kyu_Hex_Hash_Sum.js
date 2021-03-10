/*
Complete the function that accepts a valid string and returns an integer.

Wait, that would be too easy! Every character of the string should be converted to the hex value of its ascii code, then the result should be the sum of the numbers in the hex strings (ignore letters).
Examples

"Yo" ==> "59 6f" ==> 5 + 9 + 6 = 20
"Hello, World!"  ==> 91
"Forty4Three"    ==> 113
*/

function hexHash(code){
  try {
    let arr1 = [];
    let sum = 0;
    for (var i = 0; i < code.length; i++) {
      var hex = Number(code.charCodeAt(i)).toString(16);
      arr1.push(hex);
    }
  
    let str = arr1.join('').match(/\d/g);
    for (let i = 0; i < str.length; i++){
      sum += Number(str[i]);
    }
    return sum; 
  } 
  catch (err){
    return 0;
  }

}
