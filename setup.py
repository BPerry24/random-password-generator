import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='random-password-generator',
    version='0.0.1',
    author='Brady Perry',
    author_email='brdyprry@gmail.com',
    description='A cryptographically random and secure random password generator',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/BPerry24/random-password-generator.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Licesne :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6"
)