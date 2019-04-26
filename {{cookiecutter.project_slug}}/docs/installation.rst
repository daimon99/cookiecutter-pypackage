.. highlight:: shell

============
安装
============



稳定版本
--------------

打开控制台，运行:

.. code-block:: console

    $ pip install --extra-index-url http://<username>:<password>@pypi.taijihuabao.com/ --trusted-host pypi.taijihuabao.com {{ cookiecutter.project_slug }}

如果你直接写在 `requirements.txt` 中，这样写

.. code-block:: ini

    --extra-index-url http://<username>:<password>@pypi.taijihuabao.com/
    --trusted-host pypi.taijihuabao.com
    {{ cookiecutter.project_slug }}
