import sqlalchemy as sa
import sqlalchemy.orm as so
from Database.Chemicals.models import Compound, CompoundAtom, Atom

hydrogen = Atom(name='Hydrogen', symbol='H')
oxygen = Atom(name='Oxygen', symbol='O')

water = Compound(name='Water',
                 atom_connections=
                 [CompoundAtom(atom=hydrogen, number=1),
                  CompoundAtom(atom=oxygen, number=2),
                  ],)

print(water.atoms)
print(water.formula())

sqlite_engine = sa.create_engine('sqlite:///chemicals.db', echo=True)

with so.Session(bind=sqlite_engine) as session:
    session.add(water)
    session.commit()