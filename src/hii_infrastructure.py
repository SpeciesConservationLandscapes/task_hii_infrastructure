import ee
from task_base import EETask


class HIIInfrastructure(EETask):
    ee_rootdir = "projects/HII/v1/sumatra_poc"
    ee_driverdir = 'driver/infrastructure'
    # if input lives in ee, it should have an "ee_path" pointing to an ImageCollection/FeatureCollection
    inputs = {
        "dir_aeroway_aerodrome_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_aeroway_aerodrome_density_300m'",
        },
        "dir_aeroway_apron_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_aeroway_apron_density_300m'",
        },
        "dir_aeroway_hangar_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_aeroway_hangar_density_300m'",
        },
        "dir_aeroway_helipad_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_aeroway_helipad_density_300m'",
        },
        "dir_aeroway_heliport_PG_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_aeroway_heliport_PG_density_300m'",
        },
        "dir_aeroway_runway_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_aeroway_runway_density_300m'",
        },
        "dir_aeroway_spaceport_PG_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_aeroway_spaceport_PG_density_300m'",
        },
        "dir_aeroway_taxiway_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_aeroway_taxiway_density_300m'",
        },
        "dir_aeroway_terminal_PG_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_aeroway_terminal_PG_density_300m'",
        },
        "dir_amenity_aerialway_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_amenity_aerialway_density_300m'",
        },
        "dir_amenity_alpinecampwild_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_amenity_alpinecampwild_density_300m'",
        },
        "dir_leisure_beach_resort_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_leisure_beach_resort_density_300m'",
        },
        "dir_amenity_fuel_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_amenity_fuel_density_300m'",
        },
        "dir_leisure_golf_course_PG_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_leisure_golf_course_PG_density_300m'",
        },
        "dir_leisure_marina_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_leisure_marina_density_300m'",
        },
        "dir_leisure_pitch_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_leisure_pitch_density_300m'",
        },
        "dir_amenity_sanitary_dump_station_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_amenity_sanitary_dump_station_density_300m'",
        },
        "dir_barrier_city_wall_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_barrier_city_wall_density_300m'",
        },
        "dir_barrier_ditch_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_barrier_ditch_density_300m'",
        },
        "dir_barrier_hedge_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_barrier_hedge_density_300m'",
        },
        "dir_barrier_retaining_wall_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_barrier_retaining_wall_density_300m'",
        },
        "dir_barrier_wall_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_barrier_wall_density_300m'",
        },
        "dir_highway_bridleway_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_highway_bridleway_density_300m'",
        },
        "dir_highway_bus_guideway_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_highway_bus_guideway_density_300m'",
        },
        "dir_highway_cycleway_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_highway_cycleway_density_300m'",
        },
        "dir_highway_elevator_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_highway_elevator_density_300m'",
        },
        "dir_highway_escape_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_highway_escape_density_300m'",
        },
        "dir_highway_footway_density_300mA": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_highway_footway_density_300mA'",
        },
        "dir_highway_living_street_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_highway_living_street_density_300m'",
        },
        "dir_highway_mini_roundabout_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_highway_mini_roundabout_density_300m'",
        },
        "dir_highway_motorway_link_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_highway_motorway_link_density_300m'",
        },
        "dir_highway_path_density_300mA": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_highway_path_density_300mA'",
        },
        "dir_highway_pedestrian_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_highway_pedestrian_density_300m'",
        },
        "dir_highway_primary_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_highway_primary_density_300m'",
        },
        "dir_highway_primary_link_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_highway_primary_link_density_300m'",
        },
        "dir_highway_raceway_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_highway_raceway_density_300m'",
        },
        "dir_highway_rest_area_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_highway_rest_area_density_300m'",
        },
        "dir_highway_road_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_highway_road_density_300m'",
        },
        "dir_highway_secondary_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_highway_secondary_density_300m'",
        },
        "dir_highway_secondary_link_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_highway_secondary_link_density_300m'",
        },
        "dir_highway_steps_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_highway_steps_density_300m'",
        },
        "dir_highway_tertiary_density_300mA": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_highway_tertiary_density_300mA'",
        },
        "dir_highway_tertiary_link_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_highway_tertiary_link_density_300m'",
        },
        "dir_highway_track_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/wcsbackup/osm_earth/dir_highway_track_density_300m'",
        },
        "dir_highway_trunk_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_highway_trunk_density_300m'",
        },
        "dir_highway_trunk_link_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_highway_trunk_link_density_300m'",
        },
        "dir_highway_turning_circle_NO_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_highway_turning_circle_NO_density_300m'",
        },
        "dir_highway_unclassified_density_300m_A": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_highway_unclassified_density_300m_A'",
        },
        "groads_additions": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/intact_default_CROP/groads_additions",
        },
        "dir_landuse_basin_PG_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_landuse_basin_PG_density_300m'",
        },
        "dir_landuse_cemetery_PG_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_landuse_cemetery_PG_density_300m'",
        },
        "dir_landuse_industrial_PG_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_landuse_industrial_PG_density_300m'",
        },
        "dir_landuse_landfill_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_landuse_landfill_density_300m'",
        },
        "dir_landuse_quarry_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_landuse_quarry_density_300m'",
        },
        "dir_landuse_salt_pond_PG_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_landuse_salt_pond_PG_density_300m'",
        },
        "dir_landuse_village_green_PG_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_landuse_village_green_PG_density_300m'",
        },
        "dir_man_made_adit_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_man_made_adit_density_300m'",
        },
        "dir_man_made_beacon_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_man_made_beacon_density_300m'",
        },
        "dir_man_made_breakwater_PG_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_man_made_breakwater_PG_density_300m'",
        },
        "dir_man_made_chimney_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_man_made_chimney_density_300m'",
        },
        "dir_man_made_communications_tower_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_man_made_communications_tower_density_300m'",
        },
        "dir_man_made_dyke_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_man_made_dyke_density_300m'",
        },
        "dir_man_made_embankment_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_man_made_embankment_density_300m'",
        },
        "dir_man_made_gasometer_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_man_made_gasometer_density_300m'",
        },
        "dir_man_made_groyne_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_man_made_groyne_density_300m'",
        },
        "dir_man_made_lighthouse_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_man_made_lighthouse_density_300m'",
        },
        "dir_man_made_mast_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_man_made_mast_density_300m'",
        },
        "dir_man_made_mineshaft_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_man_made_mineshaft_density_300m'",
        },
        "dir_man_made_observatorytelescope_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_man_made_observatorytelescope_density_300m'",
        },
        "dir_man_made_petroleum_well_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_man_made_petroleum_well_density_300m'",
        },
        "dir_man_made_pier_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_man_made_pier_density_300m'",
        },
        "dir_man_made_pipeline_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_man_made_pipeline_density_300m'",
        },
        "dir_man_made_pumping_station_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_man_made_pumping_station_density_300m'",
        },
        "dir_man_made_reservoir_covered_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_man_made_reservoir_covered_density_300m'",
        },
        "dir_man_made_silo_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_man_made_silo_density_300m'",
        },
        "dir_man_made_snow_fence_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_man_made_snow_fence_density_300m'",
        },
        "dir_man_made_storage_tank_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_man_made_storage_tank_density_300m'",
        },
        "dir_man_made_tower_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_man_made_tower_density_300m'",
        },
        "dir_man_made_wastewater_plant_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_man_made_wastewater_plant_density_300m'",
        },
        "dir_man_made_watermill_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_man_made_watermill_density_300m'",
        },
        "dir_man_made_water_tower_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_man_made_water_tower_density_300m'",
        },
        "dir_man_made_water_well_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_man_made_water_well_density_300m'",
        },
        "dir_man_made_water_works_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_man_made_water_works_density_300m'",
        },
        "dir_man_made_windmill_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_man_made_windmill_density_300m'",
        },
        "dir_man_made_works_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_man_made_works_density_300m'",
        },
        "dir_military_airfield_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_military_airfield_density_300m'",
        },
        "dir_military_ammunition_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_military_ammunition_density_300m'",
        },
        "dir_military_barracks_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_military_barracks_density_300m'",
        },
        "dir_military_bunker_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/osm_earth/dir_military_bunker_density_300m'",
        },
        "dir_military_checkpoint_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_military_checkpoint_density_300m'",
        },
        "dir_military_danger_area_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_military_danger_area_density_300m'",
        },
        "dir_military_naval_base_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_military_naval_base_density_300m'",
        },
        "dir_military_nuclear_explosion_site_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_military_nuclear_explosion_site_density_300m'",
        },
        "dir_military_range_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_military_range_density_300m'",
        },
        "dir_military_trench_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_military_trench_density_300m'",
        },
        "dir_power_cable_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_power_cable_density_300m'",
        },
        "dir_power_heliostat_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_power_heliostat_density_300m'",
        },
        "dir_power_line_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_power_line_density_300m'",
        },
        "dir_power_substation_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_power_substation_density_300m'",
        },
        "dir_power_xbio_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_power_xbio_density_300m'",
        },
        "dir_power_xcoal_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_power_xcoal_density_300m'",
        },
        "dir_power_xhydro_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_power_xhydro_density_300m'",
        },
        "dir_power_xnuclear_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_power_xnuclear_density_300m'",
        },
        "dir_power_xoil_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_power_xoil_density_300m'",
        },
        "dir_power_xother_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_power_xother_density_300m'",
        },
        "dir_power_xsolar_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_power_xsolar_density_300m'",
        },
        "dir_power_xwaste_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_power_xwaste_density_300m'",
        },
        "dir_power_xwind_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_power_xwind_density_300m'",
        },
        "dir_railway_abandoned_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_railway_abandoned_density_300m'",
        },
        "dir_railway_disused_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_railway_disused_density_300m'",
        },
        "dir_railway_funicular_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_railway_funicular_density_300m'",
        },
        "dir_railway_halt_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_railway_halt_density_300m'",
        },
        "dir_railway_light_rail_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_railway_light_rail_density_300m'",
        },
        "dir_railway_miniature_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_railway_miniature_density_300m'",
        },
        "dir_railway_monorail_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_railway_monorail_density_300m'",
        },
        "dir_railway_narrow_gauge_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_railway_narrow_gauge_density_300m'",
        },
        "dir_railway_platform_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_railway_platform_density_300m'",
        },
        "dir_railway_preserved_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_railway_preserved_density_300m'",
        },
        "dir_railway_rail_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_railway_rail_density_300m'",
        },
        "dir_railway_station_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_railway_station_density_300m'",
        },
        "dir_railway_subway_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_railway_subway_density_300m'",
        },
        "dir_railway_tram_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_railway_tram_density_300m'",
        },
        "dir_waterway_canal_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_waterway_canal_density_300m'",
        },
        "dir_waterway_dam_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_waterway_dam_density_300m'",
        },
        "dir_waterway_ditch_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_waterway_ditch_density_300m'",
        },
        "dir_waterway_drain_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_waterway_drain_density_300m'",
        },
        "dir_waterway_lock_gate_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_waterway_lock_gate_density_300m'",
        },
        "dir_waterway_weir_density_300m": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/yourecoveredinbees/osm_earth/dir_waterway_weir_density_300m'",
        },

        "jrc": {
            "ee_type": EETask.IMAGE,
            "ee_path": "JRC/GSW1_0/GlobalSurfaceWater"
        },
        "caspian": {
            "ee_type": EETask.FEATURECOLLECTION,
            "ee_path": "users/aduncan/caspian"
        },
        "ocean": {
            "ee_type": EETask.IMAGE,
            "ee_path": "users/aduncan/cci/ESACCI-LC-L4-WB-Ocean-Map-150m-P13Y-2000-v40",
        }
            }
    



    gpw_cadence = 5

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_aoi_from_ee("{}/sumatra_poc_aoi".format(self.ee_rootdir))



    def calc(self):

        jrc = ee.Image(self.inputs['jrc']['ee_path']).select('occurrence').lte(75).unmask(1).multiply(ee.Image(0)\
                                        .clip(ee.FeatureCollection(self.inputs['caspian']['ee_path'])).unmask(1))
        ocean = ee.Image(self.inputs['ocean']['ee_path']);


 
        rast_aeroway_density_300m_direct = ee.Image(self.inputs['dir_aeroway_aerodrome_density_300m']['ee_path']).multiply(10)\
                                .add(ee.Image(self.inputs['dir_aeroway_apron_density_300m']['ee_path']).multiply(10))\
                                .add(ee.Image(self.inputs['dir_aeroway_hangar_density_300m']['ee_path']).multiply(10))\
                                .add(ee.Image(self.inputs['dir_aeroway_helipad_density_300m']['ee_path']).multiply(10))\
                                .add(ee.Image(self.inputs['dir_aeroway_heliport_PG_density_300m']['ee_path']).multiply(10))\
                                .add(ee.Image(self.inputs['dir_aeroway_runway_density_300m']['ee_path']).multiply(10))\
                                .add(ee.Image(self.inputs['dir_aeroway_spaceport_PG_density_300m']['ee_path']).multiply(10))\
                                .add(ee.Image(self.inputs['dir_aeroway_taxiway_density_300m']['ee_path']).multiply(10))\
                                .add(ee.Image(self.inputs['dir_aeroway_terminal_PG_density_300m']['ee_path']).multiply(10))
                                
                                


        rast_amen_tour_leis_aerial_density_300m_direct = ee.Image(self.inputs['dir_amenity_aerialway_density_300m']['ee_path']).multiply((5))\
                                .add(ee.Image(self.inputs['dir_amenity_alpinecampwild_density_300m']['ee_path']).multiply((4)))\
                                .add(ee.Image(self.inputs['dir_leisure_beach_resort_density_300m']['ee_path']).multiply((4)))\
                                .add(ee.Image(self.inputs['dir_amenity_fuel_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_leisure_golf_course_PG_density_300m']['ee_path']).multiply((4)))\
                                .add(ee.Image(self.inputs['dir_leisure_marina_density_300m']['ee_path']).multiply((4)))\
                                .add(ee.Image(self.inputs['dir_leisure_pitch_density_300m']['ee_path']).multiply((4)))\
                                .add(ee.Image(self.inputs['dir_amenity_sanitary_dump_station_density_300m']['ee_path']).multiply((10)))
                                

 
        rast_barrier_density_300m_direct = ee.Image(self.inputs['dir_barrier_city_wall_density_300m']['ee_path']).multiply((8))\
                                .add(ee.Image(self.inputs['dir_barrier_ditch_density_300m']['ee_path']).multiply((8)))\
                                .add(ee.Image(self.inputs['dir_barrier_hedge_density_300m']['ee_path']).multiply((2)))\
                                .add(ee.Image(self.inputs['dir_barrier_retaining_wall_density_300m']['ee_path']).multiply((8)))\
                                .add(ee.Image(self.inputs['dir_barrier_wall_density_300m']['ee_path']).multiply((8)))
                                




        rast_highway_density_300m_direct = ee.Image(self.inputs['dir_highway_bridleway_density_300m']['ee_path']).multiply((4))\
                                .add(ee.Image(self.inputs['dir_highway_bus_guideway_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_highway_cycleway_density_300m']['ee_path']).multiply((4)))\
                                .add(ee.Image(self.inputs['dir_highway_elevator_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_highway_escape_density_300m']['ee_path']).multiply((4)))\
                                .add(ee.Image(self.inputs['dir_highway_footway_density_300mA']['ee_path']).multiply((4)))\
                                .add(ee.Image(self.inputs['dir_highway_living_street_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_highway_mini_roundabout_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_highway_motorway_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_highway_motorway_link_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_highway_path_density_300mA']['ee_path']).multiply((4)))\
                                .add(ee.Image(self.inputs['dir_highway_pedestrian_density_300m']['ee_path']).multiply((4)))\
                                .add(ee.Image(self.inputs['dir_highway_primary_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_highway_primary_link_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_highway_raceway_density_300m']['ee_path']).multiply((10)))\
                                #.add(ee.Image(self.inputs['dir_highway_residential_300m']['ee_path']).multiply((10))) // NOT DONE!!!
                                .add(ee.Image(self.inputs['dir_highway_rest_area_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_highway_road_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_highway_secondary_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_highway_secondary_link_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_highway_service_density_300mA']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_highway_steps_density_300m']['ee_path']).multiply((4)))\
                                .add(ee.Image(self.inputs['dir_highway_tertiary_density_300mA']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_highway_tertiary_link_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_highway_track_density_300m']['ee_path']).multiply((4)))\
                                .add(ee.Image(self.inputs['dir_highway_trunk_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_highway_trunk_link_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_highway_turning_circle_NO_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_highway_unclassified_density_300mA']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['groads_additions']['ee_path']).multiply((10)))
                                




        rast_landuse_density_300m_direct = ee.Image(self.inputs['dir_landuse_basin_PG_density_300m']['ee_path']).multiply((10))\
                                .add(ee.Image(self.inputs['dir_landuse_cemetery_PG_density_300m']['ee_path']).multiply((4)))\
                                .add(ee.Image(self.inputs['dir_landuse_industrial_PG_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_landuse_landfill_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_landuse_quarry_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_landuse_salt_pond_PG_density_300m']['ee_path']).multiply((4)))\
                                .add(ee.Image(self.inputs['dir_landuse_village_green_PG_density_300m']['ee_path']).multiply((4)))
                                






        rast_manmade_density_300m_direct = ee.Image(self.inputs['dir_man_made_adit_density_300m']['ee_path']).multiply((10))\
                                .add(ee.Image(self.inputs['dir_man_made_beacon_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_man_made_breakwater_PG_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_man_made_chimney_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_man_made_communications_tower_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_man_made_dyke_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_man_made_embankment_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_man_made_gasometer_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_man_made_groyne_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_man_made_lighthouse_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_man_made_mast_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_man_made_mineshaft_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_man_made_observatorytelescope_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_man_made_petroleum_well_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_man_made_pier_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_man_made_pipeline_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_man_made_pumping_station_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_man_made_reservoir_covered_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_man_made_silo_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_man_made_snow_fence_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_man_made_storage_tank_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_man_made_tower_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_man_made_wastewater_plant_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_man_made_watermill_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_man_made_water_tower_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_man_made_water_well_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_man_made_water_works_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_man_made_windmill_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_man_made_works_density_300m']['ee_path']).multiply((10)))
                                
                                





        rast_military_density_300m_direct = ee.Image(self.inputs['dir_military_airfield_density_300m']['ee_path']).multiply((10))\
                                .add(ee.Image(self.inputs['dir_military_ammunition_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_military_barracks_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_military_bunker_density_300m']['ee_path']).multiply((10))) \
                                .add(ee.Image(self.inputs['dir_military_checkpoint_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_military_danger_area_density_300m']['ee_path']).multiply((8)))\
                                .add(ee.Image(self.inputs['dir_military_naval_base_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_military_nuclear_explosion_site_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_military_range_density_300m']['ee_path']).multiply((8)))\
                                .add(ee.Image(self.inputs['dir_military_trench_density_300m']['ee_path']).multiply((8)))
                                



        rast_power_density_300m_direct = ee.Image(self.inputs['dir_power_cable_density_300m']['ee_path']).multiply((8))\
                                .add(ee.Image(self.inputs['dir_power_heliostat_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_power_line_density_300m']['ee_path']).multiply((8)))\
                                .add(ee.Image(self.inputs['dir_power_substation_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_power_xbio_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_power_xcoal_density_300m']['ee_path']).multiply((10)))\
                                #.add(ee.Image(self.inputs['dir_power_xgas_density_300m']['ee_path']).multiply((10))) // 300 not done
                                .add(ee.Image(self.inputs['dir_power_xhydro_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_power_xnuclear_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_power_xoil_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_power_xother_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_power_xsolar_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_power_xwaste_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_power_xwind_density_300m']['ee_path']).multiply((10)))
                                




        rast_railway_density_300m_direct = ee.Image(self.inputs['dir_railway_abandoned_density_300m']['ee_path']).multiply((4))\
                                .add(ee.Image(self.inputs['dir_railway_disused_density_300m']['ee_path']).multiply((4)))\
                                .add(ee.Image(self.inputs['dir_railway_funicular_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_railway_halt_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_railway_light_rail_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_railway_miniature_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_railway_monorail_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_railway_narrow_gauge_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_railway_platform_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_railway_preserved_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_railway_rail_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_railway_station_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_railway_subway_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_railway_tram_density_300m']['ee_path']).multiply((10)))
                                




        rast_waterway_density_300m_direct = ee.Image(self.inputs['dir_waterway_canal_density_300m']['ee_path']).multiply((10))\
                                .add(ee.Image(self.inputs['dir_waterway_dam_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_waterway_ditch_density_300m']['ee_path']).multiply((4)))\
                                .add(ee.Image(self.inputs['dir_waterway_drain_density_300m']['ee_path']).multiply((4)))\
                                .add(ee.Image(self.inputs['dir_waterway_lock_gate_density_300m']['ee_path']).multiply((10)))\
                                .add(ee.Image(self.inputs['dir_waterway_weir_density_300m']['ee_path']).multiply((4)))
                                


        osm = rast_aeroway_density_300m_direct\
                              .add(rast_amen_tour_leis_aerial_density_300m_direct)\
                              .add(rast_barrier_density_300m_direct)\
                              #.add(rast_highway_density_300m_direct)\
                              .add(rast_landuse_density_300m_direct)\
                              .add(rast_manmade_density_300m_direct)\
                              .add(rast_military_density_300m_direct)\
                              .add(rast_power_density_300m_direct)\
                              #.add(rast_railway_density_300m_direct)\
                              .add(rast_waterway_density_300m_direct)\
                              .multiply(2)
                              


        #NEED TO REDO BELOW INCORPORATING WEIGHTINGS AND ELIMINATING 500M BUFFER
        #roads 500m
        roads_bool = rast_highway_density_300m_direct.gt(0).multiply(2)
        roads_500m = roads_bool.reduceNeighborhood(reducer=ee.Reducer.max(), kernel=ee.Kernel.square(1,'pixels'))\
                          .reproject(crs='EPSG:4326',scale=300)


        DECAY_CONSTANT = -0.0002
        INDIRECT_INFLUENCE = 4
        roads_indirect = roads_bool.eq(0).cumulativeCost(roads_bool,15000).reproject(crs='EPSG:4326',scale=300).unmask(0)\
                                        .multiply(DECAY_CONSTANT).exp()\
                                        .multiply(INDIRECT_INFLUENCE)
                                        

        roads_total = roads_500m.add(roads_indirect)
        roads_total = roads_total.where(roads_total.gt(8),8)


        #rail 500m
        rail_bool = rast_railway_density_300m_direct.gt(0).multiply(2)
        rail_500m = rail_bool.reduceNeighborhood(reducer=ee.Reducer.max(), kernel=ee.Kernel.square(1,'pixels'))\
                          .reproject(crs='EPSG:4326',scale=300)
                          


        current_infra = roads_total.add(rail_500m).add(osm)

    def check_inputs(self):
        super().check_inputs()
        # add any task-specific checks here, and set self.status = self.FAILED if any fail


if __name__ == "__main__":
    infrastructure_task = HIIInfrastructure()
    infrastructure_task.run()
