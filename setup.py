import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="piskle",
    version="0.1.1",
    author="Amal HASNI, Dhia HMILA",
    author_email="emerald.snippets@gmail.com",
    description="Piskle allows you to selectively and efficiently serialize scikit-learn models "
                "to save on memory and load times.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    url="https://github.com/hmiladhia/piskle",
    packages=['piskle'],
    install_requires=['scikit-learn==0.24.0'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords=['serialization', 'scikit-learn', 'export', 'pickle', 'models', 'objects', 'joblib', 'estimators'],
)
