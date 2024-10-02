# This file was generated by liblab | https://liblab.com/

from .services.server import ServerService
from .services.dutch_metadata import DutchMetadataService
from .services.dutch_castles import DutchCastlesService
from .services.dutch_georef_stations import DutchGeorefStationsService
from .services.dutch_windmills import DutchWindmillsService
from .services.gdps_temperature import GdpsTemperatureService
from .services.icoads_sst import IcoadsSstService
from .services.lakes import LakesService
from .services.mapserver_world_map import MapserverWorldMapService
from .services.obs import ObsService
from .services.ogr_addresses_gpkg import OgrAddressesGpkgService
from .services.ogr_addresses_sqlite import OgrAddressesSqliteService
from .services.ogr_geojson_lakes import OgrGeojsonLakesService
from .services.ogr_gpkg_poi import OgrGpkgPoiService
from .services.ogr_gpkg_wales_railway_lines import OgrGpkgWalesRailwayLinesService
from .services.ogr_gpkg_wales_stations import OgrGpkgWalesStationsService
from .services.unesco_pois_italy import UnescoPoisItalyService
from .services.utah_city_locations import UtahCityLocationsService
from .services.jobs import JobsService
from .services.hello_world import HelloWorldService
from .services.stac import StacService
from .net.environment import Environment


class GeobeyondSdk:
    def __init__(self, base_url: str = Environment.DEFAULT.value, timeout: int = 60000):
        """
        Initializes GeobeyondSdk the SDK class.
        """

        self.server = ServerService(base_url=base_url)
        self.dutch_metadata = DutchMetadataService(base_url=base_url)
        self.dutch_castles = DutchCastlesService(base_url=base_url)
        self.dutch_georef_stations = DutchGeorefStationsService(base_url=base_url)
        self.dutch_windmills = DutchWindmillsService(base_url=base_url)
        self.gdps_temperature = GdpsTemperatureService(base_url=base_url)
        self.icoads_sst = IcoadsSstService(base_url=base_url)
        self.lakes = LakesService(base_url=base_url)
        self.mapserver_world_map = MapserverWorldMapService(base_url=base_url)
        self.obs = ObsService(base_url=base_url)
        self.ogr_addresses_gpkg = OgrAddressesGpkgService(base_url=base_url)
        self.ogr_addresses_sqlite = OgrAddressesSqliteService(base_url=base_url)
        self.ogr_geojson_lakes = OgrGeojsonLakesService(base_url=base_url)
        self.ogr_gpkg_poi = OgrGpkgPoiService(base_url=base_url)
        self.ogr_gpkg_wales_railway_lines = OgrGpkgWalesRailwayLinesService(
            base_url=base_url
        )
        self.ogr_gpkg_wales_stations = OgrGpkgWalesStationsService(base_url=base_url)
        self.unesco_pois_italy = UnescoPoisItalyService(base_url=base_url)
        self.utah_city_locations = UtahCityLocationsService(base_url=base_url)
        self.jobs = JobsService(base_url=base_url)
        self.hello_world = HelloWorldService(base_url=base_url)
        self.stac = StacService(base_url=base_url)
        self.set_timeout(timeout)

    def set_base_url(self, base_url):
        """
        Sets the base URL for the entire SDK.
        """
        self.server.set_base_url(base_url)
        self.dutch_metadata.set_base_url(base_url)
        self.dutch_castles.set_base_url(base_url)
        self.dutch_georef_stations.set_base_url(base_url)
        self.dutch_windmills.set_base_url(base_url)
        self.gdps_temperature.set_base_url(base_url)
        self.icoads_sst.set_base_url(base_url)
        self.lakes.set_base_url(base_url)
        self.mapserver_world_map.set_base_url(base_url)
        self.obs.set_base_url(base_url)
        self.ogr_addresses_gpkg.set_base_url(base_url)
        self.ogr_addresses_sqlite.set_base_url(base_url)
        self.ogr_geojson_lakes.set_base_url(base_url)
        self.ogr_gpkg_poi.set_base_url(base_url)
        self.ogr_gpkg_wales_railway_lines.set_base_url(base_url)
        self.ogr_gpkg_wales_stations.set_base_url(base_url)
        self.unesco_pois_italy.set_base_url(base_url)
        self.utah_city_locations.set_base_url(base_url)
        self.jobs.set_base_url(base_url)
        self.hello_world.set_base_url(base_url)
        self.stac.set_base_url(base_url)

        return self

    def set_timeout(self, timeout: int):
        """
        Sets the timeout for the entire SDK.

        :param int timeout: The timeout (ms) to be set.
        :return: The SDK instance.
        """
        self.server.set_timeout(timeout)
        self.dutch_metadata.set_timeout(timeout)
        self.dutch_castles.set_timeout(timeout)
        self.dutch_georef_stations.set_timeout(timeout)
        self.dutch_windmills.set_timeout(timeout)
        self.gdps_temperature.set_timeout(timeout)
        self.icoads_sst.set_timeout(timeout)
        self.lakes.set_timeout(timeout)
        self.mapserver_world_map.set_timeout(timeout)
        self.obs.set_timeout(timeout)
        self.ogr_addresses_gpkg.set_timeout(timeout)
        self.ogr_addresses_sqlite.set_timeout(timeout)
        self.ogr_geojson_lakes.set_timeout(timeout)
        self.ogr_gpkg_poi.set_timeout(timeout)
        self.ogr_gpkg_wales_railway_lines.set_timeout(timeout)
        self.ogr_gpkg_wales_stations.set_timeout(timeout)
        self.unesco_pois_italy.set_timeout(timeout)
        self.utah_city_locations.set_timeout(timeout)
        self.jobs.set_timeout(timeout)
        self.hello_world.set_timeout(timeout)
        self.stac.set_timeout(timeout)

        return self


# c029837e0e474b76bc487506e8799df5e3335891efe4fb02bda7a1441840310c
