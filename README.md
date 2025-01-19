# Weather Dashboard 🌤️

A dynamic weather information dashboard that fetches and displays real-time weather details for any city, including a 3-day forecast. The project is built using Django, HTML, CSS, and JavaScript.

# Features

-  **Real-Time Weather Information**: Displays current temperature, wind speed, and weather description for a user-specified city.
-  **3-Day Forecast**: Provides a detailed forecast for the next three days, including temperature and wind speed.
-  **Responsive Design**: Mobile-friendly layout for seamless viewing on any device.
-  **Error Handling**: Displays user-friendly error messages for invalid or missing data.
-  **Background Animation**: Optional background video to enhance visual appeal.
-  **Alert Auto-hide**: Error messages disappear automatically after 2.5 seconds.

# Tech Stack 🛠️
-  **Backend**: Django
-  **Frontend**: HTML, CSS, JavaScript
-  **Database**: N/A (Weather data fetched via an API)
-  **Styling**: Custom CSS animations and transitions
-  **APIs Used**: OpenWeatherMap (or any weather API)

weather-dashboard/ <br>
│  <br>
├── templates/  <br>
│   ├── index.html          # Main HTML template  <br>
├── static/  <br>
│   ├── css/  <br>
│   │   └── index.css       # Styling  <br>
│   ├── videos/  <br>
│   │   └── background.mp4  # Background video (optional)  <br>
├── views.py                # Django views for processing data  <br>
├── models.py               # Django models (if required)  <br>
├── requirements.txt        # Project dependencies  <br>
├── README.md               # Project README  <br>

# Usage 🖥️
1. Enter the city name in the input field and click "Search."
2. View the current weather details and the 3-day forecast.
3. If the city is invalid, an error message will appear briefly.

# UI View

![Image](https://github.com/user-attachments/assets/5644d879-2f2d-4b64-b667-332b71fde7fc) <br>

![Image](https://github.com/user-attachments/assets/cb814ef9-558c-4381-b881-957bd02434ba)
