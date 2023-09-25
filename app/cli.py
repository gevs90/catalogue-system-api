import click

from app.services.auth import AuthService
from app.schemas.auth import CreateUserSchema
from app.database.session import create_session
from app.version import __version__


@click.group(invoke_without_command=True)
@click.option("--version", is_flag=True, help="Show package version")
def main(version: bool) -> None:
    """Console Command Admin!"""
    if version:
        click.echo("Version: " + __version__)


@main.command()
@click.option("--name", type=str, help="User name")
@click.option("--email", type=str, help="Email")
@click.option("--password", type=str, help="Password")
def admin(name: str, email: str, password: str) -> None:
    """Create new user.
    Example:
        create_user admin --name 'Administrator' --email admin@admin.text --password admin1234
    """
    click.echo("Creating user admin !" + name)
    user = CreateUserSchema(name=name, email=email,
                            password=password, role="admin")
    session = next(create_session())
    AuthService(session).create_user(user)
    click.echo("User admin created at!")
