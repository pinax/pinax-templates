![](http://pinaxproject.com/pinax-design/patches/pinax-templates.svg)

# Pinax Templates

[![](https://img.shields.io/pypi/v/pinax-templates.svg)](https://pypi.python.org/pypi/pinax-templates/)

[![CircleCi](https://img.shields.io/circleci/project/github/pinax/pinax-templates.svg)](https://circleci.com/gh/pinax/pinax-templates)
[![Codecov](https://img.shields.io/codecov/c/github/pinax/pinax-templates.svg)](https://codecov.io/gh/pinax/pinax-templates)
[![](https://img.shields.io/github/contributors/pinax/pinax-templates.svg)](https://github.com/pinax/pinax-templates/graphs/contributors)
[![](https://img.shields.io/github/issues-pr/pinax/pinax-templates.svg)](https://github.com/pinax/pinax-templates/pulls)
[![](https://img.shields.io/github/issues-pr-closed/pinax/pinax-templates.svg)](https://github.com/pinax/pinax-templates/pulls?q=is%3Apr+is%3Aclosed)

[![](http://slack.pinaxproject.com/badge.svg)](http://slack.pinaxproject.com/)
[![](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Table of Contents

* [About Pinax](#about-pinax)
* [Overview](#overview)
  * [Features](#features)
  * [Supported Pinax Apps](supported-pinax-apps)
  * [Supported Django and Python versions](#supported-django-and-python-versions)
* [Documentation](#documentation)
  * [Installation](#installation)
  * [Usage](#usage)
* [Template Browser](#template-browser)
* [FAQ](#faq)
* [Change Log](#change-log)
* [Contribute](#contribute)
* [Code of Conduct](#code-of-conduct)
* [Connect with Pinax](#connect-with-pinax)
* [License](#license)

## About Pinax

Pinax is an open-source platform built on the Django Web Framework. It is an ecosystem of reusable
Django apps, themes, and starter project templates. This collection can be found at http://pinaxproject.com.

## pinax-templates

### Overview

`pinax-templates` provides semantically-correct templates for Pinax apps.

#### Supported Pinax Apps

* [django-user-accounts](https://github.com/pinax/django-user-accounts)
* [pinax-announcements](https://github.com/pinax/pinax-announcements)
* [pinax-blog](https://github.com/pinax/pinax-blog)
* [pinax-cohorts](https://github.com/pinax/pinax-cohorts)
* [pinax-documents](https://github.com/pinax/pinax-documents)
* [pinax-invitations](https://github.com/pinax/pinax-invitations)
* [pinax-likes](https://github.com/pinax/pinax-likes)
* [pinax-notifications](https://github.com/pinax/pinax-notifications)
* [pinax-stripe](https://github.com/pinax/pinax-stripe)
* [pinax-waitinglist](https://github.com/pinax/pinax-waitinglist)

#### Supported Django and Python versions

Django \ Python | 2.7 | 3.4 | 3.5 | 3.6
--------------- | --- | --- | --- | ---
1.11 |  *  |  *  |  *  |  *  
2.0  |     |  *  |  *  |  *


## Documentation

### Installation

To install pinax-templates:

```shell
$ pip install pinax-templates
```

Add `pinax.templates` to your `INSTALLED_APPS` setting:

```python
INSTALLED_APPS = [
    # other apps
    "pinax.templates",
]
```


### Usage

With pinax-templates installed, all default templates for supported apps are ready for use.

## Template Browser

This project provides a template browser at http://templates.pinaxproject.com.
Browse there to see each Pinax application template collection, dressed up with Bootstrap 4 styling.

On this site, you can browse all the templates in various different states. In
addition there is a source toggle where you can view the template, see what blocks
are defined, and easily copy and paste into your project if you want to override
or customize the template code.

## FAQs

### How do I remove / edit the footer?

### How do I change the styling?

### How do I change the site name?

### How do I add my own scripts?

### How do I change the titles on my pages?


## Change Log

### 2.0.0

* Remove django-user-accounts template tags from pinax-documents templates **Backward incompatible, requires pinax-documents>=1.0.2+**

### 1.0.4

* Add pinax-calendars templates

### 1.0.3

* Add pinax-waitinglist templates

### 1.0.2

* Fix urlname reference for pinax-invitations

### 1.0.1

* Update django>=1.11 in requirements
* Remove pytest from CI
* Add PyPi-compatible docs in setup.py
* Revise trove classifiers
* Improve .gitignore
* Update CI configuration

### 1.0.0

* Initial release


## Contribute

For an overview on how contributing to Pinax works read this [blog post](http://blog.pinaxproject.com/2016/02/26/recap-february-pinax-hangout/)
and watch the included video, or read our [How to Contribute](http://pinaxproject.com/pinax/how_to_contribute/) section.
For concrete contribution ideas, please see our
[Ways to Contribute/What We Need Help With](http://pinaxproject.com/pinax/ways_to_contribute/) section.

In case of any questions we recommend you join our [Pinax Slack team](http://slack.pinaxproject.com)
and ping us there instead of creating an issue on GitHub. Creating issues on GitHub is of course
also valid but we are usually able to help you faster if you ping us in Slack.

We also highly recommend reading our blog post on [Open Source and Self-Care](http://blog.pinaxproject.com/2016/01/19/open-source-and-self-care/).


## Code of Conduct

In order to foster a kind, inclusive, and harassment-free community, the Pinax Project
has a [code of conduct](http://pinaxproject.com/pinax/code_of_conduct/).
We ask you to treat everyone as a smart human programmer that shares an interest in Python, Django, and Pinax with you.


## Connect with Pinax

For updates and news regarding the Pinax Project, please follow us on Twitter [@pinaxproject](https://twitter.com/pinaxproject)
and check out our [Pinax Project blog](http://blog.pinaxproject.com).


## License

Copyright (c) 2012-2018 James Tauber and contributors under the [MIT license](https://opensource.org/licenses/MIT).
