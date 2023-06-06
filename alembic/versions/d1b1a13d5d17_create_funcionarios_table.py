"""create funcionarios table

Revision ID: d1b1a13d5d17
Revises: b48ed2ae56cc
Create Date: 2023-06-05 22:15:43.620577

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1b1a13d5d17'
down_revision = 'b48ed2ae56cc'
branch_labels = None
depends_on = None



def upgrade() -> None:
    op.create_table(
        'funcionarios',
        sa.Column('cpf', sa.String(length=11), primary_key=True),
        sa.Column('nome', sa.String(length=50), nullable=False),
        sa.Column('endereco', sa.String(100), nullable=False),
        sa.Column('salario', sa.Float, nullable=False),
        sa.Column('cod_setor', sa.Integer, sa.ForeignKey('setores.cod_setor'))
    )


def downgrade() -> None:
    op.drop_table('funcionarios')
