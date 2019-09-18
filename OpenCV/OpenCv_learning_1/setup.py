from setuptools import setup

setup(
    name='process_automation',
    version='1.0',
    packages = ['process_automation'],
    install_requires=[
        'process_automation',
        'boto3',
        'opencv-python',
        'numpy',
        'botocore',
        'slackclient'
    ]
)