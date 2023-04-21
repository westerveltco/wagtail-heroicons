# Wagtail Heroicons

[![PyPI](https://img.shields.io/pypi/v/wagtail-heroicons)](https://pypi.org/project/wagtail-heroicons/) [![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/joshuadavidthomas/wagtail-heroicons/test.yml?branch=main)](https://github.com/joshuadavidthomas/wagtail-heroicons/actions/workflows/test.yml)

Add [Heroicons](https://heroicons.com/) to the Wagtail admin.

Note: SVG icons within the Wagtail admin are a relatively new feature in Wagtail, and the hook used within this package is not publically documented. As such, the API provided by Wagtail may change and cause breakage within this package. See Issue [#6107](https://github.com/wagtail/wagtail/issues/6107) and PR [#6028](https://github.com/wagtail/wagtail/pull/6028) in the Wagtail repository for more information.

## Installation

Install the package using pip:

```bash
pip install wagtail-heroicons
```

Add `wagtail_heroicons` to your `INSTALLED_APPS` setting in your `settings.py` file:

```python
INSTALLED_APPS = [
    ...
    'wagtail_heroicons',
]
```

## Usage

All icons follow the following naming convention: `heroicons-<name>-<style>`.

For example, the [solid Adjustments icon](https://heroicons.com/#adjustments-sm-btn) would be `heroicons-adjustments-solid`.

To see all available icons, names and styles, visit the [Heroicons website](https://heroicons.com/).

See the [Wagtail documentation](https://docs.wagtail.org/en/latest/search.html?q=icon) for more information on using icons in Wagtail.

## License

This package is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Heroicons are licensed under the MIT License and are Copyright (c) 2020 Refactoring UI Inc.