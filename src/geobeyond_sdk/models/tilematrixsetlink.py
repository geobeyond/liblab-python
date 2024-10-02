# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap(
    {"tile_matrix_set": "tileMatrixSet", "tile_matrix_set_uri": "tileMatrixSetURI"}
)
class Tilematrixsetlink(BaseModel):
    """Tilematrixsetlink

    :param tile_matrix_set: tile_matrix_set
    :type tile_matrix_set: str
    :param tile_matrix_set_uri: tile_matrix_set_uri, defaults to None
    :type tile_matrix_set_uri: str, optional
    """

    def __init__(self, tile_matrix_set: str, tile_matrix_set_uri: str = None):
        """Tilematrixsetlink

        :param tile_matrix_set: tile_matrix_set
        :type tile_matrix_set: str
        :param tile_matrix_set_uri: tile_matrix_set_uri, defaults to None
        :type tile_matrix_set_uri: str, optional
        """
        self.tile_matrix_set = tile_matrix_set
        if tile_matrix_set_uri is not None:
            self.tile_matrix_set_uri = tile_matrix_set_uri
