import requests
import json
import argparse
import os
import csv
import time

# Get library names either from the argument or through LIVUS
def get_library_names():
    if args.name:
        return [args.name]
    else:
        with open('../out/exec/predictions.txt', 'r') as file:
            return [line.strip() for line in file]

# Fetch JSON data from the provided URL with a buffer between requests
def get_json_data(url):
    response = requests.get(url)

    # If the request was unsuccessful, print the error and exit
    if response.status_code != 200:
        print(f"Error occurred while fetching JSON data: {response.status_code}")
        exit()

    return response.json()

# Save JSON data to the provided file
def save_json_data(file_path_json, json_data):
    with open(file_path_json, "w") as file:
        json.dump(json_data, file)

# Load JSON data from the provided file
def load_json_data(file_path_json):
    with open(file_path_json, "r") as file:
        return json.load(file)

# Delete all files in the target directory to avoid collisions
def remove_files_in_directory(directory):
    file_list = os.listdir(directory)
    for file_name in file_list:
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            os.rmdir(file_path)

# Append new JSON data to the existing data in the file
def append_new_data(file_path_json, new_json_data):
    existing_data = load_json_data(file_path_json)
    existing_data["vulnerabilities"].extend(new_json_data["vulnerabilities"])
    save_json_data(file_path_json, existing_data)

# Extract CVE data from the JSON data
def get_cve_data(json_data):
    cve_data = []
    for vulnerability in json_data["vulnerabilities"]:
        cve_id = vulnerability["cve"]["id"]
        published = vulnerability["cve"]["published"]
        descriptions = vulnerability["cve"].get("descriptions", [])
        description = ""
        for desc in descriptions:
            if "value" in desc and desc.get("lang", "") == "en":
                description = desc["value"]
                break 
        base_score = f'V3.1: {next((metric["cvssData"]["baseScore"] for metric in vulnerability["cve"].get("metrics", {}).get("cvssMetricV31", []) if "cvssData" in metric and "baseScore" in metric["cvssData"]), None)}'
        if base_score == 'V3.1: None':
            base_score = f'V3.0: {next((metric["cvssData"]["baseScore"] for metric in vulnerability["cve"].get("metrics", {}).get("cvssMetricV30", []) if "cvssData" in metric and "baseScore" in metric["cvssData"]), None)}'
            if base_score == 'V3.0: None':
                base_score = f'V2: {next((metric["cvssData"]["baseScore"] for metric in vulnerability["cve"].get("metrics", {}).get("cvssMetricV2", []) if "cvssData" in metric and "baseScore" in metric["cvssData"]), None)}'
        cve_data.append([cve_id, published, description, base_score])
    return cve_data

# Save data to the CSV file
def save_to_csv(file_path_csv, data):
    with open(file_path_csv, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["CVE ID", "Published", "Description", "Base Score"])
        writer.writerows(data)

def main():
    target_path = "../out/exec/CVE_results"
    remove_files_in_directory(target_path)
    library_names = get_library_names()
    dos_buffer = 10  # Add a buffer between the GET requests to avoid being blocked by the NVD API

    for library_name in library_names:
        print(f"Searching for {library_name}...")
        url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={library_name}"
        json_data = get_json_data(url)

        if json_data["totalResults"] == 0:
            print(f"No vulnerabilities found for {library_name}.")
            continue

        file_path_json = f"{target_path}/{library_name}.json"
        file_path_csv = f"{target_path}/{library_name}.csv"
        save_json_data(file_path_json, json_data)
        total_results = json_data["totalResults"]
        results_per_page = json_data["resultsPerPage"]
        start_index = results_per_page

        while total_results > results_per_page:
            url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={library_name}&startIndex={start_index}"
            new_json_data = get_json_data(url)
            append_new_data(file_path_json, new_json_data)
            print("Another page appended")
            total_results -= results_per_page
            start_index += results_per_page
            time.sleep(dos_buffer)

        print(f"Processing the CVE data...")
        cve_data = get_cve_data(load_json_data(file_path_json))
        save_to_csv(file_path_csv, cve_data)
        print("Saved to file")
        time.sleep(dos_buffer)


# Parse command line arguments
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="NVD Parser",
        description="Parse the NVD Database either to receive CVEs for multiple libraries or input a library through the CLI",
        epilog="To use the NVD Parser for multiple libraries, provide the path to the input file containing one library name per line.",
    )
    parser.add_argument("-n", "--name", help="Specify the library name or a keyword to search for.")
    args = parser.parse_args()
    main()
