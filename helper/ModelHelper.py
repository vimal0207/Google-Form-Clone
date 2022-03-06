from django.db import models
from django.contrib import admin

from django.db import connection, migrations, models
from django.db.migrations.executor import MigrationExecutor

def create_table(table_name, model_fields, app_label):
    class Migration(migrations.Migration):
        initial = True
        dependencies = []
        operations = [
            migrations.CreateModel(
                name=table_name,
                fields=[
                    ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ] + [(k, field) for k,field in model_fields.items()],
                options={
                    'db_table': table_name,
                },
            ),
        ]
    executor = MigrationExecutor(connection)
    migration = Migration(table_name, app_label)
    with connection.schema_editor(atomic=True) as schema_editor:
        migration.apply(executor._create_project_state(), schema_editor)

def create_model(name, fields=None, app_label='', module='', options=None, admin_opts=None):
    """
    Create specified model
    """
    class Meta:
        # Using type('Meta', ...) gives a dictproxy error during model creation
        pass

    if app_label:
        # app_label must be set using the Meta inner class
        setattr(Meta, 'app_label', app_label)

    # Update Meta with any options that were provided
    if options is not None:
        for key, value in options.items():
            setattr(Meta, key, value)

    # Set up a dictionary to simulate declarations within a class
    attrs = {'__module__': module, 'Meta': Meta}

    # Add in any fields that were provided
    if fields:
        attrs.update(fields)

    # Create the class, which automatically triggers ModelBase processing
    model = type(name, (models.Model,), attrs)

    # Create an Admin class if admin options were provided
    if admin_opts is not None:
        class Admin(admin.ModelAdmin):
            pass
        # for key, value in admin_opts:
        #     setattr(Admin, key, value)
        admin.site.register(model, Admin)

    return model