import click
from models import m_c, Utilisateur, engine, session
from sqlalchemy import insert
from sqlalchemy.orm import sessionmaker

@click.group()
def cli():
    pass


@cli.group()
def create():
    pass


@cli.group()
def display():
    pass

@cli.group()
def delete():
    pass


@click.command()
@click.option('-n', '--name', prompt='Your name: ', help='Name to greet')
@click.option('-n', '--lastname', prompt='Your last name: ', help='Last name to greet')
@click.option('-n', '--role', prompt='Your role (admin, student, client): ', help='role to greet')
def user(name, lastname, role):

    nouvel_utilisateur = Utilisateur(namenom = name, lastname=lastname, role=role)
    session.add(nouvel_utilisateur)
    session.commit()
    print(f"create new user {name} ")
    session.close()

    
@click.command()
def user_list():
    print("display new user")

create.add_command(user)
display.add_command(user_list)
    
if __name__ == "__main__":
    m_c.create_all(engine)
    cli()