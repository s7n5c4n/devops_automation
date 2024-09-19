from setuptools import setup, find_packages

setup(
    name="devops_automation",
    version="1.1.0",
    author="s7n5c4n",
    author_email="cr.hachim2.0@gmail.com",
    description="Librería para la automatización de tareas DevOps",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/s7n5c4n/devops_automation",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[ 
        "docker",
        "requests",
    ],
)
