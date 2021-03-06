"""empty message

Revision ID: 195bb6ea49db
Revises: 
Create Date: 2022-01-26 15:23:18.751541

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '195bb6ea49db'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alimento',
    sa.Column('create_time', sa.String(), nullable=True),
    sa.Column('update_time', sa.String(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=20), nullable=True),
    sa.Column('descricao', sa.String(length=20), nullable=True),
    sa.Column('quantidade', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cliente',
    sa.Column('create_time', sa.String(), nullable=True),
    sa.Column('update_time', sa.String(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cpf', sa.String(length=15), nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('senha', sa.String(length=20), nullable=True),
    sa.Column('telefone', sa.String(length=20), nullable=True),
    sa.Column('endereco', sa.String(length=70), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('funcionario',
    sa.Column('create_time', sa.String(), nullable=True),
    sa.Column('update_time', sa.String(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('senha', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('produto',
    sa.Column('create_time', sa.String(), nullable=True),
    sa.Column('update_time', sa.String(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=20), nullable=True),
    sa.Column('descricao', sa.String(length=20), nullable=True),
    sa.Column('preco', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('carrinho',
    sa.Column('create_time', sa.String(), nullable=True),
    sa.Column('update_time', sa.String(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('precoTotal', sa.Float(), nullable=True),
    sa.Column('id_cliente', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_cliente'], ['cliente.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('association',
    sa.Column('carrinho_id', sa.Integer(), nullable=True),
    sa.Column('produto_id', sa.Integer(), nullable=True),
    sa.Column('quantidade_produto', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['carrinho_id'], ['carrinho.id'], ),
    sa.ForeignKeyConstraint(['produto_id'], ['produto.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('association')
    op.drop_table('carrinho')
    op.drop_table('produto')
    op.drop_table('funcionario')
    op.drop_table('cliente')
    op.drop_table('alimento')
    # ### end Alembic commands ###
