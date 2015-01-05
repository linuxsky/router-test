__author__ = 'shiyang'
#encoding:UTF-8

import ConfigParser

import UT_serial

CONFIG_FILE = "config.conf"

def inred( s ):
    return"%s[31;2m%s%s[0m"%(chr(27), s, chr(27))

def inblue( s ):
    return"%s[34;2m%s%s[0m"%(chr(27), s, chr(27))

def uart_test():
    cf = ConfigParser.ConfigParser()
    cf.read(CONFIG_FILE)
    uart_name = cf.get("serial","SER_NAME")
    uart_batrate = cf.getint("serial","SER_BARATE")
    ret = UT_serial.Test_serial_main(uart_name,uart_batrate)
    if(ret):
        print "UT-Serial test" + inred(" Failed!")
    else:
        print "UT-Serial test" + inblue(" Success!")


if __name__ == '__main__':
    uart_test()