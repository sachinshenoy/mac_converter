import sys
sys.path.append(r"c:\users\YOURUSERNAME\appdata\local\programs\python\python35-32\lib\site-packages")
import pyperclip

def get_mac():
    '''Used to get the mac from the clip borad'''
    return pyperclip.paste()

def convert(mac_address):
    '''Converts the MAC from xxxx.xxxx.xxxx format to xx:xx:xx:xx:xx format or vise versa'''
    if str(mac_address).count(".",0,len(mac_address))==2 and len(mac_address)==14:
        #Convert MAC from xxxx.xxxx.xxxx format to xx:xx:xx:xx:xx:xx format
        mac_address=str(mac_address)
        mac_address=mac_address.replace(".","")
        count = 1
        mac_address=list(mac_address)
        while(count<14):
            mac_address.insert(count+1,":")
            count+=3
        return (''.join(mac_address)).lower()

    elif str(mac_address).count(":",0,len(mac_address))==5 and len(mac_address)==17:
        #Convert MAC from xx:xx:xx:xx:xx:xx format to xxxx.xxxx.xxxx format
        mac_address=str(mac_address)
        mac_address=mac_address.replace(":","")
        count = 3
        mac_address=list(mac_address)
        while(count<13):
            mac_address.insert(count+1,".")
            count+=5
        return (''.join(mac_address)).lower()

    elif str(mac_address).count("-",0,len(mac_address))==5 and len(mac_address)==17:
        #Convert MAC from xx-xx-xx-xx-xx-xx format to xxxx.xxxx.xxxx format
        mac_address=str(mac_address)
        mac_address=mac_address.replace("-","")
        count = 3
        mac_address=list(mac_address)
        while(count<13):
            mac_address.insert(count+1,".")
            count+=5
        return (''.join(mac_address)).lower()

    elif str(mac_address).count("\r\n")>0:
        #Converts multiline clipboards normally from copying several rows in excel for example.
        multi_line=str(mac_address).split("\r\n")
        size=len(multi_line)
        result=list()
        for x in range(0,size-1):
            single_result=convert(multi_line[x])
            result.append(single_result+"\r\n")
        return ''.join(result)

    else:
        return "Invalid MAC format"


def main():
    pyperclip.copy(convert(get_mac()))


if __name__ == '__main__':
    main()

