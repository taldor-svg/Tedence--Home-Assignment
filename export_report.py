from pathlib import Path
import base64

import nbformat
from nbconvert import HTMLExporter
from nbconvert.preprocessors import ExecutePreprocessor


NOTEBOOK = Path("/app/notebooks/template.ipynb")
OUTPUT_DIR = Path("/app/output")


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    notebook = nbformat.read(NOTEBOOK, as_version=4)
    executor = ExecutePreprocessor(timeout=600, kernel_name="python3")
    executor.preprocess(notebook, {"metadata": {"path": str(NOTEBOOK.parent)}})

    figure_number = 0
    for cell_number, cell in enumerate(notebook.cells, start=1):
        for output_number, output in enumerate(cell.get("outputs", []), start=1):
            image = output.get("data", {}).get("image/png")
            if image is None:
                continue
            figure_number += 1
            filename = f"figure-{figure_number:02d}-cell-{cell_number:02d}.png"
            (OUTPUT_DIR / filename).write_bytes(base64.b64decode(image))
            print(f"Saved {filename}")

    if figure_number == 0:
        raise RuntimeError("Notebook execution produced no PNG visualizations")

    html, _ = HTMLExporter().from_notebook_node(notebook)
    report_path = OUTPUT_DIR / "template.html"
    report_path.write_text(html, encoding="utf-8")
    print(f"Saved {report_path} with {figure_number} embedded visualizations")


if __name__ == "__main__":
    main()
