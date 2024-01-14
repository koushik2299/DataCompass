from setuptools import setup, find_packages

setup(
    name='datacompass',
    version='0.1',
    packages=find_packages(),
    description='A short description of your package',
    long_description=open('README.md').read(),
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
