from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

import yaml


@dataclass
class Parameter:
    name: str
    type: str
    default_value: str
    display_name: str
    allowed_values: Optional[List[str]] = None


def main():
    file_path = Path("sample_templates/docker-build-and-push.yml")
    data = yaml.safe_load(file_path.read_text())

    parameters = []

    for parameter in data["parameters"]:
        parameters.append(
            Parameter(
                name=parameter.get("name"),
                type=parameter.get("type"),
                default_value=parameter.get("default"),
                display_name=parameter.get("displayName"),
                allowed_values=parameter.get("values"),
            )
        )

    pass


if __name__ == "__main__":
    main()
