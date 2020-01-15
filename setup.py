import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="demo-my-demo-app",
    version="0.0.1",

    description="AWS EKS + Kafka POC stack: demo my-demo-app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="Israel Fdez.",

    package_dir={"": "my-demo-app"},
    packages=setuptools.find_packages(where="eks_kafka"),

    install_requires=[

    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",


        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Typing :: Typed",
    ],
)
