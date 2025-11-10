import sqlalchemy as sa
import sqlalchemy.orm as so
from datetime import datetime
from Database.climbing.models import Climber, Route, ClimberRoute
from Database.climbing.create_db import construct_db

# This will delete the current database and construct a new one
construct_db()

climbers = [Climber(first_name="Milan", last_name="Gal"),
            Climber(first_name="Andrew", last_name="Dales"),
            Climber(first_name="Eleanore", last_name="Shiner"),
            ]

routes = [Route(name="Killer Climb"),
          Route(name="Black Wall"),
          ]

sqlite_engine = sa.create_engine('sqlite:///climbing.db', echo=True)

# Write data
with so.Session(bind=sqlite_engine) as session:
    # Add routes directly - this will cause the date to default to the current date
    climbers[0].routes_climbed.append(routes[0])
    climbers[0].routes_climbed.append(routes[1])
    climbers[1].routes_climbed.append(routes[0])

    # Create an association object:
    cr = ClimberRoute(climber=climbers[2],
                      route=routes[0],
                      date_climbed=datetime(2024,12, 31),
                      )


    session.add_all(climbers)
    session.commit()

# sess = so.Session(bind=sqlite_engine)
# climbers = sess.execute(sa.Select(Climber)).scalars().all()
# sess.close()
