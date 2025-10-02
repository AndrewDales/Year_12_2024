#from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so


class Base(so.DeclarativeBase):
    pass

class CompoundAtom(Base):
    __tablename__ = 'compound_atoms'
    id: so.Mapped[int] = so.mapped_column(primary_key=True, autoincrement=True)
    compound_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey('compounds.id'))
    atom_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey('atoms.atom_id'))
    number: so.Mapped[int]
    compound: so.Mapped['Compound'] = so.relationship(back_populates='atom_connections')
    atom: so.Mapped['Atom'] = so.relationship(back_populates='compound_connections')

class Compound(Base):
    __tablename__ = 'compounds'
    id: so.Mapped[int] = so.mapped_column(primary_key=True, autoincrement=True)
    # m_formula: so.Mapped[str]
    # formula: so.Mapped[str]
    name: so.Mapped[str]
    # smiles: so.Mapped[str]
    # mr: so.Mapped[float]
    atom_connections: so.Mapped[list['CompoundAtom']] = so.relationship('CompoundAtom',
                                                                        back_populates='compound')
    # ion: so.Mapped[int]
    # charge: so.Mapped[int]
    # c_type: so.Mapped[str]

    # def get_atoms(self):
    #     return self.atoms

    @property
    def atoms(self):
        return {ac.atom: ac.number for ac in self.atom_connections}

    @atoms.setter
    def atoms(self, atom_quant_dictionary):
        self.atom_connections = [
            CompoundAtom(atom=atom, number=number)
            for atom, number in atom_quant_dictionary.items()
        ]

    def __str__(self):
        return self.name

    def formula(self):
        def symbol_number(symbol, quantity):
            if quantity == 1:
                return symbol
            else:
                return f'{symbol}{quantity}'
        return ''.join(symbol_number(atom.symbol, quantity) for atom, quantity in self.atoms.items())

class Atom(Base):
    __tablename__ = 'atoms'
    atom_id: so.Mapped[int] = so.mapped_column(primary_key=True, autoincrement=True)
    name: so.Mapped[str]
    symbol: so.Mapped[str]
    # mass: so.Mapped[float]
    compound_connections: so.Mapped[list['CompoundAtom']] = so.relationship('CompoundAtom',
                                                                 back_populates='atom')

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Atom(name='{self.name}', symbol={self.symbol})"

if __name__ == "__main__":
    hydrogen = Atom(name='Hydrogen', symbol='H')
    oxygen = Atom(name='Oxygen', symbol='O')

    water = Compound(name='Water',
                     atom_connections=
                     [CompoundAtom(atom=hydrogen, number=2),
                      CompoundAtom(atom=oxygen, number=1),
                      ], )

    print(water.atoms)
    print(water.formula())
