from shapely import geometry
import mercantile
import numpy as np
import logging

logging.basicConfig(format='%(levelname)s:%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)


def get_tile_list(geom,
                  zoom=17):
    """Generate the Tile List for The Tasking List

    Parameters
    ----------
    geom: shapely geometry of area.

    zoom : int Zoom Level for Tiles
        One or more zoom levels.

    Yields
    ------
    list of tiles that intersect with provided geom

    """

    west, south, east, north = geom.bounds
    tiles = mercantile.tiles(west, south, east, north, zooms=zoom)
    tile_list = []

    for tile in tiles:

        tile_geom = geometry.shape(mercantile.feature(tile)['geometry'])

        if tile_geom.intersects(geom):
            tile_list.append(tile)

    return tile_list









