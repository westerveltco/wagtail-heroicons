# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project attempts to adhere to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<!--
## [${version}]
### Added - for new features
### Changed - for changes in existing functionality
### Deprecated - for soon-to-be removed features
### Removed - for now removed features
### Fixed - for any bug fixes
### Security - in case of vulnerabilities
[${version}]: https://github.com/westerveltco/wagtail-heroicons/releases/tag/v${version}
-->

## [Unreleased]

## [0.2.2]

### Fixed

-   Fixed a bug where the icons were registered incorrectly and thus not able to be rendered by Django's `render_to_string` function. Reported by @seb-b in #58.

## [0.2.1]

### Fixed

-   Fixed a bug where the icons being registered by the wagtail hook were not being found.

## [0.2.0]

### Added

-   Now using `django-twc-package` as as package template.

### Changed

-   Now using `nox` for testing.
-   Build script has been moved from inside the package to the root of the repository.
-   Added link to MIT license in all SVG files and split the license and Refactoring UI Inc. copyright information into separate lines.
-   Icon registration has been simplified to just getting a list of the icon files under the `heroicons` template directory.
-   Application template directory containing icons has been renamed to match the package name.

### Removed

-   Dropped support for Python 3.7.
-   Removed all build scripts and related methods from package.
-   Removed `icons.py` and associated tests.

## [0.1.3]

-   Fixed a TypeError when attempting to use the package; the `Heroicon` dataclass was adding a `Path` object to the list of icons in the `register_icons` Wagtail hook instead of a string. Reported by @ReijerTheCoder in #40 and fixed in #41.

## [0.1.2]

### Changed

-   Add the MIT license and Refactoring UI Inc. copyright information to all SVG files.

## [0.1.1]

### Changed

-   Refactored the internals of the package to use a `Heroicon` dataclass instead of a `list` of icon names.

### Fixed

-   Add try/except block for `hooks` import from `wagtail.core` to `wagtail` to fix a deprecation warning.

## [0.1.0]

Initial release!

### Added

-   Build script:
    -   Download Heroicons from NPM and copy to `templates` folder
    -   Edit SVG files to add correct `id` attribute
    -   Edit and build the icon registry in `icons.py`
-   Initial documentation

[unreleased]: git@github.com:joshuadavidthomas/wagtail-heroicons/compare/v0.2.2...HEAD
[0.1.0]: https://github.com/joshuadavidthomas/wagtail-heroicons/releases/tag/v0.1.0
[0.1.1]: https://github.com/joshuadavidthomas/wagtail-heroicons/releases/tag/v0.1.1
[0.1.2]: https://github.com/joshuadavidthomas/wagtail-heroicons/releases/tag/v0.1.2
[0.1.3]: https://github.com/joshuadavidthomas/wagtail-heroicons/releases/tag/v0.1.3
[0.2.0]: git@github.com:joshuadavidthomas/wagtail-heroicons/releases/tag/v0.2.0
[0.2.1]: git@github.com:joshuadavidthomas/wagtail-heroicons/releases/tag/v0.2.1
[0.2.2]: git@github.com:joshuadavidthomas/wagtail-heroicons/releases/tag/v0.2.2
