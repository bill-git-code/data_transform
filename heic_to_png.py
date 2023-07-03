# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 14:36:57 2023

@author: Bill Kuo
"""

from PIL import Image

def convert_heic_to_png(input_file, output_file):
    image = Image.open(input_file)
    image.save(output_file, "PNG")

# 使用範例
input_heic_file = 'input.heic'
output_png_file = 'output.png'
convert_heic_to_png(input_heic_file, output_png_file)
