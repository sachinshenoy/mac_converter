# import sys
# sys.path.append(r"c:\users\YOURUSERNAME\appdata\local\programs\python\python35-32\lib\site-packages")
import pyperclip
import re


def get_mac():
    """Used to get the mac from the clip board"""
    return pyperclip.paste()


def convert(mac_address):
    """Converts the MAC from xxxx.xxxx.xxxx format to xx:xx:xx:xx:xx format or vise versa"""

    # Regex to match MAC Address patterns xx.xx.xx.xx.xx.xx or xxxx.xxxx.xxxx
    # with separator '.' or '-' or ':'
    regex = r"(([A-F0-9]{2}[:.-]){5}[A-F0-9]{2}|([A-F0-9]{4}[:.-]){2}[A-F0-9]{4})"

    # Findall used to look for all instances of the match, with multiline and ignore case flags
    mac_tuple = re.findall(regex, mac_address, re.MULTILINE | re.IGNORECASE)

    # Initializing temp variables. i for iteration, result for return result collection and
    # temp for temporary string variable storage and manipulation.
    # separator to store the separator used with the input mac address format.
    i = 0
    result = []
    temp = ''
    separator = ''
    while i < len(mac_tuple):
        # Check if the MAC Address format is a xx.xx.xx.xx.xx.xx then results are in xxxx.xxxx.xxxx format
        if (mac_tuple[i][0].count(':') == 5 or mac_tuple[i][0].count('.') == 5 or mac_tuple[i][0].count('-') == 5):
            separator = mac_tuple[i][0][2]
            temp = mac_tuple[i][0].replace(separator, '')
            temp = temp[0:4] + separator + temp[4:8] + separator + temp[8:] + '\r\n'
            result.append(temp)
            i += 1
        # When the MAC Address is in the xxxx.xxxx.xxxx format, result are xx.xx.xx.xx.xx.xx
        else:
            separator = mac_tuple[i][0][4]
            temp = mac_tuple[i][0].replace(separator, '')
            temp = temp[0:2] + separator + temp[2:4] + separator + temp[4:6] + separator + temp[6:8] \
                   + separator + temp[8:10] + separator + temp[10:] + '\r\n'
            result.append(temp)
            i += 1
    return ''.join(result)


def main():

    """
    MAC ADDRESS Format Converter for Windows Clipboard:
    --------------------------------------------------
    This program takes input text which is copied to the windows clipboard containing MAC Addresses and
    outputs the mac address in the transformed format.

    For example:
    input format is xxxx.xxxx.xxxx the output will be xx.xx.xx.xx.xx.xx
    input format xx.xx.xx.xx.xx.xx will result in output in xxxx.xxxx.xxxx format

    The input separator used in the output will match the one from the input. Also the text can contain multiple
    mac addresses intermingled with other text for Data

    Usage:
        Just copy the input text to windows clipboard and run the program then
        paste the output from the windows clipboard to the required document.

    Works/Tested for Windows 7, Windows 8.x and Window 10"""

    pyperclip.copy(convert(get_mac()))
#    print(convert(mac_address))


if __name__ == '__main__':
    main()
