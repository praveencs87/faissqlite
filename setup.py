from setuptools import setup, find_packages

setup(
    name='faissqlite',
    version='0.1.0',
    description='Persistent and efficient vector store using FAISS + SQLite',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/praveencs87/faissqlite',
    packages=find_packages(),
    install_requires=[
        'faiss-cpu>=1.7.4',
        'numpy>=1.21.0',
    ],
    extras_require={
        'api': ['fastapi>=0.100.0'],
    },
    python_requires='>=3.7',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'faissqlite=faissqlite.cli:main',
        ],
    },
)
