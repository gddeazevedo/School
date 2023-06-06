"""create cursos table

Revision ID: c2d64aaba2dd
Revises: d1b1a13d5d17
Create Date: 2023-06-05 22:18:42.888762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2d64aaba2dd'
down_revision = 'd1b1a13d5d17'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'cursos',
        sa.Column('cod_curso', sa.Integer, primary_key=True),
        sa.Column('nome', sa.String(length=50), nullable=False),
        sa.Column('ano_inicio', sa.DateTime, nullable=False)
    )


def downgrade() -> None:
    op.drop_table('cursos')
