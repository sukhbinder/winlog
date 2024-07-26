import setuptools
import os

def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()
    

setuptools.setup(
    name='WinLog',
    version='0.0.1',
    description='A Python script to log active Windows title to desktop log',
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    project_urls={
        "Documentation": "https://sukhbinder.wordpress.com",
        "Issues": "https://github.com/sukhbinder/winlog/issues",
        "CI": "https://github.com/sukhbinder/winlog/actions",
        "Changelog": "https://github.com/sukhbinder/winlog/releases",
    },
    license="Apache License, Version 2.0",
    author='Sukhbinder Singh',
    author_email='sukh2010@yahoo.com',
    url='https://github.com/sukhbinder/winlog',
    py_modules=['winlog'],
    entry_points={
        'console_scripts': ['winlog = winlog:main']
    },
    python_requires=">=3.8",
    extras_require={
        "test": [
            "pytest",
        ]
    },
)
