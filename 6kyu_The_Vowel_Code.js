/*
Step 1: Create a function called encode() to replace all the lowercase vowels in a given string with numbers according to the following pattern:

a -> 1
e -> 2
i -> 3
o -> 4
u -> 5

For example, encode("hello") would return "h2ll4". There is no need to worry about uppercase vowels in this kata.

Step 2: Now create a function called decode() to turn the numbers back into vowels according to the same pattern shown above.

For example, decode("h3 th2r2") would return "hi there".

For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels.

*/

function encode(string) {
  let arr = [];
  for(let i = 0; i < string.length; i++){
    if(string.charAt(i) == 'a'){
     arr.push(1);
    }
    else if(string.charAt(i) == 'e'){
     arr.push(2);
    }
    else if(string.charAt(i) == 'i'){
     arr.push(3);
    }
    else if(string.charAt(i) == 'o'){
     arr.push(4);
    }
    else if(string.charAt(i) == 'u'){
     arr.push(5);
    }
    else {
      arr.push(string[i])
    }
  }
  return arr.join('');
}

function decode(string) {
  let arr = [];
  for(let i = 0; i < string.length; i++){
    if(string.charAt(i) == '1'){
     arr.push('a');
    }
    else if(string.charAt(i) == '2'){
     arr.push('e');
    }
    else if(string.charAt(i) == '3'){
     arr.push('i');
    }
    else if(string.charAt(i) == '4'){
     arr.push('o');
    }
    else if(string.charAt(i) == '5'){
     arr.push('u');
    }
    else {
      arr.push(string[i])
    }
  }
  return arr.join('');
}
