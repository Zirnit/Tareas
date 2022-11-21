class Taxon:
  subcategorias = []      
  def __init__(self, categoria, nombre):
     self.categoria = categoria
     self.nombre = nombre
     self.subcategorias = []

  def incluir(self, subcat):
    self.subcategorias.append(subcat)
