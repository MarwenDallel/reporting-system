#!python
import dis
from nbconvert import PythonExporter


class Extractor:
    def __init__(self) -> None:
        self.instructions = None
        self.source = None
        self.meta = None
        self.python_exporter = PythonExporter()
        self.imports = {"IMPORT_FROM": list(), "IMPORT_NAME": list()}

    def extract(self, notebook_path):
        (self.source, self.meta) = self.python_exporter.from_filename(notebook_path)
        return self.source

    def save_script(self, dest_path):
        with open(dest_path, "w") as outfile:
            outfile.writelines(self.source)

    def get_imports(self, source):
        self.instructions = dis.get_instructions(source)
        for instruction in self.instructions:
            if "IMPORT_NAME" in instruction.opname:
                self.imports["IMPORT_NAME"].append(instruction.argval)
            elif "IMPORT_FROM" in instruction.opname:
                self.imports["IMPORT_FROM"].append(instruction.argval)
        return self.imports


def main():
    notebook_path = input("Enter notebook path: ")
    extractor = Extractor()
    source = extractor.extract(notebook_path)
    imports = extractor.get_imports(source)
    print(imports)


if __name__ == "__main__":
    main()
