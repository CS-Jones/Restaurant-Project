# Restaurant Project 

A lightweight Python script that leverages the **Google Places API** to programmatically discover, filter, and extract detailed information about restaurants within a specified geographic radius.

## 🚀 Features

* **Geocoding Integration:** Automatically converts a string address into geographic coordinates (Latitude and Longitude).
* **Radius-Based Searching:** Converts search radiuses from miles to meters natively to seamlessly feed into the Google Maps Client.
* **Pagination Support:** Automatically handles Google's `next_page_token` to fetch comprehensive results beyond the initial API response page.
* **Granular Detail Fetching:** Extracts specific fields such as `name`, `type`, `vicinity`, and `rating` for deep-dive location profiling.

## 🛠️ Tech Stack & Dependencies

* **Language:** Python 3.x
* **Core Libraries:**
  * `googlemaps` - Official Python client library for Google Maps Platform services.
  * `pandas` - Data manipulation tool.
  * `pprint` - Pretty-printing data structures for clean console debugging.

## 📋 Prerequisites

Before running the script, you must have a Google Cloud Project with the **Places API** and **Geocoding API** enabled.

1. Go to the [Google Cloud Console](https://google.com).
2. Create a project and generate an **API Key**.
3. Restrict your API key to the Geocoding and Places APIs for security.

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd YOUR_REPO_NAME
   ```

2. **Install dependencies:**
   ```bash
   pip install googlemaps pandas
   ```

3. **Configure your API Key:**
   Create a file named `API_KEY.txt` in the root directory of the project and paste your raw Google API key inside it:
   ```text
   AIzaSyYourActualGoogleApiKeyGoesHere...
   ```

## 💻 Usage

1. Open the script and define your target address variable:
   ```python
   address = 'Times Square, New York, NY'  # Add your target location here
   ```

2. Adjust your search radius (in miles) and search types if needed:
   ```python
   search_type = 'restaurant'
   distance = miles_to_meters(5) # Find places within 5 miles
   ```

3. Run the script:
   ```bash
   python main.py
   ```

## 🗺️ Roadmap & Next Steps

* [ ] Fix the empty `address` variable constraint to accept dynamic CLI arguments.
* [ ] Complete the JSON-to-Dictionary parsing layer to automatically strip unwanted business types (like `meal_delivery`).
* [ ] Export the final aggregated data list into a structured `.csv` or `.xlsx` spreadsheet using `pandas`.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
