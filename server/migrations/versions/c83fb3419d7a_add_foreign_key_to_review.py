"""add foreign key to Review

Revision ID: c83fb3419d7a
Revises: 3677bd348ad5
Create Date: 2025-06-13 22:35:43.293642
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'c83fb3419d7a'
down_revision = '3677bd348ad5'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('reviews') as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer()))
        batch_op.create_foreign_key(
            'fk_reviews_employee_id_employees',
            'employees',
            ['employee_id'],
            ['id']
        )


def downgrade():
    with op.batch_alter_table('reviews') as batch_op:
        batch_op.drop_constraint('fk_reviews_employee_id_employees', type_='foreignkey')
        batch_op.drop_column('employee_id')
