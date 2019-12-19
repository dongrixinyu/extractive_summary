# -*- coding=utf-8 -*-

from setuptools import setup

# version 0.1.0: 使用 lda 主题模型，同时利用 word 级别 tfidf 信息，
# lead-3 信息，增加句子冗余信息处理规则，使用 MMR 算法抽取句子。

# setup
setup(name="cse",
      version="0.1.0",
      url="https://github.com/dongrixinyu/extractive_summary",
      author="dongrixinyu",
      author_email="dongrixinyu.89@163.com",
      
      py_modules=[],
      packages=[
            "cse",
      ],

      include_package_data=True,
      install_requires=[
          "pkuseg"
      ],

      entry_points={
      },
)
