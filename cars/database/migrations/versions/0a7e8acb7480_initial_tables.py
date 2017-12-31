"""Initial tables

Revision ID: 0a7e8acb7480
Revises: 
Create Date: 2017-12-31 22:34:41.574013

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '0a7e8acb7480'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'manufacturer',
        sa.Column('id', sa.Integer, nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table(
        'model',
        sa.Column('id', sa.Integer, nullable=False),
        sa.Column('name', sa.Text, nullable=False),
        sa.Column('manufacturer_id', sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(['manufacturer_id'], ['manufacturer.id'], ondelete='CASCADE',
                                name="Ref_model_to_manufacturer"),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    pass
