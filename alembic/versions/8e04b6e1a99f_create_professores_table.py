"""create professores table

Revision ID: 8e04b6e1a99f
Revises: c2d64aaba2dd
Create Date: 2023-06-06 19:06:35.462549

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e04b6e1a99f'
down_revision = 'c2d64aaba2dd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'professores',
        sa.Column('cpf', sa.String(length=11), primary_key=True),
        sa.Column('nome', sa.String(length=50), nullable=False),
        sa.Column('telefone', sa.String(length=11), nullable=False),
        sa.Column('endereco', sa.String(length=100), nullable=False),
        sa.Column('data_contratacao', sa.DateTime, nullable=False),
        sa.Column('salario', sa.Float, nullable=False),
        sa.Column('ativo', sa.Boolean, nullable=False),
        sa.Column('cod_curso', sa.Integer, sa.ForeignKey('cursos.cod_curso', ondelete='CASCADE'), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('professores')
