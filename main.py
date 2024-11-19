from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional
from markdowngenerator import MarkdownGenerator

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


def generate_markdown_table(parameters: list[Parameter]) -> None:
    with MarkdownGenerator(filename="output.md", enable_write=False) as output_doc:
        output_doc.addHeader(1, "Hello there!")
        output_doc.writeTextLine(f'{output_doc.addBoldedText("This is just a test.")}')
        output_doc.addHeader(2, "Second level header.")
        table = [
            {"Column1": "col1row1 data", "Column2": "col2row1 data"},
            {"Column1": "col1row2 data", "Column2": "col2row2 data"},
        ]

        output_doc.addTable(dictionary_list=table)
        output_doc.writeTextLine("Ending the document....")


def main():
    parameters = load_pipeline_template(
        Path("sample_templates/docker-build-and-push.yml")
    )

    generate_markdown_table(parameters)

    pass


if __name__ == "__main__":
    main()
