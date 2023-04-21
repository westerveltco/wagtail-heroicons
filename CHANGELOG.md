# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.2] - 2023-04-21

### Changed

- Add the MIT license and Refactoring UI Inc. copyright information to all SVG files.

## [0.1.1] - 2023-04-21

### Changed

- Refactored the internals of the package to use a `Heroicon` dataclass instead of a `list`
  of icon names.

### Fixed

- Add try/except block for `hooks` import from `wagtail.core` to `wagtail` to fix a 
  deprecation warning.

## [0.1.0] - 2022-08-11

Initial release!

### Added

- Build script:
  - Download Heroicons from NPM and copy to `templates` folder
  - Edit SVG files to add correct `id` attribute
  - Edit and build the icon registry in `icons.py`
- Initial documentation

[unreleased]: https://github.com/joshuadavidthomas/wagtail-heroicons/compare/v0.1.2...HEAD
[0.1.2]: https://github.com/joshuadavidthomas/wagtail-heroicons/releases/tag/v0.1.2
[0.1.1]: https://github.com/joshuadavidthomas/wagtail-heroicons/releases/tag/v0.1.1
[0.1.0]: https://github.com/joshuadavidthomas/wagtail-heroicons/releases/tag/v0.1.0
