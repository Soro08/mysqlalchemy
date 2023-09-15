import click


@click.command()
@click.option('-n', '--name', prompt='Your name', help='Name to greet')
@click.option('-n', '--firstname', prompt='Your firstname', help='firstname to greet')
def main(name, firstname):
    """Greets a user who gives his name as input"""
    click.echo(f'Hello {name} {firstname}!')
    
if __name__ == '__main__':
    main()