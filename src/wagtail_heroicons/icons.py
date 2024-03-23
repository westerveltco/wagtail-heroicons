from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import List

from django.utils.functional import classproperty

HeroiconList = List["Heroicon"]


class IconType(Enum):
    OUTLINE = "outline"
    SOLID = "solid"


@dataclass(order=True)
class Heroicon:
    type: IconType
    name: str

    @property
    def path(self) -> Path:
        return Path(f"{self.template_dir}/{self.type.value}/{self.name}.svg")

    @classproperty
    def template_dir(self) -> Path:
        return Path(__file__).parent / "templates" / "heroicons"

    @classmethod
    def get_icons(cls) -> HeroiconList:
        icons: HeroiconList = []

        for icon_type in IconType:
            icons.extend(
                cls(icon_type, icon.stem)
                for icon in Path(f"{cls.template_dir}/{icon_type.value}").glob("*.svg")
            )

        return icons
