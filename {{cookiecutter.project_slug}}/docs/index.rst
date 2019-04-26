`{{ cookiecutter.project_name }}` 预处理模块 使用手册
======================================

`TTS` 预处理模块。

文字经过此模块处理后，再向后送给 `TTS` 合成引擎。确保每一个细节读到最好。

.. toctree::
   :maxdepth: 2
   :caption: 内容:

   readme
   installation
   usage
   modules
   contributing
   {% if cookiecutter.create_author_file == 'y' -%}authors
   {% endif -%}history

索引目录
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
