import click
from flask.cli import FlaskGroup
from app import create_app, db

app = create_app()

cli = FlaskGroup(create_app=lambda: app)


@cli.command("init_db")
def init_db():
    """Initialize the database."""
    with app.app_context():
        db.create_all()
        click.echo("Initialized the database.")


@cli.command("drop_db")
def drop_db():
    """Drop all database tables."""
    if click.confirm("Are you sure you want to drop all tables?"):
        with app.app_context():
            db.drop_all()
            click.echo("Dropped all tables.")


if __name__ == "__main__":
    cli()
