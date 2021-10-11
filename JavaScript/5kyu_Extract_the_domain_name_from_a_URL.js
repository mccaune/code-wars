/*
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"

domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"

domainName("http://github.com/carbonfive/raygun") == "github" 
domainName("http://www.zombie-bites.com") == "zombie-bites"
domainName("https://www.cnet.com") == "cnet"
*/

function domainName(url){
  
  if (url.startsWith('http://www.') || url.startsWith('https://www.') || url.startsWith('www.')){
    let arr = url.split('.')
    return arr[1];
  }
  else if (url.startsWith('http')){
    let arr1 = url.split('//').slice(1).join('').split('.');
    return arr1[0];
  }
  else {
    let arr = url.split('.')
    return arr[0];
  }
}
