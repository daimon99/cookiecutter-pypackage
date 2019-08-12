# coding: utf-8
import pytest


@pytest.fixture
def {{cookiecutter.project_slug}}config():
    """引入测试用的配置文件"""
    import {{cookiecutter.project_slug}}config
    return {{cookiecutter.project_slug}}config
