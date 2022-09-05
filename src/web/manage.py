from flask.cli import FlaskGroup

from project import app, db, UserDocker


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    db.session.add(UserDocker(email="michael@mherman.org"))
    db.session.commit()


if __name__ == "__main__":
    cli()
