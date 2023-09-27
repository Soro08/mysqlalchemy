import click
from models import m_c, engine, session
from models import (
    enregistrer_utilisateur,
    authentification_initiale,
    auto_login,
    logout_user,
    admin_required,
)
from views import get_user_data, get_user_login_data


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
def create():
    if admin_required(session):
        name, lastname, password, role = get_user_data()
        enregistrer_utilisateur(session, name, lastname, password, role=role)

        print(f"create new user {name} ")
        session.close()
    else:
        print("You don")


@click.command()
def login():
    if auto_login(session):
        pass
    else:
        name, password = get_user_login_data()
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
