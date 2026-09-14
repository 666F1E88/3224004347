import sys
import re
from rapidfuzz.distance import LCSseq

# 预编译正则表达式
PUNCT_PATTERN = re.compile(r'[^\w\s]')
SPACE_PATTERN = re.compile(r'\s+')


def read_file(path):
    """
    读取文件内容
    """

    # 以只读模式打开文件，编码使用utf-8
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def preprocess(text):
    """
    去除标点符号和空白字符
    """
    
    text = PUNCT_PATTERN.sub('', text)
    text = SPACE_PATTERN.sub('', text)
    return text


def calculate_similarity(orig, orig_add):
    """
    基于LCS计算相似度，使用LCSseq.similarity
    """

    # 预处理
    orig_clean = preprocess(orig)
    orig_add_clean = preprocess(orig_add)

    # 如果空则返回0
    if not orig_clean or not orig_add_clean:
        return 0.0

    # 计算两段文本的LCS长度
    lcs_length = LCSseq.similarity(orig_clean, orig_add_clean)

    max_length = max(len(orig_clean), len(orig_add_clean))
    
    return lcs_length / max_length


def main():
    """
    解析命令行参数，读取文件，计算相似度，写入答案文件
    """

    # 检查命令行参数数量是否为4
    if len(sys.argv) != 4:
        print("用法：python main.py <原文文件> <抄袭版文件> <答案文件>")
        sys.exit(1)

    # 从命令行参数获取三个路径
    orig_path = sys.argv[1]
    orig_add_path = sys.argv[2]
    ans_path = sys.argv[3]

    # 读取文件
    orig = read_file(orig_path)
    orig_add = read_file(orig_add_path)

    # 计算相似度
    similarity = calculate_similarity(orig, orig_add)

    # 结果保留两位小数，写入答案文件
    with open(ans_path, 'w', encoding='utf-8') as f:
        f.write(f"{similarity:.2f}")

    # 打印
    print(f"重复率：{similarity:.2f}")


if __name__ == '__main__':
    main()
