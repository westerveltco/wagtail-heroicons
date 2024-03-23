# wagtail-heroicons

[![PyPI](https://img.shields.io/pypi/v/wagtail-heroicons)](https://pypi.org/project/wagtail-heroicons/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/wagtail-heroicons)
![Django Version](https://img.shields.io/badge/django-3.2%20%7C%204.2%20%7C%205.0-%2344B78B?labelColor=%23092E20)
![Wagtail Version](https://img.shields.io/badge/wagtail-5.2%20%7C%206.0-%2300676A?labelColor=%232E1F5E)

<!-- https://shields.io/badges -->
<!-- django-3.2 | 4.2 | 5.0-#44B78B -->
<!-- labelColor=%23092E20 -->
<!-- https://shields.io/badges -->
<!-- wagtail-5.2 | 6.0-#00676A -->
<!-- labelColor=%232E1F5E -->

Add [Heroicons](https://heroicons.com/) to the Wagtail admin.

## Requirements

-   Python 3.8, 3.9, 3.10, 3.11, 3.12
-   Django 3.2, 4.2, 5.0
-   Wagtail 5.2, 6.0

## Getting Started

1. Install the package from PyPI:

```bash
python -m pip install wagtail-heroicons
```

2. Add the app to your Django project's `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...,
    "wagtail_heroicons",
    ...,
]
```

## Usage

All icons follow the following naming convention: `heroicons-<name>-<style>`.

For example, the [solid Adjustments icon](https://heroicons.com/#adjustments-sm-btn) would be `heroicons-adjustments-solid`.

To see all available icons, names and styles, visit the [Heroicons website](https://heroicons.com/).

See the [Wagtail documentation](https://docs.wagtail.org/en/latest/search.html?q=icon) for more information on using icons in Wagtail.

## License

`wagtail-heroicons` is licensed under the MIT license. See the [`LICENSE`](LICENSE) file for more information.

Heroicons are licensed under the MIT License and are Copyright (c) 2020 Refactoring UI Inc.
