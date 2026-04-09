import click
from core.pipeline import process_code

@click.command()
@click.argument('file', type=click.Path(exists=True))
@click.option('--lang', default=None, help="Programming language (optional)")
def main(file, lang):
    with open(file, 'r') as f:
        code = f.read()

    result = process_code(code, lang)
    print("\n=== CLEAN CODE OUTPUT ===\n")
    print(result)

if __name__ == "__main__":
    main()