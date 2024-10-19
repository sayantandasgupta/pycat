import click

@click.command()
@click.argument('file_paths', nargs=-1, type=click.Path(exists=True))
def main(file_paths):
    for file_path in file_paths:
        with open(file_path, 'r') as f:
            click.echo(f.read())