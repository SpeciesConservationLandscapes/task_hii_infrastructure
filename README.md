HII INFRASTUCTURE DRIVER
---------------

## What does this task do?

This task calculates the (unitless) anthropogenic "influence" of roads on the terrestrial surface as one of the key
drivers for a combined [Human Influence Index](https://github.com/SpeciesConservationLandscapes/task_hii_weightedsum)
. "Influence" is the `direct` influence
relative to each cell with at least one type of infrastructure. These source infrastructure cells are a combination of:

1. The most recent OSM data relative to `taskdate`, as rasterized by the
   [task_hii_osm_csv](https://github.com/SpeciesConservationLandscapes/task_hii_osm_csv) and
   [task_hii_osm_ingest](https://github.com/SpeciesConservationLandscapes/task_hii_osm_ingest) tasks. This image,
   stored in Earth Engine at `projects/HII/v1/osm/osm_image`, contains up to 193
   bands for OSM features infrastructure tags. A cell in each band has a
   value of 1 in every 300m pixel if there are any OSM features with that tag in the cell, and NoData otherwise.
   This data is available since 2012-09-12, in steadily increasing quantity and quality.
2. Static GHSL data (https://ghsl.jrc.ec.europa.eu/) representing built-up areas from
   1975-2015 are used to fill cells not marked by OSM. (Implicitly, we do not capture infrastructure that actually disappears
   over time.) In the future, once GHSL's contribution is marginal enough, we will discontinue its use. Conversely,
   prior to 2012-09-12, it is the only source.

We are able to use the different OSM infrastructure types to weight infrastructure influence by type, a key advance over previous Human Footprint efforts.

```
"osm": {
    "aerialway_cable_car": 4,
    "aerialway_chair_lift": 4,
    "aerialway_drag_lift": 4,
    "aerialway_gondola": 4,
    "aerialway_j-bar": 4,
    "aerialway_magic_carpet": 4,
    "aerialway_mixed_lift": 4,
    "aerialway_platter": 4,
    "aerialway_rope_tow": 4,
    "aerialway_station": 4,
    "aerialway_t-bar": 4,
    "aerialway_yes": 4,
    "aerialway_zip_line": 4,
    "aeroway_aerodrome": 10,
    "aeroway_apron": 10,
    "aeroway_hangar": 10,
    "aeroway_helipad": 10,
    "aeroway_heliport": 10,
    "aeroway_runway": 10,
    "aeroway_spaceport": 10,
    "aeroway_taxiway": 10,
    "aeroway_terminal": 10,
    "amenity_bus_station": 10,
    "amenity_fuel": 10,
    "amenity_marketplace": 10,
    "amenity_parking": 10,
    "amenity_public_bath": 10,
    "amenity_recycling": 10,
    "amenity_refugee_site": 10,
    "amenity_sanitary_dump_station": 10,
    "amenity_shelter": 10,
    "amenity_toilets": 10,
    "amenity_waste_basket": 4,
    "amenity_waste_disposal": 10,
    "amenity_waste_transfer_station": 10,
    "barrier_city_wall": 10,
    "barrier_ditch": 4,
    "barrier_fence": 4,
    "barrier_hedge": 4,
    "barrier_retaining_wall": 10,
    "barrier_wall": 10,
    "building_apartments": 10,
    "building_bakehouse": 10,
    "building_barn": 6,
    "building_bungalow": 6,
    "building_cabin": 4,
    "building_carport": 4,
    "building_cathedral": 10,
    "building_chapel": 10,
    "building_church": 10,
    "building_civic": 10,
    "building_college": 10,
    "building_commercial": 10,
    "building_conservatory": 10,
    "building_construction": 10,
    "building_cowshed": 4,
    "building_detached": 6,
    "building_digester": 10,
    "building_dormitory": 10,
    "building_farm": 8,
    "building_farm_auxiliary": 6,
    "building_fire_station": 10,
    "building_garage": 10,
    "building_garages": 10,
    "building_gatehouse": 10,
    "building_ger": 4,
    "building_government": 10,
    "building_grandstand": 10,
    "building_greenhouse": 8,
    "building_hangar": 10,
    "building_hospital": 10,
    "building_hotel": 10,
    "building_house": 10,
    "building_houseboat": 4,
    "building_hut": 4,
    "building_industrial": 10,
    "building_kindergarten": 10,
    "building_kiosk": 10,
    "building_military": 10,
    "building_monastery": 10,
    "building_mosque": 10,
    "building_office": 10,
    "building_parking": 10,
    "building_pavilion": 10,
    "building_presbytery": 10,
    "building_public": 10,
    "building_religious": 10,
    "building_residential": 8,
    "building_retail": 10,
    "building_riding_hall": 10,
    "building_roof": 10,
    "building_school": 10,
    "building_semidetached_house": 8,
    "building_service": 10,
    "building_shed": 4,
    "building_shrine": 10,
    "building_slurry_tank": 10,
    "building_sports_hall": 10,
    "building_stable": 8,
    "building_static_caravan": 10,
    "building_sty": 10,
    "building_supermarket": 10,
    "building_synagogue": 10,
    "building_temple": 10,
    "building_terrace": 10,
    "building_toilets": 10,
    "building_train_station": 10,
    "building_transformer_tower": 10,
    "building_transportation": 10,
    "building_university": 10,
    "building_warehouse": 10,
    "building_water_tower": 10,
    "building_yes": 10,
    "landuse_basin": 4,
    "landuse_brownfield": 4,
    "landuse_cemetery": 4,
    "landuse_industrial": 10,
    "landuse_landfill": 10,
    "landuse_quarry": 10,
    "landuse_salt_pond": 10,
    "landuse_village_green": 4,
    "leisure_beach_resort": 4,
    "leisure_golf_course": 4,
    "leisure_marina": 10,
    "leisure_miniature_golf": 8,
    "leisure_pitch": 4,
    "leisure_sports_centre": 10,
    "leisure_stadium": 10,
    "leisure_summer_camp": 4,
    "leisure_swimming_pool": 6,
    "leisure_track": 10,
    "leisure_water_park": 10,
    "man_made_adit": 10,
    "man_made_beacon": 10,
    "man_made_breakwater": 10,
    "man_made_chimney": 10,
    "man_made_communications_tower": 10,
    "man_made_dyke": 6,
    "man_made_embankment": 6,
    "man_made_gasometer": 10,
    "man_made_groyne": 10,
    "man_made_lighthouse": 10,
    "man_made_mast": 10,
    "man_made_mineshaft": 10,
    "man_made_petroleum_well": 10,
    "man_made_pier": 10,
    "man_made_pipeline": 10,
    "man_made_pumping_station": 10,
    "man_made_reservoir_covered": 10,
    "man_made_silo": 10,
    "man_made_snow_fence": 4,
    "man_made_storage_tank": 10,
    "man_made_tower": 10,
    "man_made_wastewater_plant": 10,
    "man_made_water_tower": 10,
    "man_made_water_well": 10,
    "man_made_water_works": 10,
    "man_made_watermill": 10,
    "man_made_windmill": 10,
    "man_made_works": 10,
    "military_airfield": 10,
    "military_ammunition": 10,
    "military_barracks": 10,
    "military_bunker": 10,
    "military_checkpoint": 10,
    "military_danger_area": 8,
    "military_naval_base": 10,
    "military_nuclear_explosion_site": 10,
    "military_range": 10,
    "military_trench": 10,
    "power_cable": 8,
    "power_heliostat": 10,
    "power_line": 8,
    "power_substation": 10,
    "public_transport_platform": 10,
    "public_transport_station": 10,
    "public_transport_stop_area": 10,
    "sport_golf": 10,
    "tourism_alpine_hut": 4,
    "tourism_artwork": 4,
    "tourism_camp_site": 4,
    "tourism_caravan_site": 10,
    "tourism_theme_park": 10,
    "tourism_wilderness_hut": 4,
    "tourism_zoo": 10,
    "waterway_boatyard": 10,
    "waterway_canal": 10,
    "waterway_dam": 10,
    "waterway_ditch": 4,
    "waterway_drain": 4,
    "waterway_lock_gate": 10,
    "waterway_weir": 4,
},
"ghsl": {
    "ghsl": 10,
}
}
```

For any given output cell, the end result is the maximum (**not** the cumulative addition) of each type of infrastructure. Values are multiplied by 100 and converted to integer for efficient
exporting to and storage in the Earth Engine HII Road Driver image collection (`projects/HII/v1/driver/infrastructure`).

## Variables and Defaults

### Environment variables
```
SERVICE_ACCOUNT_KEY=<GOOGLE SERVICE ACCOUNT KEY>
```

### Class constants

```
scale=300
GHSL_THRESHOLD=2
OSM_START = datetime(2012, 9, 12).date()
```

## Usage

*All parameters may be specified in the environment as well as the command line.*

```
/app # python task.py --help
usage: task.py [-h] [-d TASKDATE] [--overwrite]

optional arguments:
  -h, --help            show this help message and exit
  -d TASKDATE, --taskdate TASKDATE
  --overwrite           overwrite existing outputs instead of incrementing

```
