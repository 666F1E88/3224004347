# 导入单元测试框架
import unittest
# 导入操作系统接口
import os
# 导入临时文件模块
import tempfile
# 导入三个待测试的函数
from main import read_file, preprocess, calculate_similarity


class TestReadFile(unittest.TestCase):
    """
    测试read_file函数
    """

    def test_read_multiline_file(self):
        """
        读取含多行、中文、英文、数字的文件
        """
        
        content = "第一行 abc\n第二行 123\n第三行 end"
        # 创建临时文件
        with tempfile.NamedTemporaryFile(mode='w', delete=False,
                                          suffix='.txt', encoding='utf-8') as f:
            f.write(content)
            path = f.name

        # 读取文件
        result = read_file(path)
        # 删除临时文件
        os.unlink(path)
        
        self.assertEqual(result, content)

    def test_read_empty_file(self):
        """
        读取空文件应返回空字符串
        """
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False,
                                          suffix='.txt', encoding='utf-8') as f:
            path = f.name
            
        result = read_file(path)
        os.unlink(path)
        self.assertEqual(result, "")

    def test_read_missing_file(self):
        """
        文件不存在
        """
        
        with self.assertRaises(FileNotFoundError):
            read_file("this_file_does_not_exist_xyz.txt")


class TestPreprocess(unittest.TestCase):
    """
    测试preprocess函数
    """

    def test_mixed_punctuation(self):
        """
        中英文标点混合去除
        """
        
        self.assertEqual(preprocess("Hello，世界！(test)？"), "Hello世界test")

    def test_fullwidth_and_halfwidth(self):
        """
        全角半角标点混合去除
        """
        
        self.assertEqual(preprocess("Ａ，Ｂ。Ｃ！"), "ＡＢＣ")

    def test_newline_tab_space(self):
        """
        换行、制表符、空格混合去除
        """
        
        self.assertEqual(preprocess("a\nb\tc d"), "abcd")

    def test_only_numbers_and_letters(self):
        """
        纯字母数字保持不变
        """
        
        self.assertEqual(preprocess("abc123XYZ"), "abc123XYZ")

    def test_empty_input(self):
        """
        空字符串输入返回空字符串
        """
        
        self.assertEqual(preprocess(""), "")


class TestCalculateSimilarity(unittest.TestCase):
    """
    测试calculate_similarity函数
    """

    def test_identical_long_text(self):
        """
        长文本完全相同，相似度输出1.0
        """
        
        text = "春眠不觉晓处处闻啼鸟夜来风雨声花落知多少"
        self.assertAlmostEqual(calculate_similarity(text, text), 1.0)

    def test_completely_unrelated(self):
        """
        完全不相关的两段文本，相似度低于0.3
        """
        
        sim = calculate_similarity("北京大学计算机系", "红烧排骨盖浇饭")
        self.assertLess(sim, 0.3)

    def test_one_is_substring(self):
        """
        一方是另一方的子串，相似度大于0.5
        """
        
        sim = calculate_similarity("春眠不觉晓处处闻啼鸟夜来风雨声", "处处闻啼鸟夜来风雨声")
        self.assertGreater(sim, 0.5)

    def test_repeated_characters(self):
        """
        重复字符的文本，相似度应合理
        """
        
        sim = calculate_similarity("aaaaaaaaaa", "aaaaabbbbb")
        self.assertGreater(sim, 0.4)
        self.assertLess(sim, 1.0)

    def test_one_side_empty(self):
        """
        一方为空，相似度为0
        """
        
        self.assertEqual(calculate_similarity("你好世界", ""), 0.0)
        self.assertEqual(calculate_similarity("", "你好世界"), 0.0)

    def test_both_sides_empty(self):
        """
        双方都为空，相似度为0
        """
        
        self.assertEqual(calculate_similarity("", ""), 0.0)


if __name__ == '__main__':
    unittest.main()
