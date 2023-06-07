"""create disciplinas table

Revision ID: 72cdd124af50
Revises: d0bbf8f1c409
Create Date: 2023-06-06 23:08:39.274631

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72cdd124af50'
down_revision = 'd0bbf8f1c409'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'disciplinas',
        sa.Column('cod_disciplina', sa.Integer, primary_key=True),
        sa.Column('nome', sa.String(length=50), nullable=False, unique=True),
        sa.Column(
            'cpf_professor',
            sa.String(length=11),
            sa.ForeignKey('professores.cpf', ondelete='CASCADE')
        )
    )


def downgrade() -> None:
    op.drop_table('disciplinas')
