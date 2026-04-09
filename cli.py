import click
import os
from core.pipeline import process_code

OUTPUT_DIR = "examples/after"


def generate_output_filename(input_path):
    filename = os.path.basename(input_path)

    if "before" in filename:
        return filename.replace("before", "after")
    else:
        name, ext = os.path.splitext(filename)
        return f"{name}_cleaned{ext}"


@click.command()
@click.argument('file', type=click.Path(exists=True))
@click.option('--lang', default=None, help="Programming language (optional)")
def main(file, lang):
    with open(file, 'r') as f:
        code = f.read()

    result = process_code(code, lang)

    print("\n=== CLEAN CODE OUTPUT ===\n")
    print(result)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    output_filename = generate_output_filename(file)
    output_path = os.path.join(OUTPUT_DIR, output_filename)

    with open(output_path, 'w') as f:
        f.write(result)

    print(f"\n✅ Saved automatically to: {output_path}")


if __name__ == "__main__":
    main()
