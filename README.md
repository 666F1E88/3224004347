# PaperCheck 论文查重

## 功能
输入原文和抄袭版论文，计算重复率，输出到答案文件。

## 安装依赖
```bash
pip install -r requirements.txt
```

## 运行程序
**用法：python main.py <原文文件> <抄袭版文件> <答案文件>**
```bash
python main.py orig.txt orig_0.8_add.txt ans.txt
python main.py orig.txt orig_0.8_del.txt ans.txt
python main.py orig.txt orig_0.8_dis_1.txt ans.txt
python main.py orig.txt orig_0.8_dis_10.txt ans.txt
python main.py orig.txt orig_0.8_dis_15.txt ans.txt
```

## 查看性能
```bash
python -m cProfile -s tottime main.py orig.txt orig_0.8_add.txt ans.txt
```

## 查看测试覆盖率
```bash
python -m coverage run -m unittest test_main.py
python -m coverage report
python -m coverage html
```

## 运行单元测试
```bash
python -m unittest test_main.py -v
```
