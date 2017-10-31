from setuptools import setup, find_packages

setup(
    name='calculator',

    version='1.0.0',

    description='Stock Calculator',

    entry_points={
        'console_scripts': [
            'stock_calculator = calculator.app:main'
        ]
    },

    packages=find_packages(exclude=['contrib', 'docs', 'test*', 'bin']),
    include_package_data=True,
    install_requires=[
        'flask'
    ],
)