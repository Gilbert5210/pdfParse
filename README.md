<!--
 * @Author: zhanjiangyuan zhanjiangyuan@kuaishou.com
 * @Date: 2024-12-22 15:13:52
 * @LastEditors: zhanjiangyuan zhanjiangyuan@kuaishou.com
 * @LastEditTime: 2024-12-22 15:14:09
 * @FilePath: /pdfParse/README.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->

# PDF 关键词提取工具

## 简介

这是一个用于从 PDF 文件中提取特定关键词及其后跟随的名字的工具。该工具支持批量处理指定目录下的所有 PDF 文件，并将结果输出到一个文本文件中。

## 小白如何使用
- 在dist目录下有两个文件分别为
  - mac 应用包：extract_pdf
  - window应用包: extract_pdf.exe
  - 下载到你本地后
- 分别怎么使用？
  - mac 应用包：
    - 在终端输入
    ```shell
     # 在这个目录下sourceFiles为需要待查找的文件
      extract_pdf ./sourceFiles/
    ```

  - window应用包：
    - 在终端输入
    ```shell
     # 在这个目录下sourceFiles为需要待查找的文件
      extract_pdf.exe ./sourceFiles/
    ```


## 安装依赖

### 在 Windows 上安装依赖

1. 打开命令提示符（Command Prompt）或 PowerShell。
2. 确保你已经安装了 Python。如果没有安装，可以从 [Python 官方网站](https://www.python.org/) 下载并安装。
3. 安装所需的 Python 包：
   ```sh
      pip install pymupdf
   ```

### 使用方法

在 Windows 上使用
打开命令提示符（Command Prompt）或 PowerShell。
导航到包含 extract_pdf.py 脚本的目录：
把你本地文件复制全部放到 sourceFiles 文件夹下

```sh
# 在这个目录下
python extract_pdf.py ./sourceFiles/

```
