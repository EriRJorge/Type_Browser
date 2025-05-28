from setuptools import setup, find_packages

setup(
    name="Type_Browser",
    version="1.1.0",
    description="A modern, lightweight web browser built with Python and Qt",
    author="Type Browser Team",
    author_email="contact@typebrowser.com",
    url="https://github.com/typebrowser/type-browser",
    packages=find_packages(),
    install_requires=[
        "PyQt5>=5.15.0",
        "PyQtWebEngine>=5.15.0",
    ],
    entry_points={
        "console_scripts": [
            "type-browser=TypeBrowser:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Internet :: WWW/HTTP :: Browsers",
        "Topic :: Desktop Environment :: Desktop Environment",
    ],
    python_requires=">=3.8",
    include_package_data=True,
    package_data={
        "Type_Browser": [
            "icon.png",
            "*.ui",
            "*.qss",
        ],
    },
    long_description="""
Type Browser is a modern, lightweight web browser built with Python and Qt.
It features a clean, dark-themed interface and essential browsing capabilities.

Features:
- Fast and secure browsing
- Modern dark theme UI
- Tabbed browsing
- Bookmark management
- Download manager
- Customizable settings

Requirements:
- Python 3.8 or higher
- PyQt5 5.15.0 or higher
- PyQtWebEngine 5.15.0 or higher
""",
    long_description_content_type="text/markdown",
) 