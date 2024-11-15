import click
from pathlib import Path
from pdf_split_middle import pdf_split_middle


@click.command()
@click.argument('pdf_path')
@click.option('--pdf_output_path', default='split_middle.pdf', help='Path of the new PDF.')
@click.option('--skip_pages', default='', help='A comma separated list of pages to skip.')
@click.option('--shift_middle_percentage', default=0, help='Shift the split line. -49 to 49', type=float)
@click.option('--recursive', is_flag=True, default=False, help='Walk through pdf_path directory')
@click.option('--recursive_suffix', default='split', help='Suffix for output pdf file name when using recursive option')

def cli(pdf_path, pdf_output_path, skip_pages, shift_middle_percentage, recursive, recursive_suffix):
    skip_pages = skip_pages.split(',')
    if recursive:
        for path in Path(pdf_path).rglob('*'):
            if path.suffix.lower() == '.pdf':
                output_path = f'{path.parent}/{path.stem}_{recursive_suffix}{path.suffix}'
                pdf_split_middle(path, output_path, skip_pages, shift_middle_percentage)
    else:
        pdf_split_middle(pdf_path, pdf_output_path, skip_pages, shift_middle_percentage)

if __name__ == '__main__':
    cli()
