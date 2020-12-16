#!python
import dis
from collections import defaultdict
from nbconvert import PythonExporter


class Extractor:

    def __init__(self) -> None:
        self.instructions = None
        self.source = None
        self.meta = None
        self.python_exporter = PythonExporter()
        self.imports = defaultdict(list)

    def extract(self, notebook_path: str) -> str:
        (self.source, self.meta) = self.python_exporter.from_filename(notebook_path)
        return self.source

    def save_script(self, dest_path: str) -> None:
        with open(dest_path, "w") as outfile:
            outfile.writelines(self.source)

    def get_imports(self, source: str) -> defaultdict:
        self.instructions = dis.get_instructions(source)
        for instruction in self.instructions:
            if "IMPORT_NAME" in instruction.opname or "IMPORT_FROM" in instruction.opname:
                self.imports[instruction.opname].append(instruction.argval)
        return self.imports


def main() -> None:
    notebook_path: str = input("Enter notebook path: ")
    extractor = Extractor()
    source = extractor.extract(notebook_path)
    imports = extractor.get_imports(source)
    print(imports)


if __name__ == "__main__":
    main()
