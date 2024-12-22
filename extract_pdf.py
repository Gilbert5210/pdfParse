import fitz  # PyMuPDF
import sys
import os
import re
from pathlib import Path

def extract_text_from_pdf(pdf_path):
    # 打开 PDF 文件
    doc = fitz.open(pdf_path)
    text_content = ''

    # 遍历每一页
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text_content += page.get_text("text") + '\n'

    return text_content

def write_to_file(content, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(content)

def extract_keywords(text, keywords):
    results = []
    for keyword in keywords:
        pattern = re.compile(rf'{re.escape(keyword)}\s*(\S+)', re.IGNORECASE)
        matches = pattern.findall(text)
        for match in matches:
            results.append((keyword, match))
    return results

def main():
    if len(sys.argv) < 2:
        print("使用方法: python extract_pdf.py <PDF文件目录>")
        sys.exit(1)

    directory = os.path.abspath(sys.argv[1])

    if not os.path.isdir(directory):
        print(f"目录不存在: {directory}")
        sys.exit(1)

    output_path = 'output.txt'
    all_results = []

    # 遍历目录下的所有 PDF 文件
    for pdf_file in Path(directory).glob('*.pdf'):
        pdf_path = str(pdf_file)
        try:
            text_content = extract_text_from_pdf(pdf_path)
            keywords = ['编辑部主任', '编辑部副主任', '执行主编', '责任编辑', '常务副主编']
            extracted_content = extract_keywords(text_content, keywords)
            all_results.extend(extracted_content)
        except Exception as e:
            print(f"处理文件 {pdf_path} 时出错: {e}")

    # 将所有结果写入文件
    with open(output_path, 'w', encoding='utf-8') as file:
        for keyword, name in all_results:
            file.write(f"{keyword}: {name}\n")

    print(f"提取的文本已保存到: {output_path}")

if __name__ == "__main__":
    main()