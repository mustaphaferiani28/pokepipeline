from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Pokemon, Type, Ability, PokemonStat
from utils import fetch_pokemon, transform_pokemon

def main():
    engine = create_engine("sqlite:///pokedb.sqlite", echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for i in range(1, 21):
        raw = fetch_pokemon(i)
        data = transform_pokemon(raw)

        pokemon = session.get(Pokemon, data["id"])
        if not pokemon:
            pokemon = Pokemon(id=data["id"], name=data["name"], height=data["height"], weight=data["weight"], base_experience=data["base_experience"])
            session.add(pokemon)

        pokemon.types.clear()
        for t_name in data["types"]:
            type_obj = session.query(Type).filter_by(name=t_name).first()
            if not type_obj:
                type_obj = Type(name=t_name)
                session.add(type_obj)
            pokemon.types.append(type_obj)

        pokemon.abilities.clear()
        for a_name in data["abilities"]:
            ability_obj = session.query(Ability).filter_by(name=a_name).first()
            if not ability_obj:
                ability_obj = Ability(name=a_name)
                session.add(ability_obj)
            pokemon.abilities.append(ability_obj)

        pokemon.stats.clear()
        for stat_name, stat_value in data["stats"].items():
            stat_obj = PokemonStat(stat_name=stat_name, stat_value=stat_value)
            pokemon.stats.append(stat_obj)

        session.commit()

    session.close()
    print("Pipeline terminé — données enregistrées dans pokedb.sqlite")

if __name__ == "__main__":
    main()
