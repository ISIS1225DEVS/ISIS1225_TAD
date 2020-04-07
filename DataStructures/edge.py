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

def newEdge (va, vb, weight=0):
    edge = {'vertexA':va, 'vertexB':vb,'weight':weight}
    return edge


def weight (edge):
    return edge['weight']


def either (edge):
    return edge['vertexA']


def other (edge, vertex):
    return edge['vertexB']

def compareedges (edge1, edge2):
    e1v = either (edge1)
    e2v = either (edge2)

    if e1v == e2v:
        if other(edge1, e1v) == other (edge2,e2v):
            return True
    return False

