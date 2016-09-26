from setuptools import setup, find_packages

setup(
    name = "unsubscribe",
    version = "1.0.0",
    packages = find_packages(),
    author = "Kevin Kennell",
    author_email = "kevin@kennell.de",
    license = "MIT",
    url = "http://github.com/kennell/unsubscribe",
    install_requires=[
        'click',
        'requests',
        'scandir',
        'tqdm'
    ],
    entry_points={
        'console_scripts': [
            'unsubscribe = unsubscribe.cli:main'
        ]
    }
)