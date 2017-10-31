![](http://pinaxproject.com/pinax-design/patches/blank.svg)

# Pinax Templates

[![](https://img.shields.io/pypi/v/pinax-templates.svg)](https://pypi.python.org/pypi/pinax-templates/)
[![](https://img.shields.io/badge/license-MIT-blue.svg)](https://pypi.python.org/pypi/pinax-templates/)

[![Codecov](https://img.shields.io/codecov/c/github/pinax/pinax-templates.svg)](https://codecov.io/gh/pinax/pinax-templates)
[![CircleCI](https://circleci.com/gh/pinax/pinax-templates.svg?style=svg)](https://circleci.com/gh/pinax/pinax-templates)
![](https://img.shields.io/github/contributors/pinax/pinax-templates.svg)
![](https://img.shields.io/github/issues-pr/pinax/pinax-templates.svg)
![](https://img.shields.io/github/issues-pr-closed/pinax/pinax-templates.svg)

[![](http://slack.pinaxproject.com/badge.svg)](http://slack.pinaxproject.com/)


## General

This package includes more than just application templates, but some general
purpose templates and a base template for your project to extend.

### Full Templates

These include a full base template, a template that provides side navigation,
and a couple error templates that Django will render on a `500` or `404`
response.

#### `base.html`

This is the parent of all other templates.  Everything eventually extends `base.html`
unless you add a second base template in your project.

##### Blocks

* `head_title_base` - the block inside the `<title>` element, defaults to `Site.name`
  * `head_title` - inside the `head_title_base` allowing for per page addition without having to use `block.super`
* `viewport`
* `styles`
* `html5shim`
* `extra_head_base`
  * `extra_head`
* `body_class_base`
  * `body_class`
* `body_id`
* `body_extra_attributes`
* `topbar_base`
  * `topbar`
    * `site_brand`
    * `nav`
    * `account_bar`
* `body_base`
  * `content_left`
  * `messages`
  * `body`
  * `content_right`
* `footer_base`
  * `footer`
* `scripts`
* `extra_body_base`
  * `extra_body`

#### `subnav_base.html`

This template extends `site_base.html` which is defined in your project to extend
and customize the `base.html` template discussed above.  It defines the `body`
block and adds to it the following blocks:

* `subnav`
* `content`


#### `404.html`

#### `500.html`

### Fragments

#### `_account_bar.html`

#### `_messages.html`

#### `_nav.html`

#### `pagination/_pagination.html`


## Django User Accounts

## Pinax Announcements

## Pinax Blog

## Pinax Cohorts

## Pinax Documents

## Pinax Invitations

## Pinax Likes

## Pinax Messages

## Pinax Notifications

## Pinax Stripe


---

Pinax
------

Pinax is an open-source platform built on the Django Web Framework. It is an ecosystem of reusable Django apps, themes, and starter project templates.

This collection can be found at http://pinaxproject.com.


Running the Tests
-------------------

```
$ pip install detox
$ detox
```


Documentation
---------------

The `pinax-templates` documentation is currently under construction. If you would like to help us write documentation, please join our Pinax Project Slack team and let us know! The Pinax documentation is available at http://pinaxproject.com/pinax/.


Contribute
----------------

See this blog post http://blog.pinaxproject.com/2016/02/26/recap-february-pinax-hangout/ including a video, or our How to Contribute (http://pinaxproject.com/pinax/how_to_contribute/) section for an overview on how contributing to Pinax works. For concrete contribution ideas, please see our Ways to Contribute/What We Need Help With (http://pinaxproject.com/pinax/ways_to_contribute/) section.

In case of any questions we recommend you join our Pinax Slack team (http://slack.pinaxproject.com) and ping us there instead of creating an issue on GitHub. Creating issues on GitHub is of course also valid but we are usually able to help you faster if you ping us in Slack.

We also highly recommend reading our Open Source and Self-Care blog post (http://blog.pinaxproject.com/2016/01/19/open-source-and-self-care/).


Code of Conduct
----------------

In order to foster a kind, inclusive, and harassment-free community, the Pinax Project has a code of conduct, which can be found here  http://pinaxproject.com/pinax/code_of_conduct/. We ask you to treat everyone as a smart human programmer that shares an interest in Python, Django, and Pinax with you.


Pinax Project Blog and Twitter
--------------------------------

For updates and news regarding the Pinax Project, please follow us on Twitter at @pinaxproject and check out our blog http://blog.pinaxproject.com.
