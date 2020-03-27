"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Desarrollado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config
from DataStructures import adjlist as alt 

"""
  Este módulo implementa el tipo abstracto de datos (TAD) Graph. 
  Se puede implementar sobre una lista de adyacencias (ADJ_LIST) o una matriz de adyacencias (ADJ_MATRIX)
"""


def newGraph(datastructure = "ADJ_LIST"):
    """
    Crea un grafo vacio.
    """
    if (datastructure == "ADJ_LIST"):
        graph = alt.newGraph()

    return graph


