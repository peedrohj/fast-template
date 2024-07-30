from typing import List

from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from setup.app import BASE
from setup.config import CONFIG
from alembic import context

import importlib
import os
import sys

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config
config.set_main_option('sqlalchemy.url', CONFIG.DB_SQLITE_URL())



# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = BASE.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

def import_all_models(app_names: List[str]):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(current_dir)

    sys.path.append(base_dir)

    for app_name in app_names:
        app_path = os.path.join(base_dir, app_name)

        if not os.path.isdir(app_path):
            return

        models_path = os.path.join(app_path, "infra", 'models')
        if not os.path.isdir(models_path):
            return

        for file_name in os.listdir(models_path):
            if not file_name.endswith('.py') and file_name != '__init__.py':
                return

            module_name = file_name[:-3]
            module_path = f"{app_name}.infra.models.{module_name}"

            try:
                importlib.import_module(module_path)
                print(f"Imported {module_path}")
            except Exception as e:
                print(f"Failed to import {module_path}: {e}")


import_all_models(app_names=CONFIG.APP_NAMES)


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
