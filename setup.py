from setuptools import setup

setup(
      name='compare-strings',
      version='0.0.1',
      description='A library for measuring similarity between strings',
      py_modules=["CompareStrings",
                  "helpers\\helpers"],
      package_dir={'':'src'},
      classifiers = [
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independant",
          "Intended Audience :: Financial and Insurance Industry",
          "Intended Audience :: Fraud Prevention"
          ])