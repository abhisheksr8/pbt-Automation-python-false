from setuptools import setup, find_packages

setup(
    name='AutomationPBT-falsepython',
    version='1.0',
    packages=find_packages(include=['automationpbtfalsepython*']),
    description='AutomationPBT-falsepython',
    install_requires=[
        'prophecy-libs==1.9.5'
    ],
    entry_points={
        'console_scripts': [
            'main = automationpbtfalsepython.pipeline:main',
        ],
    },
    data_files=[(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require={
        'test': ['pytest', 'pytest-html'],
    }
)