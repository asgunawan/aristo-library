from pathlib import Path
import re

from docx import Document


def normalize_markdown(text: str) -> str:
    text = text.replace("\r\n", "\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def convert_file(docx_path: Path) -> tuple[Path, int]:
    doc = Document(str(docx_path))
    lines = []

    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            lines.append("")
            continue

        style_name = para.style.name.lower() if para.style and para.style.name else ""
        if style_name.startswith("heading"):
            level_match = re.search(r"(\d+)", style_name)
            level = int(level_match.group(1)) if level_match else 1
            level = max(1, min(level, 6))
            lines.append(f"{'#' * level} {text}")
        elif "list" in style_name or style_name.startswith("bullet"):
            lines.append(f"- {text}")
        else:
            lines.append(text)

    markdown = "\n".join(lines)
    markdown = normalize_markdown(markdown)

    md_path = docx_path.with_suffix(".md")
    md_path.write_text(markdown, encoding="utf-8")
    return md_path, 0


def main() -> None:
    root = Path.cwd()
    skip_dirs = {".git", ".venv", "venv", "node_modules", "scripts"}

    docx_files = []
    for path in root.rglob("*.docx"):
        if any(part in skip_dirs for part in path.parts):
            continue
        docx_files.append(path)
    docx_files.sort()

    converted = []
    for docx in docx_files:
        md_file, warning_count = convert_file(docx)
        converted.append((docx, md_file, warning_count))

    print(f"CONVERTED_COUNT={len(converted)}")
    for src, dst, warnings in converted:
        print(f"{src} => {dst} | conversion_messages={warnings}")


if __name__ == "__main__":
    main()
