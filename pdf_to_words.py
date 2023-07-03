# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 13:18:39 2023

@author: Bill Kuo
"""

from pdf2docx import Converter

def convert_pdf_to_word(input_file, output_file):
    cv = Converter(input_file)  # 建立 Converter 物件，傳入 PDF 檔案路徑
    cv.convert(output_file, start=0, end=None)  # 將 PDF 轉換為 Word，並指定輸出檔案路徑
    cv.close()  # 關閉 Converter 物件

# 使用範例
input_pdf_file = 'input.pdf'  # 輸入的 PDF 檔案路徑
output_word_file = 'output.docx'  # 輸出的 Word 檔案路徑
convert_pdf_to_word(input_pdf_file, output_word_file)  # 呼叫函式進行轉換
