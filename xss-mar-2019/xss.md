% XSS and More 
% @global4g 
% Mar 2019

# XSS 


## Browser
-  How many tabs do you you have
-  javascript and DOM 
-  <https://www.w3schools.com/js/js_htmldom.asp>

## What is XSS
- OWASP 10
- Different Categories/Impact



## Whats in a name 
- XSS / CSS 
- SOP 
- <https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy>


## Is XSS a vulnerability 
- <https://www.owasp.org/index.php/Cross-site_Scripting_(XSS)> 
- CSS.pdf 


# Demo 1

## Reflected XSS

- Steal Cookies 
- Change page layout 
- Login Form 

# Exploits 

## Types of Exploits 

- Authenticated
- Unauthenticated / Remote 


# Info Exposure 

## Non Sensitive

- Email Addresses
- Internal IP Addresses
- Host Names, etc.
 



# Demo 2

## Internal Site

- Vulnerable to Unauthenticated exploits 


# Demo 3

## Cors/Frame POC 


# Demo 4

## Chaining

- Combine seemingly trivial vulnerabilites to cause devastating damage



# Recap 

## Not just exploits

------------------

![Traditional XSS Exploit](pic-xss1.png)



------------------

![Another XSS Exploit](pic-xss2.png)


# All good things come to end


## Other Resources

- <https://github.com/petercunha/Jenkins-PreAuth-RCE-PoC/blob/master/README.txt> 
- <http://blog.orange.tw/2019/02/abusing-meta-programming-for-unauthenticated-rce.html> 
- <https://github.com/adamyordan/cve-2019-1003000-jenkins-rce-poc> 
- <https://www.youtube.com/watch?v=abuH-j-6-s0>

## Command line for presentation 
- pandoc -t revealjs -s -o xss.html xss.md -V revealjs-url=http://lab.hakim.se/reveal-js -V theme=blood
