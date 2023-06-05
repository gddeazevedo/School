"""create setores table

Revision ID: ef654b3ddf76
Revises: 
Create Date: 2023-06-05 18:42:32.956922

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef654b3ddf76'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'setores',
        sa.Column('cod_setor', sa.Integer, primary_key=True),
        sa.Column('nome', sa.String(length=50), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('setores')
