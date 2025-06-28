import os
import json

def verify_chunks(original_txt_path, chunk_json_path):
    # Load original text
    with open(original_txt_path, 'r', encoding='utf-8') as f:
        original_text = f.read()
    
    original_len = len(original_text)
    original_lines = original_text.count('\n') + 1
    
    # Load chunked JSON data
    with open(chunk_json_path, 'r', encoding='utf-8') as f:
        chunks = json.load(f)
    
    # Combine all chunk texts into one big string
    combined_text = ''
    for chunk in chunks:
        # chunk['text'] or chunk depending on your JSON structure
        # Adjust this if chunk structure differs
        if isinstance(chunk, dict) and 'text' in chunk:
            combined_text += chunk['text']
        else:
            # If chunk is just a string
            combined_text += str(chunk)
    
    combined_len = len(combined_text)
    combined_lines = combined_text.count('\n') + 1

    print(f"Original file: {os.path.basename(original_txt_path)}")
    print(f"Original length (chars): {original_len}")
    print(f"Original lines: {original_lines}")
    print(f"Combined chunks length (chars): {combined_len}")
    print(f"Combined chunks lines: {combined_lines}")
    
    if combined_len == original_len:
        print("✅ Character counts match exactly.")
    else:
        print(f"⚠️ Character count mismatch: {original_len - combined_len} characters difference.")
    
    if combined_lines == original_lines:
        print("✅ Line counts match exactly.")
    else:
        print(f"⚠️ Line count mismatch: {original_lines - combined_lines} lines difference.")

    print(f"Number of chunks: {len(chunks)}")
    print('-' * 40)

# Example usage:
RAW_PATH = r"C:\Ordinance\data\raw"
CHUNK_PATH = r"C:\Ordinance\data\chunks"

file_pairs = [
    ("Chapter__2-4.txt", "chapter_2-4_provisions_for_selling,_distributing_and_consuming_alcohol.json"),
    ("Chapter__6-5.txt", "chapter__6-5_garbage_provisions.json"),
    ("Chapter__6-6.txt", "chapter__6-6_bicycles.json"),
    ("Chapter__6-7.txt", "chapter__6-7_ambulance_services.json"),
    ("Chapter_1-1.txt", "chapter_1-1_name,_boundaries,_power_and_general_provisions.json"),
    ("Chapter_1-2.txt", "chapter_1-2_elections.json"),
    ("Chapter_1-3.txt", "chapter_1-3_the_mayor,_city_council_&_committees.json"),
    ("Chapter_1-4.txt", "chapter_1-4_city_appointive_officials.json"),
    ("Chapter_1-5.txt", "chapter_1-5_duties_and_compensation_of_appointive_officials.json"),
    ("Chapter_1-6.txt", "chapter_1-6_financial_regulations.json"),
    ("Chapter_1-7.txt", "chapter_1-7_code_of_conduct;_federal_grants.json"),
    ("Chapter_1-8.txt", "chapter_1-8_finance.json"),
    ("Chapter_1-9.txt", "chapter_1-9_records.json"),
    ("Chapter_1-10.txt", "chapter_1-10_section_in_general.json"),
    ("Chapter_1-11.txt", "chapter_1-11_establishing_planning_&_zoning_commission.json"),
    ("Chapter_2-1.txt", "chapter_2-1_alcoholic_beverages.json"),
    ("Chapter_2-2.txt", "chapter_2-2_general.json"),
    ("Chapter_2-3.txt", "chapter_2-3_licensing.json"),
    ("Chapter_3-1.txt", "chapter_3-1_animals.json"),
    ("Chapter_3-2.txt", "chapter_3-2_animals.json"),
    ("Chapter_3-3.txt", "chapter_3-3_livestock.json"),
    ("Chapter_3-4.txt", "chapter_3-4_fowl.json"),
    ("Chapter_4-1.txt", "chapter_4-1_adoption_of_national_code.json"),
    ("Chapter_4-4.txt", "chapter_4-4_buildings_to_be_moved.json"),
    ("Chapter_4-5.txt", "chapter_4-5_building_provisions_generally.json"),
    ("Chapter_4-6.txt", "chapter_4-6_assignment_of_building_numbers.json"),
    ("Chapter_4-7.txt", "chapter_4-7_abatement_of_dangerous_buildings.json"),
    ("Chapter_4-8.txt", "chapter_4-8_certificate_of_occupancy.json"),
    ("Chapter_5-1.txt", "chapter_5-1_rules_and_regulations_of_the_state_fire_marshalls_office.json"),
    ("Chapter_5-2.txt", "chapter_5-2_fire_protection.json"),
    ("Chapter_6-1.txt", "chapter_6-1_general_provisions_with_regard_to_licenses.json"),
    ("Chapter_6-2.txt", "chapter_6-2_contractor’s_license_provisions.json"),
    ("Chapter_6-3.txt", "chapter_6-3_peddlers_and_vendors.json"),
    ("Chapter_6-4.txt", "chapter_6-4_landscape_irrigation_contractors.json"),
    ("Chapter_6-8.txt", "chapter_6-8_sewer_cleaning_services.json"),
    ("Chapter_6-9.txt", "chapter_6-9_video_lottery_machines.json"),
    ("Chapter_6-10.txt", "chapter_6-10_tree_pesticide_applicators_license.json"),
    ("Chapter_7-1.txt", "chapter_7-1_fireworks.json"),
    ("Chapter_7-2.txt", "chapter_7-2_public_nuisances.json"),
    ("Chapter_7-3.txt", "chapter_7-3_specific_offenses.json"),
    ("Chapter_7-4.txt", "chapter_7-4_prostitution,_gambling,_and_indecency.json"),
    ("Chapter_7-5.txt", "chapter_7-5_offenses_against_the_public_peace.json"),
    ("Chapter_7-6.txt", "chapter_7-6_minors.json"),
    ("Chapter_7-7.txt", "chapter_7-7_junk.json"),
    ("Chapter_7-10.txt", "chapter_7-10_chapter_7-10.json"),
    ("Chapter_8-1.txt", "chapter_8-1_pawnbrokers_-_purpose_&_definitions.json"),
    ("Chapter_8-2.txt", "chapter_8-2_pawnbrokers_-_license.json"),
    ("Chapter_8-3.txt", "chapter_8-3_pawnbrokers_-_records.json"),
    ("Chapter_8-4.txt", "chapter_8-4_pawnbrokers_-_bookkeeping_requirements.json"),
    ("Chapter_8-5.txt", "chapter_8-5_pawnbrokers_-_general.json"),
    ("Chapter_8-6.txt", "chapter_8-6_adult_use_-_definitions.json"),
    ("Chapter_8-7.txt", "chapter_8-7_adult_uses_-_regulations.json"),
    ("Chapter_8-8.txt", "chapter_8-8_adult_uses_-licensing.json"),
    ("Chapter_8-9.txt", "chapter_8-9_adult_uses_-_performer_restrictions_and_requirements.json"),
    ("Chapter_10-1.txt", "chapter_10-1_sidewalks_and_alleys_-_general.json"),
    ("Chapter_10-2.txt", "chapter_10-2_snow_and_ice_removal.json"),
    ("Chapter_10-3.txt", "chapter_10-3_excavations_in_public_areas.json"),
    ("Chapter_10-4.txt", "chapter_10-4_public_grounds_in_general.json"),
    ("Chapter_11-1.txt", "chapter_11-1_municipal_sales_and_service_tax.json"),
    ("Chapter_11-2.txt", "chapter_11-2_special_tax_classification.json"),
    ("Chapter_11-3.txt", "chapter_11-3_county_tax_levy.json"),
    ("Chapter_11-4.txt", "chapter_11-4_municipal_sales_and_service_tax.json"),
    ("Chapter_11-6.txt", "chapter_11-6_special_assessments.json"),
    ("Chapter_12-1.txt", "chapter_12-1_in_general.json"),
    ("Chapter_12-2.txt", "chapter_12-2_enforcement_and_obedience.json"),
    ("Chapter_12-3.txt", "chapter_12-3_procedures_upon_arrest.json"),
    ("Chapter_12-4.txt", "chapter_12-4_accidents.json"),
    ("Chapter_12-5.txt", "chapter_12-5_operation_of_vehicles_generally.json"),
    ("Chapter_12-6.txt", "chapter_12-6_right-of-way_regulations.json"),
    ("Chapter_12-7.txt", "chapter_12-7_traffic_control_signs,_signals_and_devices.json"),
    ("Chapter_12-8.txt", "chapter_12-8_speed.json"),
    ("Chapter_12-9.txt", "chapter_12-9_one-way_streets_and_alleys.json"),
    ("Chapter_12-10.txt", "chapter_12-10_turns.json"),
    ("Chapter_12-11.txt", "chapter_12-11_turning_and_stopping_signals.json"),
    ("Chapter_12-12.txt", "chapter_12-12_required_stops_and_yield_intersections.json"),
    ("Chapter_12-13.txt", "chapter_12-13_miscellaneous_driving_rules.json"),
    ("Chapter_12-14.txt", "chapter_12-14_standing_and_parking.json"),
    ("Chapter_12-15.txt", "chapter_12-15_pedestrians.json"),
    ("Chapter_12-16.txt", "chapter_12-16_snowmobiles.json"),
    ("Chapter_12-17.txt", "chapter_12-17_truck_route_system.json"),
    ("Chapter_12-18.txt", "chapter_12-18_motorcycles_and_mopeds.json"),
    ("Chapter_12-19.txt", "chapter_12-19_motor_vehicles.json"),
    ("Chapter_12-20.txt", "chapter_12-20_abandoned_vehicles.json"),
    ("Chapter_12-21.txt", "chapter_12-21_golf_cart_use_in_city_limits.json"),
    ("Chapter_13-1.txt", "chapter_13-1_trees_and_noxious_vegetation.json"),
    ("Chapter_13-2.txt", "chapter_13-2_noxious_weeds.json"),
    ("Chapter_14-2.txt", "chapter_14-2_regulation_of_water_use.json"),
    ("Chapter_14-3.txt", "chapter_14-3_water_and_sewer_service_in_general.json"),
    ("Chapter_14-4.txt", "chapter_14-4_rates_and_charges.json"),
    ("Chapter_14-5.txt", "chapter_14-5_wastewater_service_charges.json"),
    ("Chapter_14-6.txt", "chapter_14-6_gas_energy.json"),
    ("Chapter_14-7.txt", "chapter_14-7_cable_television_franchise.json"),
    ("Chapter_14-8.txt", "chapter_14-8_telephone_franchise.json"),
    ("Chapter_14-9.txt", "chapter_14-9_electricity_franchise.json"),
    ("Chapter_14-10.txt", "chapter_14-10_street_lighting_service.json"),
    ("Chapter_14-11.txt", "chapter_14-11_regulating_small_cell_facilities.json"),
    ("Chapter_14-12.txt", "chapter_14-12_stormwater_utility_fee.json"),
    ("Chapter_14-41.txt", "chapter_14-41_regulation_of_sewer_use.json"),
    ("Chapter_16-1.txt", "chapter_16-1_2013_revised_subdivision_ordinance_for_the_city_of_brandon.json"),
    ("Chapter_16-2.txt", "chapter_16-2_subdivision_plans_approval_process.json"),
    ("Chapter_16-3.txt", "chapter_16-3_concept_plan.json"),
    ("Chapter_16-4.txt", "chapter_16-4_preliminary_subdivision_plan.json"),
    ("Chapter_16-5.txt", "chapter_16-5_development_engineering_plans_and_the_plat.json"),
    ("Chapter_16-6.txt", "chapter_16-6_preliminary_plan_criteria.json"),
    ("Chapter_16-7.txt", "chapter_16-7_development_engineering_plan_criteria.json"),
    ("Chapter_16-8.txt", "chapter_16-8_utilities_and_public_space.json"),
    ("Chapter_16-9.txt", "chapter_16-9_grading_and_drainage.json"),
    ("Chapter_16-10.txt", "chapter_16-10_erosion_control_plan.json"),
    ("Chapter_16-11.txt", "chapter_16-11_preservation_of_natural_features_and_amenities.json"),
    ("Chapter_16-12.txt", "chapter_16-12_rural_subdivisions.json"),
    ("Chapter_16-13.txt", "chapter_16-13_assurances_for_the_completion_of_minimum.json"),
    ("Chapter_16-14.txt", "chapter_16-14_certificates_required.json"),
    ("Chapter_16-15.txt", "chapter_16-15_construction_of_improvements_and_acceptance.json"),
    ("Chapter_16-16.txt", "chapter_16-16_easements.json"),
    ("Chapter_17-1.txt", "chapter_17-1_medical_cannabis.json"),
    ("Flood_Plain_Ordinance_-_Appendix_A.txt", "flood_plain_ordinance_-_appendix_a.json"),
    ("Zoning_Ordinances_-_Effective_05-21-2025.txt", "zoning_ordinances_-_effective_05-21-2025.json")
]


for txt_file, json_file in file_pairs:
    original_path = os.path.join(RAW_PATH, txt_file)
    chunk_path = os.path.join(CHUNK_PATH, json_file)
    verify_chunks(original_path, chunk_path)
