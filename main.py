from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

import yaml


@dataclass
class Parameter:
    name: str
    type: Optional[str] = "string"
    default_value: Optional[str] = None
    display_name: Optional[str] = None
    allowed_values: Optional[List[str]] = None


def load_pipeline_template(template_path: Path) -> list[Parameter]:
    file_path = template_path
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

    return parameters


def main():
    parameters = load_pipeline_template(
        Path("sample_templates/docker-build-and-push.yml")
    )
    print(parameters)
    pass


if __name__ == "__main__":
    main()
