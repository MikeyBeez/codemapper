from setuptools import setup, find_packages

setup(
    name='codemapper',
    version='0.1.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        # Add any dependencies here, for example:
        # 'requests',
        # 'beautifulsoup4',
    ],
    entry_points={
        'console_scripts': [
            'codemapper=cli:main',
        ],
    },
    author='MikeyBeez',
    author_email='mbonsign@gmail.com',
    description='A tool to map a code repository for LLM editing',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/MikeyBeez/codemapper',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
