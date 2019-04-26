.. highlight:: console

============
贡献代码
============

构建开发环境
---------------

构建操作::

    $ git clone git@git.taijihuabao.com:tjhb/{{ cookiecutter.project_slug }}
    $ python3 -m venv env
    $ pip install -r requirements.txt

测试
--------

先写测试用例，再写代码。

运行测试用例::

    $ pytest

上传代码
----------

设置私有库配置::

    $ vi ~/.pypirc

.. code-block:: ini

    [distutils]
    index-servers =
        pypi
        tjhb

    [pypi]
    repository: https://www.python.org/pypi

    [tjhb]
    repository: http://pypi.taijihuabao.com/
    username: <username>
    password: <password>

变更版本号::

    $ make minor

> minor / major / patch，看你的升级程度

上传::

    $ make release
