from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

pokemon_type = Table(
    "pokemon_type", Base.metadata,
    Column("pokemon_id", Integer, ForeignKey("pokemon.id"), primary_key=True),
    Column("type_id", Integer, ForeignKey("type.id"), primary_key=True),
)

pokemon_ability = Table(
    "pokemon_ability", Base.metadata,
    Column("pokemon_id", Integer, ForeignKey("pokemon.id"), primary_key=True),
    Column("ability_id", Integer, ForeignKey("ability.id"), primary_key=True),
)

class Pokemon(Base):
    __tablename__ = "pokemon"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    height = Column(Integer)
    weight = Column(Integer)
    base_experience = Column(Integer)

    types = relationship("Type", secondary=pokemon_type, back_populates="pokemons")
    abilities = relationship("Ability", secondary=pokemon_ability, back_populates="pokemons")
    stats = relationship("PokemonStat", back_populates="pokemon", cascade="all, delete-orphan")

class Type(Base):
    __tablename__ = "type"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    pokemons = relationship("Pokemon", secondary=pokemon_type, back_populates="types")

class Ability(Base):
    __tablename__ = "ability"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    pokemons = relationship("Pokemon", secondary=pokemon_ability, back_populates="abilities")

class PokemonStat(Base):
    __tablename__ = "pokemon_stat"
    id = Column(Integer, primary_key=True)
    pokemon_id = Column(Integer, ForeignKey("pokemon.id"))
    stat_name = Column(String)
    stat_value = Column(Integer)

    pokemon = relationship("Pokemon", back_populates="stats")
