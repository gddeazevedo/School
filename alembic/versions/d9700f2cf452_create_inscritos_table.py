"""create inscritos table

Revision ID: d9700f2cf452
Revises: aaa917913bd7
Create Date: 2023-06-06 23:16:43.132031

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9700f2cf452'
down_revision = 'aaa917913bd7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'inscritos',
        sa.Column(
            'cod_disciplina',
            sa.Integer,
            sa.ForeignKey('disciplinas.cod_disciplina', ondelete='CASCADE'),
            primary_key=True
        ),
        sa.Column(
            'cpf_aluno',
            sa.String(length=11),
            sa.ForeignKey('alunos.cpf', ondelete='CASCADE'),
            primary_key=True
        ),
        sa.Column('nota', sa.Float, nullable=True),
        sa.Column('vez', sa.Integer, nullable=False, default=1)
    )


def downgrade() -> None:
    op.drop_table('inscritos')
