from setuptools import setup, find_packages

setup(
    name='AMP',
    description='mostra dados professores',
    packages=find_packages(),
    entrypoints={'console_scripts':['AMP = AMP.__main__:start']}
)