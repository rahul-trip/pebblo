from setuptools import setup, find_packages

setup(
    name="daxa",
    python_requires=">=3.7",
    version="0.1.0",
    url="https://github.com/daxa-ai/daxa-analyzer-rc",
    license="Other/Proprietary License",
    description="Daxa OpenSource",
    long_description="Daxa OpenSource TBD",
    long_description_content_type="text/markdown",
    author="Daxa OpenSource Authors",
    author_email="info@daxa.ai",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "fastapi==0.109.0",
        "uvicorn==0.25.0",
        "pydantic==1.10.0a1",
        "presidio-analyzer==2.2.351",
        "presidio-anonymizer==2.2.351",
        "torch==2.1.2",
        "transformers==4.36.2",
        "jinja2>=3.1.3",
        "weasyprint==60.2"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    zip_safe=False,
)
