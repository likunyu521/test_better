#!/usr/bin/env python
# coding=utf-8
import pytest
import allure
import os


@pytest.fixture(scope='function')
def login():
    print("登录")
    yield
    print("登录完成")


@allure.feature('加入购物车')
def test_1(login):
    '''将苹果加入购物车'''
    print("测试用例1")


@allure.feature('加入购物车2')
def test_2():
    '''将橘子加入购物车'''
    print("测试用例2")


if __name__ == "__main__":
    # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
    pytest.main(["s", "-q", "--alluredir", "./temp"])
    # 执行命令 allure generate ./temp -o ./report --clean ，生成测试报告
    # os.system('allure generate ./temp -o ./report --clean')