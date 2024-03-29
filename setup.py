from setuptools import setup

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
      name='compare-strings',
      version='0.0.3',
      description='A library for measuring similarity between strings',
      py_modules=["CompareStrings",
                  "helpers\\helpers"],
      package_dir={'':'src'},
      install_requires = [
          "pandas>=1.2.4",
          "numpy>=1.19.5",
          "python_Levenshtein>=0.12.2",
          ], 
      extras_require = {
          "dev": [
              "pytest>=3.7"
              ]
          },
      classifiers = [
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Intended Audience :: Financial and Insurance Industry"
          ],
      long_description = long_description,
      long_description_content_type = "text/markdown"
      
      )