import sys
import re
from difflib import SequenceMatcher

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
    # 去掉标点
    text = re.sub(r'[^\w\s]', '', text)
    # 去掉空白
    text = re.sub(r'\s+', '', text)
    return text

def calculate_similarity(orig, orig_add):
    """
    基于LCS计算相似度
    相似度 = LCS 长度 / 较长序列长度
    """
    # 预处理，保留纯文字
    orig_clean = preprocess(orig)
    orig_add_clean = preprocess(orig_add)

    # 有空时返回0
    if not orig_clean or not orig_add_clean:
        return 0.0

    # 按字符比较
    matcher = SequenceMatcher(None, orig_clean, orig_add_clean)
    # 返回所有匹配块
    lcs_length = sum(block.size for block in matcher.get_matching_blocks())

    # 除以较长序列的长度
    max_length = max(len(orig_clean), len(orig_add_clean))
    return lcs_length / max_length

def main():
    # 检查命令行参数数量
    if len(sys.argv) != 4:
        print("用法：python main.py <原文文件> <抄袭版文件> <答案文件>")
        sys.exit(1)

    # 从命令行参数取出三个路径
    orig_path = sys.argv[1]
    orig_add_path = sys.argv[2]
    ans_path = sys.argv[3]

    # 读取两个文件
    orig = read_file(orig_path)
    orig_add = read_file(orig_add_path)

    # 计算相似度
    similarity = calculate_similarity(orig, orig_add)

    # 写入答案文件，保留两位小数
    with open(ans_path, 'w', encoding='utf-8') as f:
        f.write(f"{similarity:.2f}")

    # 打印
    print(f"重复率：{similarity:.2f}")

if __name__ == '__main__':
    main()
