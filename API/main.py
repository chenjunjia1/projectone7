import unittest
import allure
import os
import subprocess
from config import BASE_URL
from api.api_utils import ApiUtils
from tests.test_api import TestAPIs

if __name__ == "__main__":
    # 初始化测试报告目录
    allure_report_dir = "E:/python3.8/Code/API/reports/allure_report"
    os.makedirs(allure_report_dir, exist_ok=True)

    # 配置Allure报告
    allure_opts = ["--alluredir", allure_report_dir]

    # 加载测试套件
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestAPIs)

    # 运行测试
    with allure.step("Run API Tests"):
        unittest.TextTestRunner(verbosity=2).run(test_suite)

    # 生成Allure报告（使用绝对路径）
    allure_executable = "E:/python3.8/Allure/allure-commandline-2.24.0/allure-2.24.0/bin/allure.bat"
    subprocess.call([allure_executable, "generate", allure_report_dir, "--clean", "-o", "reports/allure_report/html"])

    # 打开Allure报告
    subprocess.call([allure_executable, "open", allure_report_dir])
