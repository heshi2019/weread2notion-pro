from setuptools import setup, find_packages

setup(
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pendulum",
        "retrying",
        "github-heatmap",
    ],
    entry_points={
        "console_scripts": [
            "weread = weread2notionpro.weread:main"
        ],
    },
    author="xieke",
    author_email="xieke6379@163.com",
    description="将微信读书的数据同步出来",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/heshi2019/weread2notion-pro.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
