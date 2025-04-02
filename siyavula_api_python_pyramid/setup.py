import os
from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.txt")) as f:
    README = f.read()
with open(os.path.join(here, "CHANGES.txt")) as f:
    CHANGES = f.read()

requires = [
    "plaster_pastedeploy",
    "pyramid",
    "pyramid_jinja2",
    "pyramid_debugtoolbar",
    "waitress",
]

tests_require = [
    "WebTest >= 1.3.1",  # py3 compat
    "pytest >= 3.7.4",
    "pytest-cov",
]

setup(
    name="siyavula_api_python_pyramid",
    version="0.0",
    description="siyavula-api-python-pyramid",
    long_description=README + "\n\n" + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author="",
    author_email="",
    url="",
    keywords="web pyramid pylons",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        "testing": tests_require,
    },
    install_requires=requires,
    entry_points={
        "paste.app_factory": [
            "main = siyavula_api_python_pyramid:main",
        ],
    },
)
