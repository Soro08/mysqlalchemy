import click
from models import m_c, engine, session
from models import (
    enregistrer_utilisateur,
    authentification_initiale,
    auto_login,
    logout_user,
)


@click.group()
def cli():
    pass


@cli.group()
def user():
    pass


@cli.group()
def display():
    pass


@cli.group()
def delete():
    pass


@click.command()
@click.option("-n", "--name", prompt="Your name: ", help="Name to greet")
@click.option("-n", "--lastname", prompt="Your last name: ", help="Last name to greet")
@click.option("-n", "--password", prompt="Your password: ", help="password")
@click.option(
    "-n", "--role", prompt="Your role (admin, student, client): ", help="role to greet"
)
def create(name, lastname, password, role):
    enregistrer_utilisateur(session, name, lastname, password, role=role)

    print(f"create new user {name} ")
    session.close()


@click.command()
def login():
    if auto_login(session):
        pass
    else:
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        authentification_initiale(session, name, password)


@click.command()
def logout():
    logout_user()


@click.command()
def user_list():
    print("display new user")


user.add_command(create)
user.add_command(login)
user.add_command(logout)
display.add_command(user_list)

if __name__ == "__main__":
    # m_c.create_all(engine)
    cli()
