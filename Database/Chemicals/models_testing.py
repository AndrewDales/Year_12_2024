import sqlalchemy as sa
import sqlalchemy.orm as so
from Database.Chemicals.models import Compound, CompoundAtom, Atom
from Database.Chemicals.create_db import construct_db

# This will delete the current database and construct a new one
construct_db()

hydrogen = Atom(name='Hydrogen', symbol='H')
oxygen = Atom(name='Oxygen', symbol='O')
carbon = Atom(name='Carbon', symbol='C')

### Create the Compound using the atom_connections
# water = Compound(name='Water',
#                  atom_connections=
#                  [CompoundAtom(atom=hydrogen, number=1),
#                   CompoundAtom(atom=oxygen, number=2),
#                   ],)

# Create water and methane using the Compound atoms setter method
water = Compound(name='Water')
water.atoms = [(hydrogen, 2),
               (oxygen, 1),
               ]

methane = Compound(name='Methane')
methane.atoms = [(carbon, 4),
                 (hydrogen, 2),
                 ]

sqlite_engine = sa.create_engine('sqlite:///chemicals.db', echo=True)

# Add compounds to the database - this will automatically also add the atoms and connections
with so.Session(bind=sqlite_engine) as session:
    session.add(water)
    session.add(methane)
    session.commit()

sqlite_engine = sa.create_engine('sqlite:///chemicals.db', echo=False)

# Retrieve data and print out
with so.Session(bind=sqlite_engine) as session:
    stmt = sa.select(Compound).where(Compound.name == "Water")
    water = session.execute(stmt).scalar_one_or_none()

    print('\nTest output')
    print(f'Retrieved compound {water}')
    print(f'Water composition: {water.atoms}')
    print(f'Water formular: {water.formula}')
    hydrogen, number = water.atoms[0]
    print(f'Water contains {number} {hydrogen} atoms')
    print(f'{hydrogen} is contained in these compounds: {hydrogen.compounds}')
    # print(methane.atoms)
    # print(methane.formula())
    #
    # print(hydrogen.compounds)