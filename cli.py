import click
from pdf_split_middle import pdf_split_middle


@click.command()
@click.argument('pdf_path')
@click.option('--pdf_output_path', default='split_middle.pdf', help='Path of the new PDF.')
@click.option('--skip_pages', default='', help='A comma separated list of pages to skip.')
@click.option('--shift_middle_percentage', help='Shift the split line. -49 to 49', type=float)
def cli(pdf_path, pdf_output_path, skip_pages, shift_middle_percentage):

	skip_pages = skip_pages.split(',')
	pdf_split_middle(pdf_path, pdf_output_path, skip_pages, shift_middle_percentage)

if __name__ == '__main__':
    cli()