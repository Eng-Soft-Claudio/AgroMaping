"""create_agriculturalarea_selinux_fix

Revision ID: 2d52dcb0afc1
Revises: 595de6c503ca
Create Date: 2025-06-01 01:06:58.286576

"""

# =======================================================================================================
# --- Importações ---                                                                               #####
# =======================================================================================================


from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import geoalchemy2

# =======================================================================================================
# --- Revisão e Identificadores ---                                                                 #####
# =======================================================================================================

revision: str = '2d52dcb0afc1'
down_revision: Union[str, None] = '595de6c503ca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# =======================================================================================================
# --- Upgrade e Downgrade do Alembic ---                                                            #####
# =======================================================================================================

def upgrade() -> None:
    op.create_table('agriculturalarea',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('geometry', geoalchemy2.types.Geometry(geometry_type='POLYGON', srid=4326, from_text='ST_GeomFromEWKT', name='geometry'), nullable=False),  # pyright: ignore[reportUnknownArgumentType]
    sa.Column('area_hectares', sa.Float(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_agriculturalarea_user_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_agriculturalarea'))
    )
    op.create_index(op.f('ix_agriculturalarea_id'), 'agriculturalarea', ['id'], unique=False)
    op.create_index(op.f('ix_agriculturalarea_name'), 'agriculturalarea', ['name'], unique=False)

def downgrade() -> None:
    op.drop_index(op.f('ix_agriculturalarea_name'), table_name='agriculturalarea')
    op.drop_index(op.f('ix_agriculturalarea_id'), table_name='agriculturalarea')
    op.drop_table('agriculturalarea')