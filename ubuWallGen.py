#!/usr/bin/env python
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
    if(len(imglist)):
        if len(argv):
            write_xml_to_file(file, imglist, int(argv[0]))
        else:
            write_xml_to_file(file, imglist, 1795)
    file.close()

def is_image(filename):
    """ Returns true if file extension in jpg, png or gif """
    return filename.endswith((".jpg", ".png", ".gif",".jpeg"))

def write_xml_to_file(file, imglist, interval):
    """ Generates xml and writes it to the file passed as argument """
    file.write(
"""<background>""")
    file.write("""
    <static>
        <duration>{1}</duration>
        <file>{0}</file>
    </static>
    <transition>
        <duration>5</duration>
        <from>{0}</from>""".format(imglist[0], interval))
    for img in imglist[1:]:
        file.write("""
        <to>{0}</to>
    </transition>
    <static>
        <duration>{1}</duration>
        <file>{0}</file>
    </static>
    <transition>
        <duration>5</duration>
        <from>{0}></from>""".format(img, interval))
    file.write("""
        <to>{0}</to>
    </transition>
</background>\n""".format(imglist[0]))

if __name__ == "__main__":
    main(sys.argv[1:])
