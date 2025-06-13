"""add foreign key to onboarding

Revision ID: a939915d2646
Revises: c83fb3419d7a
Create Date: 2025-06-13 23:05:39.733301

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a939915d2646'
down_revision = 'c83fb3419d7a'
branch_labels = None
depends_on = None


def upgrade():
    # Use batch_alter_table for SQLite compatibility
    with op.batch_alter_table('onboardings') as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            'fk_onboardings_employee_id_employees',
            'employees',
            ['employee_id'],
            ['id']
        )


def downgrade():
    with op.batch_alter_table('onboardings') as batch_op:
        batch_op.drop_constraint('fk_onboardings_employee_id_employees', type_='foreignkey')
        batch_op.drop_column('employee_id')
