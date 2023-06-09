import time
import os
import unittest
from HtmlTestRunner import HTMLTestRunner

# 定义输出的文件位置和名字
DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
now = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))

filename = now + "report.html"
# discover方法执行测试套件
testsuite = unittest.defaultTestLoader.discover(
    start_dir='../test_case',
    pattern='*test.py',
    top_level_dir=None
)

# 这里遇到困难了，title报错，搜了一下可能时最新的HTMLTestRunner改变了格式的定义，找一下官方文档
# 到最顶部导入库那里，ctrl+点击，直接跳转到源码，发现已经不叫title了，而是叫report_title tester叫report_name  而descripiton已经无了
with open(DIR + '/reports/' + filename, 'w') as f:
    runner = HTMLTestRunner(
        stream=f,
        verbosity=1,
        report_title='gateway UI report',
        report_name='tester'
        # description='执行情况',
    )
    runner.run(testsuite)


