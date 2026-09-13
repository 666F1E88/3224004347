# 获取命令行参数和退出程序
import sys
def read_file(path):
    """
    读取文件内容
    """
    # 以只读模式打开文件，编码使用utf-8
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()
def main():
    """
    解析命令行参数，读取原文和抄袭版文件，并打印内容。
    """
    if len(sys.argv) != 4:
        # 如果命令行参数数量不为4，则提示正确用法
        print("用法：python main.py <原文文件> <抄袭版文件> <答案文件>")
        sys.exit(1)

    # 从命令行参数中取出原文文件路径
    orig_path = sys.argv[1]
    # 从命令行参数中取出抄袭版文件路径
    orig_add_path = sys.argv[2]

    # 读取文件内容，并保存
    orig = read_file(orig_path)
    orig_add = read_file(orig_add_path)

    print("原文：", orig)
    print("抄袭版：", orig_add)
if __name__ == '__main__':
    main()
