#!/usr/bin/env python3
import sys
import os

def main(argv):
    """ Generate xml file of files in dir fr ubuntu desktop wallpaper """
    dirlist = os.listdir(os.getcwd()) 
    imglist = []
    for item in dirlist:
        if is_image(item):
            imglist.append("{0}/{1}".format(os.getcwd(), item))
    file = open('desktop.xml', 'w')
    write_xml_to_file(file, imglist)
    file.close()

def is_image(filename):
    """ Returns true if file extension in jpg, png or gif """
    return filename.endswith((".jpg", ".png", ".gif",))

def write_xml_to_file(file, imglist):
    """ Generates xml and writes it to the file passed as argument """
    file.write(
"""<background>
    <starttime>
        <year>2009</year>
        <month>12</month>
        <day>21</day>
        <minute>00</minute>
    </starttime>""")
    file.write("""
    <static>
        <duration>1795.0</duration>
        <file>{0}</file>
    </static>
    <transition>
        <duration>5</duration>
        <from>{0}></from>""".format(imglist[0]))
    for img in imglist:
        file.write("""
        <to>{0}</to>
    </transition>
    <static>
        <duration>5</duration>
        <file>{0}</file>
    </static>
    <transition>
        <duration>5</duration>
        <from>{0}></from>""".format(img))
    file.write("""
        <to>{0}</to>
    </transition>
</background>\n""".format(imglist[0]))

if __name__ == "__main__":
    main(sys.argv[1:])
