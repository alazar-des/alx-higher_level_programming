#!/usr/bin/python3                                                                                                                
"""                                                                                                                               
Python script sends an email and print the response body                                                                          
"""                                                                                                                               
from urllib import request, parse                                                                                                 
import sys                                                                                                                        
                                                                                                                                  
                                                                                                                                  
if __name__ == "__main__":                                                                                                        
    url = sys.argv[1]                                                                                                             
    data = parse.urlencode({'email': sys.argv[2]}).encode()                                                                       
    req = request.Request(url, data=data)                                                                                         
    with request.urlopen(req) as resp:                                                                                            
        html = resp.read().decode("utf-8")                                                                                        
        print(html)                      
