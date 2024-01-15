from setuptools import setup, find_packages

with open("README.md","r") as f:
    description = f.read()

setup(
    name='datacompass',
    version='0.4',
    packages=find_packages(),
    description='EDA in 4 lines of Code',
    long_description=description,
    long_description_content_type='text/markdown',
    author='sai_koushik',
    author_email='saikoushik.gsk@gmail.com',
    url='https://github.com/koushik2299/DataCompass',
    install_requires=[
        'pandas',  # include any other dependencies your package needs
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
