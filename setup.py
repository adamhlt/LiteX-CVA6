import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

from pythondata_cpu_cva6 import version_str

setuptools.setup(
    name="pythondata-cpu-cva6",
    version=version_str,
    author="Massimiliano Giacometti",
    author_email="massimiliano.giacometti@planv.tech",
    description="""\
Python module containing system_verilog files for CVA6 cpu.""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/litex-hub/pythondata-cpu-cva6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    zip_safe=False,
    packages=setuptools.find_packages(),
    package_data={
    	'cpu_cva6': ['cpu_cva6/system_verilog/**'],
    },
    include_package_data=True,
    project_urls={
        "Bug Tracker": "https://github.com/litex-hub/pythondata-cpu-cva6/issues",
        "Source Code": "https://github.com/litex-hub/pythondata-cpu-cva6",
    },
)
