# Extent

The extent of the features in the collection. In the Core only spatial and temporal extents are specified. Extensions may add additional members to represent other extents, for example, thermal or pressure ranges.

**Properties**

| Name     | Type     | Required | Description                                            |
| :------- | :------- | :------- | :----------------------------------------------------- |
| spatial  | Spatial  | ❌       | The spatial extent of the features in the collection.  |
| temporal | Temporal | ❌       | The temporal extent of the features in the collection. |

# Spatial

The spatial extent of the features in the collection.

**Properties**

| Name | Type              | Required | Description                                                                                                                                                                                                                                                                                                           |
| :--- | :---------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bbox | List[SpatialBbox] | ❌       | One or more bounding boxes that describe the spatial extent of the dataset. In the Core only a single bounding box is supported. Extensions may support additional areas. If multiple areas are provided, the union of the bounding boxes describes the spatial extent.                                               |
| crs  | Crs               | ❌       | Coordinate reference system of the coordinates in the spatial extent (property `bbox`). The default reference system is WGS 84 longitude/latitude. In the Core this is the only supported coordinate reference system. Extensions may support additional coordinate reference systems and add additional enum values. |

# SpatialBbox

Each bounding box is provided as four or six numbers, depending on whether the coordinate reference system includes a vertical axis (height or depth): _ Lower left corner, coordinate axis 1 _ Lower left corner, coordinate axis 2 _ Minimum value, coordinate axis 3 (optional) _ Upper right corner, coordinate axis 1 _ Upper right corner, coordinate axis 2 _ Maximum value, coordinate axis 3 (optional) The coordinate reference system of the values is WGS 84 longitude/latitude (http://www.opengis.net/def/crs/OGC/1.3/CRS84) unless a different coordinate reference system is specified in `crs`. For WGS 84 longitude/latitude the values are in most cases the sequence of minimum longitude, minimum latitude, maximum longitude and maximum latitude. However, in cases where the box spans the antimeridian the first value (west-most box edge) is larger than the third value (east-most box edge). If the vertical axis is included, the third and the sixth number are the bottom and the top of the 3-dimensional bounding box. If a feature has multiple spatial geometry properties, it is the decision of the server whether only a single spatial geometry property is used to determine the extent or all relevant geometries.

# Crs

Coordinate reference system of the coordinates in the spatial extent (property `bbox`). The default reference system is WGS 84 longitude/latitude. In the Core this is the only supported coordinate reference system. Extensions may support additional coordinate reference systems and add additional enum values.

**Properties**

| Name                               | Type | Required | Description                                    |
| :--------------------------------- | :--- | :------- | :--------------------------------------------- |
| HTTPWWWOPENGISNETDEFCRSOGC1_3CRS84 | str  | ✅       | "http://www.opengis.net/def/crs/OGC/1.3/CRS84" |

# Temporal

The temporal extent of the features in the collection.

**Properties**

| Name     | Type            | Required | Description                                                                                                                                                                                                                                                                                                                                        |
| :------- | :-------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| interval | List[List[str]] | ❌       | One or more time intervals that describe the temporal extent of the dataset. The value `null` is supported and indicates an unbounded interval end. In the Core only a single time interval is supported. Extensions may support multiple intervals. If multiple intervals are provided, the union of the intervals describes the temporal extent. |
| trs      | Trs             | ❌       | Coordinate reference system of the coordinates in the temporal extent (property `interval`). The default reference system is the Gregorian calendar. In the Core this is the only supported temporal coordinate reference system. Extensions may support additional temporal coordinate reference systems and add additional enum values.          |

# Trs

Coordinate reference system of the coordinates in the temporal extent (property `interval`). The default reference system is the Gregorian calendar. In the Core this is the only supported temporal coordinate reference system. Extensions may support additional temporal coordinate reference systems and add additional enum values.

**Properties**

| Name                                      | Type | Required | Description                                           |
| :---------------------------------------- | :--- | :------- | :---------------------------------------------------- |
| HTTPWWWOPENGISNETDEFUOMISO8601_0GREGORIAN | str  | ✅       | "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian" |

<!-- This file was generated by liblab | https://liblab.com/ -->
