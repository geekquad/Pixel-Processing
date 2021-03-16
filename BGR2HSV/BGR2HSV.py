## From:https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html 
##
##    How to find HSV values to track?
##    This is a common question found in stackoverflow.com.
##    It is very simple and you can use the same function,
##    cv2.cvtColor(). Instead of passing an image, you just pass
##    the BGR values you want. For example, to find the HSV
##    value of Green, try following commands in Python terminal:
##
##    >>> green = np.uint8([[[0,255,0 ]]])
##    >>> hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
##    >>> print hsv_green
##    [[[ 60 255 255]]]
##    Now you take [H-10, 100,100] and [H+10, 255, 255] as
##    lower bound and upper bound respectively. Apart from
##    this method, you can use any image editing tools like
##    GIMP or any online converters to find these values, but
##    don’t forget to adjust the HSV ranges.

import cv2
import numpy as np
from tkinter import messagebox

class BGR2HSV():

    def __init__(self):
        self.log_file_name = ''
        self.color_BGR_in = []
        self.hsv_color_BGR_out = []
        self.HSV_int_list = []
        self.str_HSV_insert_comma = ''
        self.str_paint_net_equiv = ''

    def setLogFileName(self, log_file_name):        
        self.log_file_name = log_file_name
        f = open(self.log_file_name, "a")
        str_conversion_header = "Blue, Green, Red, Hue, Saturation, Value, ~Hue Paint.Net, ~Sat Paint.Net, ~Val Paint.Net \n"
        f.write(str_conversion_header)
        f.close()
        
    def setColorBGR_In(self, colorBGRin):        
        self.color_BGR_in = colorBGRin

    def getHSVOut(self):
        return self.hsv_color_BGR_out

    def getStrHSV(self):
        return self.str_HSV_insert_comma

    def getPaintNetHSV(self):
        return self.str_paint_net_equiv

    def resetHSVInt(self):
        self.HSV_int_list = []
    
    ##NOTE THIS IS BGR NOT RGB!
    def convert_BGR2HSV(self):

        if (self.log_file_name == ''):
            messagebox.showerror("BGR Value Error", "NO OUTPUT DIRECTORY SELECT. Select an output directory and try again.")
        else:
            color_BGR = np.uint8([[self.color_BGR_in]])
            self.hsv_color_BGR_out = cv2.cvtColor(color_BGR,cv2.COLOR_BGR2HSV)
            print (self.hsv_color_BGR_out)        
            print(self.color_BGR_in)
            str_color_in = "{}".format(self.color_BGR_in)
            str_color_in = str_color_in.replace("[", "")
            str_color_in = str_color_in.replace("]", "")
            print(str_color_in)
            
            str_HSV_result = "{}".format(self.hsv_color_BGR_out)
            str_HSV_remove_opening_bracket = str_HSV_result.replace("[", "")
            str_HSV_remove_closing_bracket = str_HSV_remove_opening_bracket.replace("]", "")
            str_HSV_remove_triple_whtspace = str_HSV_remove_closing_bracket.replace("   ", " ")
            str_HSV_remove_double_whtspace = str_HSV_remove_triple_whtspace.replace("  ", " ")
            str_str_HSV_remove_double_whtspace_strip = str_HSV_remove_double_whtspace.strip()        
            self.str_HSV_insert_comma = str_str_HSV_remove_double_whtspace_strip.replace(" ", ", ")
            print(str_HSV_remove_opening_bracket)
            print(str_HSV_remove_closing_bracket)
            print(str_HSV_remove_double_whtspace)
            print(str_str_HSV_remove_double_whtspace_strip)
            print(self.str_HSV_insert_comma)

            # Convert string to a list.
            HSV_list = list(self.str_HSV_insert_comma.split(", "))
            print(HSV_list)

            # String list to int list conversion of HSV_list
            for i in range(0, len(HSV_list)): 
                self.HSV_int_list.append(int(HSV_list[i]))            
            print(self.HSV_int_list)

            # Convert HSV values to approximate values in Paint.Net. NOTE: Hue values in Paint.Net range
            # from 0-360 and 0-179 in OpenCV, Saturation and Value range from 0-100 in Paint.Net and 0-255 in OpenCV.
            paint_net_hue = int(2*self.HSV_int_list[0])
            paint_net_sat = int((100/255)*self.HSV_int_list[1])
            paint_net_val = int((100/255)*self.HSV_int_list[2])

            print("{}, {}, {}".format(paint_net_hue, paint_net_sat, paint_net_val))
            self.str_paint_net_equiv = ("{}, {}, {}".format(paint_net_hue, paint_net_sat, paint_net_val))

            str_conversion_input_output = str_color_in + ", " + self.str_HSV_insert_comma +", " + self.str_paint_net_equiv +"\n"
            print(str_conversion_input_output)
            
            f = open(self.log_file_name, "a")
            f.write(str_conversion_input_output) 
            f.close()
