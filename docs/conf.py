project = 'family-tree-customer-support'
author = 'family-tree-customer-support'
release = '1.0'

# Extensions
extensions = [
    'sphinx_sitemap',
]

# Paths
templates_path = ['_templates']
exclude_patterns = []

# Theme
html_theme = 'alabaster'
html_static_path = ['_static']

# Custom JS & Favicon
html_js_files = ['chatbot.js']  # chatbot widget
html_favicon = '_static/favicon.png'

{% extends "!layout.html" %}

{% block extrahead %}
{{ super() }}

<!-- Google Search Console Verification -->
<meta name="google-site-verification" content="9dhv1CKAmbsyuggEJcSyXa5WBo_Y90CvjKwi462oEYs" />

<!-- Bing Webmaster Verification -->
<meta name="msvalidate.01" content="59FDF959BB464F16C29E6DC18623CEF1" />

{% endblock %}


# Base URL for sitemap
html_baseurl = 'https://familytree-guide.readthedocs.io/en/latest/'
