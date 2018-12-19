# Creating Tiling Tools for ML-Export


This is a simple package to generate a list of tiles required for processing

```python
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

```




