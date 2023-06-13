"""create alunos table

Revision ID: d0bbf8f1c409
Revises: 8e04b6e1a99f
Create Date: 2023-06-06 23:06:36.624769

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0bbf8f1c409'
down_revision = '8e04b6e1a99f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'alunos',
        sa.Column('cpf', sa.String(length=11), primary_key=True),
        sa.Column('nome', sa.String(length=50), nullable=False),
        sa.Column('telefone', sa.String(length=11), nullable=False),
        sa.Column('endereco', sa.String(length=100), nullable=False),
        sa.Column('ativo', sa.Boolean, nullable=False),
        sa.Column('cod_curso', sa.Integer, sa.ForeignKey('cursos.cod_curso', ondelete='CASCADE'), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('alunos')
