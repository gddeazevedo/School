"""create cursos_disciplinas table

Revision ID: aaa917913bd7
Revises: 72cdd124af50
Create Date: 2023-06-06 23:14:20.485917

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aaa917913bd7'
down_revision = '72cdd124af50'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'cursos_disciplinas',
        sa.Column(
            'cod_curso',
            sa.Integer,
            sa.ForeignKey('cursos.cod_curso', ondelete='CASCADE'),
            primary_key=True
        ),
        sa.Column(
            'cod_disciplina',
            sa.Integer,
            sa.ForeignKey('disciplinas.cod_disciplina', ondelete='CASCADE'),
            primary_key=True
        )
    )


def downgrade() -> None:
    op.drop_table('cursos_disciplinas')
