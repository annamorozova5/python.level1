class Geom:
    name = "Geom"


class Line(Geom):
   pass

class React(Geom):
    pass

g = Geom()
l = Line()
r = React()
print(r.name)
