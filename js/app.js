// Crop Recommendation Platform Core JavaScript

// Base URL for backend prediction server REST API
const API_BASE = window.location.origin.includes("5000") ? "" : "http://127.0.0.1:5000";

// Crop Database with Optimal Conditions for Euclidean distance matching
const cropsDb = [
  { crop: "Rice", n: 80, p: 48, k: 40, ph: 6.4 },
  { crop: "Maize", n: 78, p: 48, k: 20, ph: 6.2 },
  { crop: "Chickpea", n: 40, p: 68, k: 80, ph: 7.3 },
  { crop: "Kidney Beans", n: 21, p: 68, k: 20, ph: 5.7 },
  { crop: "Pigeon Peas", n: 21, p: 68, k: 20, ph: 5.8 },
  { crop: "Moth Beans", n: 21, p: 48, k: 20, ph: 6.8 },
  { crop: "Mung Bean", n: 21, p: 47, k: 20, ph: 6.7 },
  { crop: "Black Gram", n: 40, p: 67, k: 19, ph: 7.1 },
  { crop: "Lentil", n: 19, p: 68, k: 19, ph: 6.9 },
  { crop: "Pomegranate", n: 19, p: 19, k: 40, ph: 6.4 },
  { crop: "Banana", n: 100, p: 82, k: 50, ph: 6.0 },
  { crop: "Mango", n: 20, p: 27, k: 30, ph: 5.8 },
  { crop: "Grapes", n: 23, p: 133, k: 200, ph: 6.0 },
  { crop: "Watermelon", n: 99, p: 17, k: 50, ph: 6.5 },
  { crop: "Muskmelon", n: 100, p: 18, k: 50, ph: 6.4 },
  { crop: "Apple", n: 21, p: 134, k: 200, ph: 5.9 },
  { crop: "Orange", n: 20, p: 17, k: 10, ph: 7.0 },
  { crop: "Papaya", n: 50, p: 59, k: 50, ph: 6.7 },
  { crop: "Coconut", n: 22, p: 17, k: 31, ph: 6.0 },
  { crop: "Cotton", n: 118, p: 46, k: 20, ph: 6.9 },
  { crop: "Jute", n: 78, p: 47, k: 40, ph: 6.7 },
  { crop: "Coffee", n: 101, p: 29, k: 30, ph: 6.8 }
];

// Mock Weather Data Repository
const weatherData = {
  "pune": {
    city: "Pune, Maharashtra", temp: 28, humidity: 62, moisture: "Medium (45%)", rainfall: 85, uv: 6,
    alert: "Moderate Humidity. Watch out for downy mildew in vine crops.",
    forecast: [
      { day: "Wed", temp: 29, rain: "10%", action: "Apply fertilizer" },
      { day: "Thu", temp: 28, rain: "20%", action: "Tillage" },
      { day: "Fri", temp: 27, rain: "55%", action: "Postpone spray" },
      { day: "Sat", temp: 26, rain: "80%", action: "Rain Harvesting" },
      { day: "Sun", temp: 28, rain: "15%", action: "Manual weeding" }
    ]
  },
  "ludhiana": {
    city: "Ludhiana, Punjab", temp: 36, humidity: 48, moisture: "Low (28%)", rainfall: 15, uv: 9,
    alert: "Extreme Heat Warning. Implement light evening irrigation to reduce heat stress on young paddy seedlings.",
    forecast: [
      { day: "Wed", temp: 37, rain: "5%", action: "Drip Irrigation" },
      { day: "Thu", temp: 38, rain: "5%", action: "Soil Mulching" },
      { day: "Fri", temp: 36, rain: "15%", action: "Check soil pH" },
      { day: "Sat", temp: 35, rain: "30%", action: "Shade nursery" },
      { day: "Sun", temp: 34, rain: "40%", action: "Light watering" }
    ]
  },
  "coimbatore": {
    city: "Coimbatore, Tamil Nadu", temp: 30, humidity: 74, moisture: "High (68%)", rainfall: 130, uv: 5,
    alert: "Heavy showers predicted. Clean drainage paths to avoid root drowning in cotton fields.",
    forecast: [
      { day: "Wed", temp: 29, rain: "75%", action: "Clear drains" },
      { day: "Thu", temp: 27, rain: "90%", action: "Indoor composting" },
      { day: "Fri", temp: 28, rain: "60%", action: "Monitor pests" },
      { day: "Sat", temp: 30, rain: "25%", action: "Transplanting" },
      { day: "Sun", temp: 31, rain: "10%", action: "NPK top-dressing" }
    ]
  },
  "guwahati": {
    city: "Guwahati, Assam", temp: 25, humidity: 88, moisture: "V. High (84%)", rainfall: 250, uv: 3,
    alert: "Severe Waterlogging Alert. Suspend nitrogen fertilization; check tea-garden ditches for drainage blockages.",
    forecast: [
      { day: "Wed", temp: 24, rain: "95%", action: "Flood check" },
      { day: "Thu", temp: 24, rain: "95%", action: "Drain trenches" },
      { day: "Fri", temp: 25, rain: "80%", action: "Inspect leaves" },
      { day: "Sat", temp: 26, rain: "60%", action: "Prune tea shrubs" },
      { day: "Sun", temp: 27, rain: "30%", action: "Harvest organic tea" }
    ]
  }
};

// Initial setup on load
document.addEventListener("DOMContentLoaded", () => {
  initRouting();
  initRangeSliders();
  initCropRecommendationForm();
  initWeatherSearch();
  initDashboard();
  initDashboardSubNav();
  initContactForm();
  setupInitialMessages();
});

// 1. Simple Single Page Application Routing
function initRouting() {
  const navLinks = document.querySelectorAll(".navbar-custom .nav-link, .hero-cta");
  const sections = document.querySelectorAll(".app-section");

  function navigateTo(targetId) {
    if (!targetId) return;

    // Normalize targetId
    const cleanId = targetId.replace("#", "");
    
    // Hide all sections with fade-out effect
    sections.forEach(sec => {
      sec.classList.remove("active");
    });

    // Update active state in navbars
    document.querySelectorAll(".navbar-custom .nav-link").forEach(link => {
      const href = link.getAttribute("href");
      if (href === `#${cleanId}`) {
        link.classList.add("active-nav");
      } else {
        link.classList.remove("active-nav");
      }
    });

    // Show target section with a slight delay for transition
    const targetSection = document.getElementById(cleanId);
    if (targetSection) {
      targetSection.classList.add("active");
      window.scrollTo(0, 0);
    }
  }

  // Handle nav link clicks
  navLinks.forEach(link => {
    link.addEventListener("click", (e) => {
      const href = link.getAttribute("href");
      if (href && href.startsWith("#")) {
        e.preventDefault();
        navigateTo(href);
        window.location.hash = href;
      }
    });
  });

  // Handle direct hash navigation on page load
  if (window.location.hash) {
    navigateTo(window.location.hash);
  } else {
    // Default to home
    navigateTo("home");
  }

  // Handle history back/forward buttons
  window.addEventListener("hashchange", () => {
    navigateTo(window.location.hash || "home");
  });
}

// 2. Interactive Range Sliders Display
function initRangeSliders() {
  const sliders = [
    { id: "input-n", displayId: "val-n" },
    { id: "input-p", displayId: "val-p" },
    { id: "input-k", displayId: "val-k" },
    { id: "input-temp", displayId: "val-temp" },
    { id: "input-humidity", displayId: "val-humidity" },
    { id: "input-ph", displayId: "val-ph" },
    { id: "input-rainfall", displayId: "val-rainfall" }
  ];

  sliders.forEach(slider => {
    const sliderEl = document.getElementById(slider.id);
    const displayEl = document.getElementById(slider.displayId);
    
    if (sliderEl && displayEl) {
      // Set initial value
      displayEl.textContent = sliderEl.value;
      
      // Listen to input events
      sliderEl.addEventListener("input", (e) => {
        displayEl.textContent = e.target.value;
      });
    }
  });
}



function initCropRecommendationForm() {
  const form = document.getElementById("crop-recommendation-form");
  const resultCard = document.getElementById("crop-result-card");
  const runLoader = document.getElementById("recommendation-loader");
  const resultPlaceholder = document.getElementById("result-placeholder");

  if (!form) return;

  form.addEventListener("submit", (e) => {
    e.preventDefault();

    // Show loading spinner
    runLoader.classList.remove("d-none");
    resultCard.style.display = "none";
    if (resultPlaceholder) resultPlaceholder.style.display = "none";

    const n = parseFloat(document.getElementById("input-n").value);
    const p = parseFloat(document.getElementById("input-p").value);
    const k = parseFloat(document.getElementById("input-k").value);
    const temp = parseFloat(document.getElementById("input-temp").value);
    const humidity = parseFloat(document.getElementById("input-humidity").value);
    const ph = parseFloat(document.getElementById("input-ph").value);
    const rainfall = parseFloat(document.getElementById("input-rainfall").value);

    // Call REST API predict endpoint
    fetch(`${API_BASE}/predict`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        N: n,
        P: p,
        K: k,
        temperature: temp,
        humidity: humidity,
        ph: ph,
        rainfall: rainfall
      })
    })
    .then(response => {
      if (!response.ok) {
        throw new Error("HTTP prediction failed: status code " + response.status);
      }
      return response.json();
    })
    .then(data => {
      runLoader.classList.add("d-none");
      if (data.status === "success") {
        const cropName = data.crop;
        const confidence = data.confidence;
        const details = data.details;

        // Populating Result UI
        document.getElementById("result-crop-icon").textContent = details.icon || "🌱";
        document.getElementById("result-crop-name").textContent = `${cropName} (Confidence: ${confidence})`;
        document.getElementById("result-crop-scientific").textContent = details.scientific;
        document.getElementById("result-crop-season").textContent = details.season;
        document.getElementById("result-crop-duration").textContent = details.duration;
        const demandEl = document.getElementById("result-crop-demand");
        if (demandEl) demandEl.textContent = details.demand;
        document.getElementById("result-crop-price").textContent = details.price;
        document.getElementById("result-crop-fertilizer").textContent = details.fertilizer;
        document.getElementById("result-crop-tips").textContent = details.tips;

        // Populate explanation and sustainable tips (additional features)
        document.getElementById("result-crop-explanation").textContent = details.explanation;
        
        const sustainableList = document.getElementById("result-crop-sustainable-tips");
        if (sustainableList) {
          sustainableList.innerHTML = "";
          details.sustainable_tips.forEach(tip => {
            const li = document.createElement("li");
            li.className = "mb-1 text-primary-emphasis";
            li.textContent = tip;
            sustainableList.appendChild(li);
          });
        }

        // Visual analysis of deficits compared to baseline cropsDb (fallback to input if crop is not matching)
        const matchingLocalCrop = cropsDb.find(c => c.crop.toLowerCase() === cropName.toLowerCase()) || {
          n: n, p: p, k: k, ph: ph
        };
        const deficitHtml = getSoilDeficitAnalysis(n, p, k, ph, matchingLocalCrop);
        document.getElementById("result-soil-analysis").innerHTML = deficitHtml;

        // Display results page and animate
        resultCard.style.display = "block";
        resultCard.scrollIntoView({ behavior: "smooth", block: "start" });
        
        // Refresh history & dashboard stats if user is logged in
        refreshHistory();
        updateDashboardCounts();
      } else {
        alert("Prediction failed: " + (data.message || "Unknown error"));
        if (resultPlaceholder) resultPlaceholder.style.display = "block";
      }
    })
    .catch(error => {
      runLoader.classList.add("d-none");
      if (resultPlaceholder) resultPlaceholder.style.display = "block";
      console.error("Prediction API connection failed:", error);
      alert("Error connecting to prediction server. Please verify the Flask backend is running on http://127.0.0.1:5000.\nDetails: " + error.message);
    });
  });
}

function getSoilDeficitAnalysis(n, p, k, ph, crop) {
  let html = `<h5 class="mb-3 text-success">Soil Parameters Matching Analysis</h5><ul class="list-group list-group-flush">`;

  // Nitrogen analysis
  const diffN = n - crop.n;
  if (Math.abs(diffN) < 15) {
    html += `<li class="list-group-item d-flex justify-content-between align-items-center">Nitrogen (N) <span>🟢 Optimal (${n} mg/kg)</span></li>`;
  } else if (diffN < 0) {
    html += `<li class="list-group-item d-flex justify-content-between align-items-center text-danger">Nitrogen (N) <span>🔴 Deficit (Needs +${Math.abs(diffN)} mg/kg)</span></li>`;
  } else {
    html += `<li class="list-group-item d-flex justify-content-between align-items-center text-warning">Nitrogen (N) <span>🟡 Surplus (+${Math.abs(diffN)} mg/kg)</span></li>`;
  }

  // Phosphorus
  const diffP = p - crop.p;
  if (Math.abs(diffP) < 10) {
    html += `<li class="list-group-item d-flex justify-content-between align-items-center">Phosphorus (P) <span>🟢 Optimal (${p} mg/kg)</span></li>`;
  } else if (diffP < 0) {
    html += `<li class="list-group-item d-flex justify-content-between align-items-center text-danger">Phosphorus (P) <span>🔴 Deficit (Needs +${Math.abs(diffP)} mg/kg)</span></li>`;
  } else {
    html += `<li class="list-group-item d-flex justify-content-between align-items-center text-warning">Phosphorus (P) <span>🟡 Surplus (+${Math.abs(diffP)} mg/kg)</span></li>`;
  }

  // Potassium
  const diffK = k - crop.k;
  if (Math.abs(diffK) < 10) {
    html += `<li class="list-group-item d-flex justify-content-between align-items-center">Potassium (K) <span>🟢 Optimal (${k} mg/kg)</span></li>`;
  } else if (diffK < 0) {
    html += `<li class="list-group-item d-flex justify-content-between align-items-center text-danger">Potassium (K) <span>🔴 Deficit (Needs +${Math.abs(diffK)} mg/kg)</span></li>`;
  } else {
    html += `<li class="list-group-item d-flex justify-content-between align-items-center text-warning">Potassium (K) <span>🟡 Surplus (+${Math.abs(diffK)} mg/kg)</span></li>`;
  }

  // pH balance
  const diffPH = ph - crop.ph;
  if (Math.abs(diffPH) < 0.4) {
    html += `<li class="list-group-item d-flex justify-content-between align-items-center">pH Level <span>🟢 Well Suited (${ph})</span></li>`;
  } else if (diffPH < 0) {
    html += `<li class="list-group-item d-flex justify-content-between align-items-center text-danger">pH Level <span>🔴 Soil is too Acidic (Needs lime amendment)</span></li>`;
  } else {
    html += `<li class="list-group-item d-flex justify-content-between align-items-center text-danger">pH Level <span>🔴 Soil is too Alkaline (Needs gypsum/sulfur)</span></li>`;
  }

  html += `</ul>`;
  return html;
}

// Log recommendation event to simulation database
function logRecommendation(cropName) {
  // Recommendations are saved automatically in the SQLite DB by app.py
  // Trigger counters and history refreshes
  refreshHistory();
  updateDashboardCounts();
}

// 4. Dynamic Weather Dashboard System
function initWeatherSearch() {
  const searchInput = document.getElementById("weather-search-input");
  const searchBtn = document.getElementById("weather-search-btn");
  const weatherResult = document.getElementById("weather-result-container");
  const weatherLoader = document.getElementById("weather-loader");

  if (!searchBtn) return;

  function handleSearch() {
    const query = searchInput.value.trim().toLowerCase();
    if (!query) return;

    weatherLoader.classList.remove("d-none");
    weatherResult.classList.add("opacity-25");

    setTimeout(() => {
      weatherLoader.classList.add("d-none");
      weatherResult.classList.remove("opacity-25");

      let data = weatherData[query];
      if (!data) {
        // Generate random mock weather for queries outside the standard list
        const randTemp = Math.floor(Math.random() * 15) + 20; // 20 to 35
        const randHumid = Math.floor(Math.random() * 40) + 50; // 50 to 90
        const randRain = Math.floor(Math.random() * 200) + 10;
        data = {
          city: query.charAt(0).toUpperCase() + query.slice(1) + " Region",
          temp: randTemp,
          humidity: randHumid,
          moisture: randHumid > 75 ? "High (70%)" : "Medium (40%)",
          rainfall: randRain,
          uv: Math.floor(Math.random() * 8) + 2,
          alert: randRain > 150 ? "Heavy rain warnings. Clear farm drain blockages." : "No severe weather warnings. Ideal for weeding and sowing.",
          forecast: [
            { day: "Wed", temp: randTemp + 1, rain: randRain > 50 ? "60%" : "15%", action: "Fertilizing" },
            { day: "Thu", temp: randTemp - 1, rain: randRain > 50 ? "70%" : "10%", action: "Harvest check" },
            { day: "Fri", temp: randTemp, rain: randRain > 50 ? "40%" : "20%", action: "Sowing prep" },
            { day: "Sat", temp: randTemp + 2, rain: randRain > 50 ? "20%" : "5%", action: "Soil aerating" },
            { day: "Sun", temp: randTemp + 1, rain: randRain > 50 ? "10%" : "5%", action: "Drip checking" }
          ]
        };
      }

      // Populate Weather UI
      document.getElementById("w-city").textContent = data.city;
      document.getElementById("w-temp").innerHTML = `${data.temp}<span>°C</span>`;
      document.getElementById("w-humidity").textContent = `${data.humidity}%`;
      document.getElementById("w-moisture").textContent = data.moisture;
      document.getElementById("w-rainfall").textContent = `${data.rainfall} mm`;
      document.getElementById("w-uv").textContent = data.uv;
      
      const alertEl = document.getElementById("w-alert");
      alertEl.textContent = data.alert;
      if (data.alert.includes("Warning") || data.alert.includes("Alert") || data.alert.includes("Heavy")) {
        alertEl.parentElement.className = "weather-alert-box bg-danger-subtle border-danger text-danger-emphasis";
      } else {
        alertEl.parentElement.className = "weather-alert-box bg-warning-subtle border-warning text-warning-emphasis";
      }

      // Populate 5-day forecast
      const forecastContainer = document.getElementById("w-forecast-grid");
      forecastContainer.innerHTML = "";
      
      data.forecast.forEach(item => {
        const cardHtml = `
          <div class="col">
            <div class="weather-forecast-card">
              <div class="fw-bold mb-2">${item.day}</div>
              <div class="text-secondary fs-3 mb-2">
                ${item.rain.replace("%","") > 50 ? "🌧️" : "☀️"}
              </div>
              <div class="fw-bold fs-5 mb-1">${item.temp}°C</div>
              <div class="text-muted small mb-2">☔ ${item.rain}</div>
              <span class="badge bg-success-subtle text-success rounded-pill px-2 py-1 small">${item.action}</span>
            </div>
          </div>
        `;
        forecastContainer.innerHTML += cardHtml;
      });

    }, 800);
  }

  searchBtn.addEventListener("click", handleSearch);
  searchInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") handleSearch();
  });
}

// 5. Farmer and Admin Dashboard Controller
let myChart = null; // Global Chart instance

function initDashboard() {
  const loginForm = document.getElementById("dashboard-login-form");
  const loginSection = document.getElementById("dashboard-login-wrapper");
  const mainDash = document.getElementById("dashboard-main-wrapper");
  
  const sidebarFarmer = document.getElementById("sidebar-farmer-nav");
  const sidebarAdmin = document.getElementById("sidebar-admin-nav");
  
  const viewFarmer = document.getElementById("farmer-dashboard-view");
  const viewAdmin = document.getElementById("admin-dashboard-view");
  
  const logoutBtn = document.getElementById("dashboard-logout-btn");
  const roleTitle = document.getElementById("dash-role-title");

  if (!loginForm) return;

  // Handle Login submission
  loginForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const username = document.getElementById("login-username").value.trim().toLowerCase();
    const password = document.getElementById("login-password").value.trim();

    if (username === "farmer" && password === "farmer123") {
      performLogin("farmer");
    } else if (username === "admin" && password === "admin123") {
      performLogin("admin");
    } else {
      alert("Invalid Credentials! Try 'farmer'/'farmer123' or 'admin'/'admin123'.");
    }
  });

  // Handle Logout
  logoutBtn.addEventListener("click", (e) => {
    e.preventDefault();
    localStorage.removeItem("logged_in_role");
    loginSection.classList.remove("d-none");
    mainDash.classList.add("d-none");
  });

  // Execute actual dashboard loading
  function performLogin(role) {
    localStorage.setItem("logged_in_role", role);
    loginSection.classList.add("d-none");
    mainDash.classList.remove("d-none");
    
    // Reset login form fields
    loginForm.reset();

    if (role === "farmer") {
      roleTitle.textContent = "Farmer Portal";
      sidebarFarmer.classList.remove("d-none");
      sidebarAdmin.classList.add("d-none");
      viewFarmer.classList.remove("d-none");
      viewAdmin.classList.add("d-none");

      // Reset Farmer Sub-view active state
      sidebarFarmer.querySelectorAll(".dashboard-nav-link").forEach(l => l.classList.remove("active-dash"));
      const defaultFarmerTab = sidebarFarmer.querySelector('a[href="#farmer-fields-view"]');
      if (defaultFarmerTab) defaultFarmerTab.classList.add("active-dash");
      
      const fieldsCard = document.getElementById("farmer-fields-card");
      const historyCard = document.getElementById("farmer-history-card");
      const chartCard = document.getElementById("farmer-chart-card");
      if (fieldsCard) fieldsCard.classList.remove("d-none");
      if (historyCard) historyCard.classList.remove("d-none");
      if (chartCard) chartCard.classList.add("d-none");
      
      initFarmerChart();
      initFarmerFieldControls();
      refreshHistory();
    } else if (role === "admin") {
      roleTitle.textContent = "Administrator Hub";
      sidebarFarmer.classList.add("d-none");
      sidebarAdmin.classList.remove("d-none");
      viewFarmer.classList.add("d-none");
      viewAdmin.classList.remove("d-none");

      // Reset Admin Sub-view active state
      sidebarAdmin.querySelectorAll(".dashboard-nav-link").forEach(l => l.classList.remove("active-dash"));
      const defaultAdminTab = sidebarAdmin.querySelector('a[href="#admin-overview-view"]');
      if (defaultAdminTab) defaultAdminTab.classList.add("active-dash");

      const overviewRow = document.getElementById("admin-overview-row");
      const messagesCard = document.getElementById("admin-messages-card");
      if (overviewRow) overviewRow.classList.remove("d-none");
      if (messagesCard) messagesCard.classList.add("d-none");
      
      initAdminAnalytics();
      initMessageLogs();
    }
    
    updateDashboardCounts();
  }

  // Persisted Session Check
  const currentRole = localStorage.getItem("logged_in_role");
  if (currentRole) {
    performLogin(currentRole);
  }
}

// Dynamically refresh counts in headers
function updateDashboardCounts() {
  const currentRole = localStorage.getItem("logged_in_role");
  
  if (currentRole === "admin") {
    fetch(`${API_BASE}/analytics`)
      .then(r => r.json())
      .then(data => {
        if (data.status === "success") {
          const totalRecEl = document.getElementById("admin-total-recs");
          if (totalRecEl) {
            totalRecEl.textContent = data.analytics.total_recommendations.toLocaleString();
          }
        }
      })
      .catch(err => {
        console.error("Error updating admin analytics counter:", err);
        let recTotal = parseInt(localStorage.getItem("total_recommendations")) || 12840;
        const totalRecEl = document.getElementById("admin-total-recs");
        if (totalRecEl) totalRecEl.textContent = recTotal.toLocaleString();
      });
  }
}

// Farmer Chart Loader (Chart.js)
function initFarmerChart() {
  const ctx = document.getElementById("soilTrendChart");
  if (!ctx) return;

  // Clean old chart if it exists to prevent memory leaks/overlapping
  if (myChart) {
    myChart.destroy();
  }

  // Soil health quarterly trend parameters
  myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['Q3-2025', 'Q4-2025', 'Q1-2026', 'Q2-2026'],
      datasets: [
        {
          label: 'Nitrogen (N) mg/kg',
          data: [65, 78, 80, 92],
          borderColor: '#2e7d32',
          backgroundColor: 'rgba(46, 125, 50, 0.1)',
          tension: 0.3,
          borderWidth: 2,
          fill: true
        },
        {
          label: 'Phosphorus (P) mg/kg',
          data: [38, 40, 42, 41],
          borderColor: '#1565c0',
          backgroundColor: 'rgba(21, 101, 192, 0.05)',
          tension: 0.3,
          borderWidth: 2,
          fill: false
        },
        {
          label: 'Potassium (K) mg/kg',
          data: [25, 20, 22, 24],
          borderColor: '#ff8f00',
          backgroundColor: 'rgba(255, 143, 0, 0.05)',
          tension: 0.3,
          borderWidth: 2,
          fill: false
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          position: 'top',
          labels: {
            font: { family: 'Plus Jakarta Sans' }
          }
        }
      },
      scales: {
        y: {
          beginAtZero: true,
          grid: { color: 'rgba(0,0,0,0.05)' }
        },
        x: {
          grid: { display: false }
        }
      }
    }
  });
}

// Farmer Add Field controls
function initFarmerFieldControls() {
  const fieldListContainer = document.getElementById("farmer-fields-list");
  const fieldForm = document.getElementById("add-field-form");

  if (!fieldListContainer || !fieldForm) return;

  // Load from local storage
  let fields = JSON.parse(localStorage.getItem("farmer_fields")) || [
    { name: "North Field", area: "1.8 Hectares", crop: "Rice", health: "Healthy" },
    { name: "Riverside Patch", area: "2.7 Hectares", crop: "Cotton", health: "Needs Irrigation" }
  ];

  function renderFields() {
    fieldListContainer.innerHTML = "";
    fields.forEach((field, index) => {
      const isWarning = field.health.includes("Needs") || field.health.includes("Deficit");
      const healthBadge = isWarning 
        ? `<span class="badge bg-warning text-dark">${field.health}</span>` 
        : `<span class="badge bg-success">${field.health}</span>`;
      
      const fieldHtml = `
        <div class="col-md-6 mb-3">
          <div class="card bg-light border-0 shadow-sm rounded-3">
            <div class="card-body">
              <div class="d-flex justify-content-between align-items-center mb-2">
                <h6 class="mb-0 fw-bold">${field.name}</h6>
                <button class="btn btn-sm btn-outline-danger border-0 py-0 px-1 delete-field-btn" data-index="${index}">🗑️</button>
              </div>
              <p class="mb-1 text-muted small">📏 Size: ${field.area}</p>
              <p class="mb-1 text-muted small">🌱 Crop: ${field.crop}</p>
              <div class="d-flex justify-content-between align-items-center mt-3">
                <span class="small text-secondary">Status:</span>
                ${healthBadge}
              </div>
            </div>
          </div>
        </div>
      `;
      fieldListContainer.innerHTML += fieldHtml;
    });

    // Wire deletes
    document.querySelectorAll(".delete-field-btn").forEach(btn => {
      btn.addEventListener("click", (e) => {
        const idx = btn.getAttribute("data-index");
        fields.splice(idx, 1);
        localStorage.setItem("farmer_fields", JSON.stringify(fields));
        renderFields();
      });
    });
  }

  // Hook submit
  fieldForm.onsubmit = (e) => {
    e.preventDefault();
    const name = document.getElementById("field-name").value;
    const area = document.getElementById("field-area").value + " Hectares";
    const crop = document.getElementById("field-crop").value;
    const health = "Healthy";

    fields.push({ name, area, crop, health });
    localStorage.setItem("farmer_fields", JSON.stringify(fields));
    renderFields();
    
    // Close modal or reset
    fieldForm.reset();
    const modalEl = document.getElementById("addFieldModal");
    const modal = bootstrap.Modal.getInstance(modalEl);
    if (modal) modal.hide();
  };

  renderFields();
}

// Admin Dashboard Analytics
function initAdminAnalytics() {
  const ctx = document.getElementById("adminUsageChart");
  if (!ctx) return;

  fetch(`${API_BASE}/analytics`)
    .then(r => r.json())
    .then(data => {
      if (data.status === "success") {
        const counts = data.analytics.crop_counts;
        // Render crop distribution chart
        new Chart(ctx, {
          type: 'doughnut',
          data: {
            labels: Object.keys(counts),
            datasets: [{
              data: Object.values(counts),
              backgroundColor: [
                '#1b5e20', // Rice
                '#ffd54f', // Maize
                '#ff8f00', // Chickpea
                '#81c784', // Cotton
                '#b0bec5'  // Others
              ],
              borderWidth: 1
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: {
                position: 'right',
                labels: { font: { family: 'Plus Jakarta Sans' } }
              }
            }
          }
        });
      }
    })
    .catch(err => {
      console.error("Error loading admin usage chart:", err);
    });
}

// Admin message Log viewer
function initMessageLogs() {
  const tableBody = document.getElementById("admin-messages-table");
  if (!tableBody) return;

  function renderMessages() {
    fetch(`${API_BASE}/messages`)
      .then(r => r.json())
      .then(data => {
        if (data.status === "success") {
          const msgs = data.messages;
          tableBody.innerHTML = "";

          if (msgs.length === 0) {
            tableBody.innerHTML = `<tr><td colspan="4" class="text-center text-muted">No messages received yet.</td></tr>`;
            return;
          }

          msgs.forEach((m) => {
            const tr = document.createElement("tr");
            tr.innerHTML = `
              <td class="small fw-semibold text-primary">${m.date || "Just now"}</td>
              <td>
                <div class="fw-bold">${m.name}</div>
                <div class="text-muted small">${m.email}</div>
              </td>
              <td><span class="badge bg-secondary-subtle text-secondary">${m.subject}</span></td>
              <td class="small">${m.message}</td>
            `;
            tableBody.appendChild(tr);
          });
        }
      })
      .catch(err => {
        console.error("Error fetching message logs:", err);
        tableBody.innerHTML = `<tr><td colspan="4" class="text-center text-danger">Failed to fetch message logs from server.</td></tr>`;
      });
  }

  renderMessages();
}

// 6. Contact Form submission logic
function initContactForm() {
  const form = document.getElementById("contact-submission-form");
  if (!form) return;

  form.addEventListener("submit", (e) => {
    e.preventDefault();

    const name = document.getElementById("contact-name").value;
    const email = document.getElementById("contact-email").value;
    const subject = document.getElementById("contact-subject").value;
    const message = document.getElementById("contact-message").value;

    fetch(`${API_BASE}/contact`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        name,
        email,
        subject,
        message
      })
    })
    .then(r => r.json())
    .then(data => {
      if (data.status === "success") {
        alert(`Thank you, ${name}! Your message has been successfully routed to our support team. We will get back to you shortly.`);
        form.reset();
      } else {
        alert("Failed to submit inquiry: " + (data.message || "Unknown error"));
      }
    })
    .catch(err => {
      console.error("Error sending contact message:", err);
      alert("Failed to submit inquiry. Please verify the Flask backend is running on http://127.0.0.1:5000.");
    });
  });
}

// Setup initial static messages so the admin panel looks populated on first view
function setupInitialMessages() {
  // Messages are now handled by SQLite DB seeds on backend.
}

// Helper to pull soil prediction history for farmer view
function refreshHistory() {
  const tableBody = document.getElementById("farmer-history-table");
  if (!tableBody) return;

  fetch(`${API_BASE}/history`)
    .then(r => r.json())
    .then(data => {
      if (data.status === "success") {
        const history = data.history;
        tableBody.innerHTML = "";

        if (history.length === 0) {
          tableBody.innerHTML = `<tr><td colspan="4" class="text-center text-muted">No predictions logged yet. Run the recommendation engine!</td></tr>`;
          return;
        }

        history.forEach(item => {
          const tr = document.createElement("tr");
          tr.innerHTML = `
            <td class="text-secondary fw-semibold">${item.timestamp}</td>
            <td>
              <div class="fw-bold text-success">N: ${item.n} | P: ${item.p} | K: ${item.k}</div>
            </td>
            <td>
              <div class="small text-muted">T: ${item.temperature}°C, H: ${item.humidity}%, pH: ${item.ph}, R: ${item.rainfall}mm</div>
            </td>
            <td>
              <span class="badge bg-success-subtle text-success border border-success-subtle px-2 py-1 rounded-pill">
                ${item.crop} (${item.confidence})
              </span>
            </td>
          `;
          tableBody.appendChild(tr);
        });
      }
    })
    .catch(err => {
      console.error("Error fetching predictions history:", err);
      tableBody.innerHTML = `<tr><td colspan="4" class="text-center text-danger">Failed to fetch prediction history from server.</td></tr>`;
    });
}

// Helper to handle sub-navigation within farmer/admin dashboards
function initDashboardSubNav() {
  const navLinks = document.querySelectorAll(".dashboard-nav-link");
  navLinks.forEach(link => {
    if (link.id === "dashboard-logout-btn") return;

    link.addEventListener("click", (e) => {
      const href = link.getAttribute("href");
      if (!href || href === "#") return;
      e.preventDefault();

      // Find active division links and update active class
      const parent = link.parentElement;
      parent.querySelectorAll(".dashboard-nav-link").forEach(l => {
        l.classList.remove("active-dash");
      });
      link.classList.add("active-dash");

      // Hide or show target components
      if (href === "#farmer-fields-view") {
        document.getElementById("farmer-fields-card").classList.remove("d-none");
        document.getElementById("farmer-history-card").classList.remove("d-none");
        document.getElementById("farmer-chart-card").classList.add("d-none");
      } else if (href === "#farmer-soil-view") {
        document.getElementById("farmer-fields-card").classList.add("d-none");
        document.getElementById("farmer-history-card").classList.add("d-none");
        document.getElementById("farmer-chart-card").classList.remove("d-none");
      } else if (href === "#admin-overview-view") {
        document.getElementById("admin-overview-row").classList.remove("d-none");
        document.getElementById("admin-messages-card").classList.add("d-none");
      } else if (href === "#admin-messages-view") {
        document.getElementById("admin-overview-row").classList.add("d-none");
        document.getElementById("admin-messages-card").classList.remove("d-none");
      }
    });
  });
}
