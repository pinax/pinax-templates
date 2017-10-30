from setuptools import find_packages, setup


setup(
    author="",
    author_email="",
    description="",
    name="pinax-templates",
    version="0.1",
    url="http://github.com/pinax/pinax-templates/",
    license="MIT",
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    test_suite="runtests.runtests",
    install_requires=[
        "Django>=1.8",
        "django-bootstrap-form>=3.0.0"
    ],
    tests_require=[
    ],
    extras_require={
        "pytest": ["pytest", "pytest-django"]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False
)
