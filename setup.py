from setuptools import setup

setup(
    name="Simple_QR_Code",
    version="1.0.0",
    author="Crusader93",
    author_email="squadron314@gmail.com",
    description=("A simple app for creating QR codes created on Python."),
    license="BSD",
    keywords="Simple QR Code",
    url="https://github.com/Crusader93/Simple-QR-Code",
    packages=['Simple_QR_Code'],
    package_dir={'Simple_QR_Code': 'src'},
    install_requires=['qrcode'],
)