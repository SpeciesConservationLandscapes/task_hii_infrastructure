import argparse
import ee
from datetime import datetime, timezone
from task_base import EETask


class HIIInfrastructure(EETask):
    ee_rootdir = "projects/HII/v1/sumatra_poc"
    ee_driverdir = "driver/infrastructure"
    ee_hiistatic_osm = "projects/HII/v1/source/osm_earth/"
    ee_hiistatic_infra = "projects/HII/v1/source/infra/"
    ee_hiistatic_physical = "projects/HII/v1/source/phys/"
    scale = 300
    DECAY_CONSTANT = -0.0002
    INDIRECT_INFLUENCE = 4


    aeroway_aerodrome_weighting = 10
    aeroway_apron_weighting = 10
    aeroway_hangar_weighting = 10
    aeroway_helipad_weighting = 10
    aeroway_heliport_weighting = 10
    aeroway_runway_weighting = 10
    aeroway_spaceport_weighting = 10
    aeroway_taxiway_weighting = 10
    aeroway_terminal_weighting = 10

    amenity_aerialway_weighting = 5
    amenity_alpinecampwild_weighting = 4
    amenity_fuel_weighting = 10
    amenity_sanitary_dump_station_weighting = 10

    barrier_city_wall_weighting = 8
    barrier_ditch_weighting = 8
    barrier_hedge_weighting = 2
    barrier_retaining_wall_weighting = 8
    barrier_wall_weighting = 8

    landuse_basin_weighting = 10
    landuse_cemetery_weighting = 4
    landuse_industrial_weighting = 10
    landuse_landfill_weighting = 10
    landuse_quarry_weighting = 10
    landuse_salt_pond_weighting = 4
    landuse_village_green_weighting = 4

    leisure_beach_resort_weighting = 4
    leisure_golf_course_weighting = 4
    leisure_marina_weighting = 4
    leisure_pitch_weighting = 4

    man_made_adit_weighting = 10
    man_made_beacon_weighting = 10
    man_made_breakwater_weighting = 10
    man_made_chimney_weighting = 10
    man_made_communications_tower_weighting = 10
    man_made_dyke_weighting = 10
    man_made_embankment_weighting = 10
    man_made_gasometer_weighting = 10
    man_made_groyne_weighting = 10
    man_made_lighthouse_weighting = 10
    man_made_mast_weighting = 10
    man_made_mineshaft_weighting = 10
    man_made_observatorytelescope_weighting = 10
    man_made_petroleum_well_weighting = 10
    man_made_pier_weighting = 10
    man_made_pipeline_weighting = 10
    man_made_pumping_station_weighting = 10
    man_made_reservoir_covered_weighting = 10
    man_made_silo_weighting = 10
    man_made_snow_fence_weighting = 4
    man_made_storage_tank_weighting = 10
    man_made_tower_weighting = 10
    man_made_wastewater_plant_weighting = 10
    man_made_water_tower_weighting = 10
    man_made_water_well_weighting = 10
    man_made_water_works_weighting = 10
    man_made_watermill_weighting = 10
    man_made_windmill_weighting = 10
    man_made_works_weighting = 10

    military_airfield_weighting = 10
    military_ammunition_weighting = 10
    military_barracks_weighting = 10
    military_bunker_weighting = 10
    military_checkpoint_weighting = 10
    military_danger_area_weighting = 8
    military_naval_base_weighting = 10
    military_nuclear_explosion_site_weighting = 10
    military_range_weighting = 8
    military_trench_weighting = 8

    power_cable_weighting = 8
    power_heliostat_weighting = 10
    power_line_weighting = 8
    power_substation_weighting = 10
    power_xbio_weighting = 10
    power_xcoal_weighting = 10
    power_xhydro_weighting = 10
    power_xnuclear_weighting = 10
    power_xoil_weighting = 10
    power_xother_weighting = 10
    power_xsolar_weighting = 10
    power_xwaste_weighting = 10
    power_xwind_weighting = 10

    waterway_canal_weighting = 10
    waterway_dam_weighting = 10
    waterway_ditch_weighting = 4
    waterway_drain_weighting = 4
    waterway_lock_gate_weighting = 10
    waterway_weir_weighting = 4


    inputs = {
        "aeroway_aerodrome": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}aeroway/aerodrome",
        },
        "aeroway_apron": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}aeroway/apron",
        },
        "aeroway_hangar": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}aeroway/hangar",
        },
        "aeroway_helipad": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}aeroway/helipad",
        },
        "aeroway_heliport": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}aeroway/heliport",
        },
        "aeroway_runway": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}aeroway/runway",
        },
        "aeroway_spaceport": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}aeroway/spaceport",
        },
        "aeroway_taxiway": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}aeroway/taxiway",
        },
        "aeroway_terminal": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}aeroway/terminal",
        },
        "amenity_aerialway": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}amenity/aerialway",
        },
        "amenity_alpinecampwild": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}amenity/alpinecampwild",
        },
        "leisure_beach_resort": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}leisure/beach_resort",
        },
        "amenity_fuel": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}amenity/fuel",
        },
        "leisure_golf_course": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}leisure/golf_course",
        },
        "leisure_marina": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}leisure/marina",
        },
        "leisure_pitch": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}leisure/pitch",
        },
        "amenity_sanitary_dump_station": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}amenity/sanitary_dump_station",
        },
        "barrier_city_wall": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}barrier/city_wall",
        },
        "barrier_ditch": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}barrier/ditch",
        },
        "barrier_hedge": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}barrier/hedge",
        },
        "barrier_retaining_wall": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}barrier/retaining_wall",
        },
        "barrier_wall": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}barrier/wall",
        },
        "landuse_basin": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}landuse/basin",
        },
        "landuse_cemetery": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}landuse/cemetery",
        },
        "landuse_industrial": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}landuse/industrial",
        },
        "landuse_landfill": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}landuse/landfill",
        },
        "landuse_quarry": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}landuse/quarry",
        },
        "landuse_salt_pond": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}landuse/salt_pond",
        },
        "landuse_village_green": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}landuse/village_green",
        },
        "man_made_adit": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/adit",
        },
        "man_made_beacon": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/beacon",
        },
        "man_made_breakwater": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/breakwater",
        },
        "man_made_chimney": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/chimney",
        },
        "man_made_communications_tower": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/communications_tower",
        },
        "man_made_dyke": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/dyke",
        },
        "man_made_embankment": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/embankment",
        },
        "man_made_gasometer": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/gasometer",
        },
        "man_made_groyne": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/groyne",
        },
        "man_made_lighthouse": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/lighthouse",
        },
        "man_made_mast": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/mast",
        },
        "man_made_mineshaft": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/mineshaft",
        },
        "man_made_observatorytelescope": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/observatorytelescope",
        },
        "man_made_petroleum_well": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/petroleum_well",
        },
        "man_made_pier": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/pier",
        },
        "man_made_pipeline": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/pipeline",
        },
        "man_made_pumping_station": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/pumping_station",
        },
        "man_made_reservoir_covered": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/reservoir_covered",
        },
        "man_made_silo": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/silo",
        },
        "man_made_snow_fence": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/snow_fence",
        },
        "man_made_storage_tank": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/storage_tank",
        },
        "man_made_tower": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/tower",
        },
        "man_made_wastewater_plant": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/wastewater_plant",
        },
        "man_made_watermill": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/watermill",
        },
        "man_made_water_tower": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/water_tower",
        },
        "man_made_water_well": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/water_well",
        },
        "man_made_water_works": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/water_works",
        },
        "man_made_windmill": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/windmill",
        },
        "man_made_works": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}man_made/works",
        },
        "military_airfield": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}military/airfield",
        },
        "military_ammunition": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}military/ammunition",
        },
        "military_barracks": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}military/barracks",
        },
        "military_bunker": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}military/bunker",
        },
        "military_checkpoint": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}military/checkpoint",
        },
        "military_danger_area": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}military/danger_area",
        },
        "military_naval_base": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}military/naval_base",
        },
        "military_nuclear_explosion_site": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}military/nuclear_explosion_site",
        },
        "military_range": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}military/range",
        },
        "military_trench": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}military/trench",
        },
        "power_cable": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}power/cable",
        },
        "power_heliostat": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}power/heliostat",
        },
        "power_line": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}power/line",
        },
        "power_substation": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}power/substation",
        },
        "power_xbio": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}power/xbio",
        },
        "power_xcoal": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}power/xcoal",
        },
        "power_xhydro": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}power/xhydro",
        },
        "power_xnuclear": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}power/xnuclear",
        },
        "power_xoil": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}power/xoil",
        },
        "power_xother": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}power/xother",
        },
        "power_xsolar": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}power/xsolar",
        },
        "power_xwaste": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}power/xwaste",
        },
        "power_xwind": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}power/xwind",
        },
        "waterway_canal": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}waterway/canal",
        },
        "waterway_dam": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}waterway/dam",
        },
        "waterway_ditch": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}waterway/ditch",
        },
        "waterway_drain": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}waterway/drain",
        },
        "waterway_lock_gate": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}waterway/lock_gate",
        },
        "waterway_weir": {
            "ee_type": EETask.IMAGECOLLECTION,
            "ee_path": f"{ee_hiistatic_osm}waterway/weir",
        },
        "watermask": {
            "ee_type": EETask.IMAGE,
            "ee_path": f"{ee_hiistatic_physical}watermask_jrc70_cciocean",
            "static": True,
        },
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.set_aoi_from_ee("{}/sumatra_poc_aoi".format(self.ee_rootdir))

    def calc(self):
        watermask = ee.Image(self.inputs["watermask"]["ee_path"])

        aeroway_aerodrome, aeroway_aerodrome_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["aeroway_aerodrome"]["ee_path"])
        )
        
        aeroway_apron, aeroway_apron_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["aeroway_apron"]["ee_path"])
        )
        
        aeroway_hangar, aeroway_hangar_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["aeroway_hangar"]["ee_path"])
        )
        
        aeroway_helipad, aeroway_helipad_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["aeroway_helipad"]["ee_path"])
        )
        
        aeroway_heliport, aeroway_heliport_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["aeroway_heliport"]["ee_path"])
        )
        
        aeroway_runway, aeroway_runway_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["aeroway_runway"]["ee_path"])
        )
        
        aeroway_spaceport, aeroway_spaceport_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["aeroway_spaceport"]["ee_path"])
        )
        
        aeroway_taxiway, aeroway_taxiway_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["aeroway_taxiway"]["ee_path"])
        )

        aeroway_terminal, aeroway_terminal_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["aeroway_terminal"]["ee_path"])
        )


        amenity_aerialway, amenity_aerialway_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["amenity_aerialway"]["ee_path"])
        )
        
        amenity_alpinecampwild, amenity_alpinecampwild_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["amenity_alpinecampwild"]["ee_path"])
        )
        
        amenity_fuel, amenity_fuel_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["amenity_fuel"]["ee_path"])
        )
        
        amenity_sanitary_dump_station, amenity_sanitary_dump_station_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["amenity_sanitary_dump_station"]["ee_path"])
        )
        

        barrier_city_wall, barrier_city_wall_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["barrier_city_wall"]["ee_path"])
        )
        
        barrier_ditch, barrier_ditch_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["barrier_ditch"]["ee_path"])
        )
        
        barrier_hedge, barrier_hedge_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["barrier_hedge"]["ee_path"])
        )
        
        barrier_retaining_wall, barrier_retaining_wall_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["barrier_retaining_wall"]["ee_path"])
        )
        
        barrier_wall, barrier_wall_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["barrier_wall"]["ee_path"])
        )
        

        landuse_basin, landuse_basin_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["landuse_basin"]["ee_path"])
        )
        
        landuse_cemetery, landuse_cemetery_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["landuse_cemetery"]["ee_path"])
        )
        
        landuse_industrial, landuse_industrial_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["landuse_industrial"]["ee_path"])
        )
        
        landuse_landfill, landuse_landfill_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["landuse_landfill"]["ee_path"])
        )
        
        landuse_quarry, landuse_quarry_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["landuse_quarry"]["ee_path"])
        )
        
        landuse_salt_pond, landuse_salt_pond_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["landuse_salt_pond"]["ee_path"])
        )
        
        landuse_village_green, landuse_village_green_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["landuse_village_green"]["ee_path"])
        )
        

        leisure_beach_resort, leisure_beach_resort_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["leisure_beach_resort"]["ee_path"])
        )
        
        leisure_golf_course, leisure_golf_course_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["leisure_golf_course"]["ee_path"])
        )
        
        leisure_marina, leisure_marina_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["leisure_marina"]["ee_path"])
        )
        
        leisure_pitch, leisure_pitch_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["leisure_pitch"]["ee_path"])
        )
        

        man_made_adit, man_made_adit_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_adit"]["ee_path"])
        )
        
        man_made_beacon, man_made_beacon_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_beacon"]["ee_path"])
        )
        
        man_made_breakwater, man_made_breakwater_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_breakwater"]["ee_path"])
        )
        
        man_made_chimney, man_made_chimney_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_chimney"]["ee_path"])
        )
        
        man_made_communications_tower, man_made_communications_tower_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_communications_tower"]["ee_path"])
        )
        
        man_made_dyke, man_made_dyke_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_dyke"]["ee_path"])
        )
        
        man_made_embankment, man_made_embankment_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_embankment"]["ee_path"])
        )
        
        man_made_gasometer, man_made_gasometer_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_gasometer"]["ee_path"])
        )

        man_made_groyne, man_made_groyne_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_groyne"]["ee_path"])
        )

        man_made_lighthouse, man_made_lighthouse_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_lighthouse"]["ee_path"])
        )
        
        man_made_mast, man_made_mast_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_mast"]["ee_path"])
        )
        
        man_made_mineshaft, man_made_mineshaft_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_mineshaft"]["ee_path"])
        )
        
        man_made_observatorytelescope, man_made_observatorytelescope_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_observatorytelescope"]["ee_path"])
        )
        
        man_made_petroleum_well, man_made_petroleum_well_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_petroleum_well"]["ee_path"])
        )
        
        man_made_pier, man_made_pier_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_pier"]["ee_path"])
        )
        
        man_made_pipeline, man_made_pipeline_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_pipeline"]["ee_path"])
        )
        
        man_made_pumping_station, man_made_pumping_station_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_pumping_station"]["ee_path"])
        )

        man_made_reservoir_covered, man_made_reservoir_covered_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_reservoir_covered"]["ee_path"])
        )

        man_made_silo, man_made_silo_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_silo"]["ee_path"])
        )
        
        man_made_snow_fence, man_made_snow_fence_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_snow_fence"]["ee_path"])
        )
        
        man_made_storage_tank, man_made_storage_tank_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_storage_tank"]["ee_path"])
        )
        
        man_made_tower, man_made_tower_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_tower"]["ee_path"])
        )
        
        man_made_wastewater_plant, man_made_wastewater_plant_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_wastewater_plant"]["ee_path"])
        )
        
        man_made_water_tower, man_made_water_tower_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_water_tower"]["ee_path"])
        )
        
        man_made_water_well, man_made_water_well_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_water_well"]["ee_path"])
        )
        
        man_made_water_works, man_made_water_works_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_water_works"]["ee_path"])
        )

        man_made_watermill, man_made_watermill_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_watermill"]["ee_path"])
        )

        man_made_windmill, man_made_windmill_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_windmill"]["ee_path"])
        )

        man_made_works, man_made_works_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["man_made_works"]["ee_path"])
        )


        military_airfield, military_airfield_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["military_airfield"]["ee_path"])
        )
        
        military_ammunition, military_ammunition_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["military_ammunition"]["ee_path"])
        )
        
        military_barracks, military_barracks_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["military_barracks"]["ee_path"])
        )
        
        military_bunker, military_bunker_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["military_bunker"]["ee_path"])
        )
        
        military_checkpoint, military_checkpoint_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["military_checkpoint"]["ee_path"])
        )
        
        military_danger_area, military_danger_area_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["military_danger_area"]["ee_path"])
        )
        
        military_naval_base, military_naval_base_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["military_naval_base"]["ee_path"])
        )
        
        military_nuclear_explosion_site, military_nuclear_explosion_site_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["military_nuclear_explosion_site"]["ee_path"])
        )

        military_range, military_range_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["military_range"]["ee_path"])
        )

        military_trench, military_trench_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["military_trench"]["ee_path"])
        )


        power_cable, power_cable_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["power_cable"]["ee_path"])
        )
        
        power_heliostat, power_heliostat_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["power_heliostat"]["ee_path"])
        )
        
        power_line, power_line_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["power_line"]["ee_path"])
        )
        
        power_substation, power_substation_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["power_substation"]["ee_path"])
        )
        
        power_xbio, power_xbio_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["power_xbio"]["ee_path"])
        )
        
        power_xcoal, power_xcoal_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["power_xcoal"]["ee_path"])
        )
        
        power_xhydro, power_xhydro_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["power_xhydro"]["ee_path"])
        )
        
        power_xnuclear, power_xnuclear_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["power_xnuclear"]["ee_path"])
        )

        power_xoil, power_xoil_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["power_xoil"]["ee_path"])
        )

        power_xother, power_xother_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["power_xother"]["ee_path"])
        )
        
        power_xsolar, power_xsolar_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["power_xsolar"]["ee_path"])
        )
        
        power_xwaste, power_xwaste_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["power_xwaste"]["ee_path"])
        )
        
        power_xwind, power_xwind_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["power_xwind"]["ee_path"])
        )


        waterway_canal, waterway_canal_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["waterway_canal"]["ee_path"])
        )
        
        waterway_dam, waterway_dam_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["waterway_dam"]["ee_path"])
        )
        
        waterway_ditch, waterway_ditch_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["waterway_ditch"]["ee_path"])
        )
        
        waterway_drain, waterway_drain_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["waterway_drain"]["ee_path"])
        )
        
        waterway_lock_gate, waterway_lock_gate_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["waterway_lock_gate"]["ee_path"])
        )
        
        waterway_weir, waterway_weir_date = self.get_most_recent_image(
            ee.ImageCollection(self.inputs["waterway_weir"]["ee_path"])
        )
        

        aeroway_total = (aeroway_aerodrome.multiply(self.aeroway_aerodrome_weighting)
            .add(aeroway_apron.multiply(self.aeroway_apron_weighting))
            .add(aeroway_hangar.multiply(self.aeroway_hangar_weighting))
            .add(aeroway_helipad.multiply(self.aeroway_helipad_weighting))
            .add(aeroway_heliport.multiply(self.aeroway_heliport_weighting))
            .add(aeroway_runway.multiply(self.aeroway_runway_weighting))
            .add(aeroway_spaceport.multiply(self.aeroway_spaceport_weighting))
            .add(aeroway_taxiway.multiply(self.aeroway_taxiway_weighting))
            .add(aeroway_terminal.multiply(self.aeroway_terminal_weighting))
        )

        amenity_total = (amenity_aerialway.multiply(self.amenity_aerialway_weighting)
            .add(amenity_alpinecampwild.multiply(self.amenity_alpinecampwild_weighting))
            .add(amenity_fuel.multiply(self.amenity_fuel_weighting))
            .add(amenity_sanitary_dump_station.multiply(self.amenity_sanitary_dump_station_weighting))
        )


        barrier_total = (barrier_city_wall.multiply(self.barrier_city_wall_weighting)
            .add(barrier_ditch.multiply(self.barrier_ditch_weighting))
            .add(barrier_hedge.multiply(self.barrier_hedge_weighting))
            .add(barrier_retaining_wall.multiply(self.barrier_retaining_wall_weighting))
            .add(barrier_wall.multiply(self.barrier_wall_weighting))
        )

        landuse_total = (landuse_basin.multiply(self.landuse_basin_weighting)
            .add(landuse_cemetery.multiply(self.landuse_cemetery_weighting))
            .add(landuse_industrial.multiply(self.landuse_industrial_weighting))
            .add(landuse_landfill.multiply(self.landuse_landfill_weighting))
            .add(landuse_quarry.multiply(self.landuse_quarry_weighting))
            .add(landuse_salt_pond.multiply(self.landuse_salt_pond_weighting))
            .add(landuse_village_green.multiply(self.landuse_village_green_weighting))
        )

        leisure_total = (leisure_beach_resort.multiply(self.leisure_beach_resort_weighting)
            .add(leisure_golf_course.multiply(self.leisure_golf_course_weighting))
            .add(leisure_marina.multiply(self.leisure_marina_weighting))
            .add(leisure_pitch.multiply(self.leisure_pitch_weighting))
        )

        man_made_total = (man_made_adit.multiply(self.man_made_adit_weighting)
            .add(man_made_beacon.multiply(self.man_made_beacon_weighting))
            .add(man_made_breakwater.multiply(self.man_made_breakwater_weighting))
            .add(man_made_chimney.multiply(self.man_made_chimney_weighting))
            .add(man_made_communications_tower.multiply(self.man_made_communications_tower_weighting))
            .add(man_made_dyke.multiply(self.man_made_dyke_weighting))
            .add(man_made_embankment.multiply(self.man_made_embankment_weighting))
            .add(man_made_gasometer.multiply(self.man_made_gasometer_weighting))
            .add(man_made_groyne.multiply(self.man_made_groyne_weighting))
            .add(man_made_lighthouse.multiply(self.man_made_lighthouse_weighting))
            .add(man_made_mast.multiply(self.man_made_mast_weighting))
            .add(man_made_mineshaft.multiply(self.man_made_mineshaft_weighting))
            .add(man_made_observatorytelescope.multiply(self.man_made_observatorytelescope_weighting))
            .add(man_made_petroleum_well.multiply(self.man_made_petroleum_well_weighting))
            .add(man_made_pier.multiply(self.man_made_pier_weighting))
            .add(man_made_pipeline.multiply(self.man_made_pipeline_weighting))
            .add(man_made_pumping_station.multiply(self.man_made_pumping_station_weighting))
            .add(man_made_reservoir_covered.multiply(self.man_made_reservoir_covered_weighting))
            .add(man_made_silo.multiply(self.man_made_silo_weighting))
            .add(man_made_snow_fence.multiply(self.man_made_snow_fence_weighting))
            .add(man_made_storage_tank.multiply(self.man_made_storage_tank_weighting))
            .add(man_made_tower.multiply(self.man_made_tower_weighting))
            .add(man_made_wastewater_plant.multiply(self.man_made_wastewater_plant_weighting))
            .add(man_made_watermill.multiply(self.man_made_watermill_weighting))
            .add(man_made_water_tower.multiply(self.man_made_water_tower_weighting))
            .add(man_made_water_well.multiply(self.man_made_water_well_weighting))
            .add(man_made_water_works.multiply(self.man_made_water_works_weighting))
            .add(man_made_windmill.multiply(self.man_made_windmill_weighting))
            .add(man_made_works.multiply(self.man_made_works_weighting))
        )

        military_total = (military_airfield.multiply(self.military_airfield_weighting)
            .add(military_ammunition.multiply(self.military_ammunition_weighting))
            .add(military_barracks.multiply(self.military_barracks_weighting))
            .add(military_bunker.multiply(self.military_bunker_weighting))
            .add(military_checkpoint.multiply(self.military_checkpoint_weighting))
            .add(military_danger_area.multiply(self.military_danger_area_weighting))
            .add(military_naval_base.multiply(self.military_naval_base_weighting))
            .add(military_nuclear_explosion_site.multiply(self.military_nuclear_explosion_site_weighting))
            .add(military_range.multiply(self.military_range_weighting))
            .add(military_trench.multiply(self.military_trench_weighting))
        )

        power_total = (power_cable.multiply(self.power_cable_weighting)
            .add(power_heliostat.multiply(self.power_heliostat_weighting))
            .add(power_line.multiply(self.power_line_weighting))
            .add(power_substation.multiply(self.power_substation_weighting))
            .add(power_xbio.multiply(self.power_xbio_weighting))
            .add(power_xcoal.multiply(self.power_xcoal_weighting))
            .add(power_xhydro.multiply(self.power_xhydro_weighting))
            .add(power_xnuclear.multiply(self.power_xnuclear_weighting))
            .add(power_xoil.multiply(self.power_xoil_weighting))
            .add(power_xother.multiply(self.power_xother_weighting))
            .add(power_xsolar.multiply(self.power_xsolar_weighting))
            .add(power_xwaste.multiply(self.power_xwaste_weighting))
            .add(power_xwind.multiply(self.power_xwind_weighting))
        )

        waterway_total = (waterway_canal.multiply(self.waterway_canal_weighting)
            .add(waterway_dam.multiply(self.waterway_dam_weighting))
            .add(waterway_ditch.multiply(self.waterway_ditch_weighting))
            .add(waterway_drain.multiply(self.waterway_drain_weighting))
            .add(waterway_lock_gate.multiply(self.waterway_lock_gate_weighting))
            .add(waterway_weir.multiply(self.waterway_weir_weighting))
        )

        osm = aeroway_total\
            .add(amenity_total)\
            .add(barrier_total)\
            .add(landuse_total)\
            .add(leisure_total)\
            .add(man_made_total)\
            .add(military_total)\
            .add(power_total)\
            .add(waterway_total)\
            .multiply(2)



        current_infra = osm.updateMask(watermask)

        self.export_image_ee(
            current_infra,
            "{}/{}".format(self.ee_driverdir, "hii_infrastructure_driver"),
        )

    def check_inputs(self):
        super().check_inputs()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--taskdate", default=datetime.now(timezone.utc).date())
    options = parser.parse_args()
    infrastructure_task = HIIInfrastructure(**vars(options))
    infrastructure_task.run()