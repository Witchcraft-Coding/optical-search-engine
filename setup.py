from setuptools import setup,find_packages

with open("README.md", "r", encoding="utf-8") as fh:
  long_description = fh.read()

setup(
  name='opsearch',
  version='0.0.7',
  author='Medha Tripathi, Param Siddharth',
  author_email='medha@witwiz.vip, param@witwiz.vip',
  description='A search engine which combs through images, not words.',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/Witchcraft-Coding/optical-search-engine',
  packages=find_packages(),
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  python_requires='>=3.8',
  entry_points={
    'console_scripts': [
      'opsearch = opsearch.main:app'
    ]
  }
)