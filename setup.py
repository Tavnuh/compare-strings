from setuptools import setup

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
      name='compare-strings',
      version='0.0.1',
      description='A library for measuring similarity between strings',
      py_modules=["CompareStrings",
                  "helpers\\helpers"],
      package_dir={'':'src'},
      install_requires = [
          
          ], 

      classifiers = [
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independant",
          "Intended Audience :: Financial and Insurance Industry",
          "Intended Audience :: Fraud Prevention"
          ],
      long_description = long_description,
      long_description_content_type = "text/markdown"
      
      )