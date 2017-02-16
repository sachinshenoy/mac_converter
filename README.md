# mac_converter
Converts MAC address from the clip board

Format 1
xx:xx:xx:xx:xx:xx to xxxx.xxx.xxx 

Format 2
xxxx.xxx.xxx to xx:xx:xx:xx:xx:xx  

Format 3
xx-xx-xx-xx-xx-xx to xxxx.xxx.xxx  
 
It will also do multi lines for example if you copy several rows in excel. 
 
It will flip between formats xx:xx:xx:xx:xx:xx and xxxx.xxx.xxx  depending on which one you send it and will always convert xx-xx-xx format to xxxx.xxx.xxx  

Requires pyperclip library 


