const urlInput = document.getElementById("urlInput");
const checkButton = document.getElementById("checkButton");
const result = document.getElementById("result");
const loading = document.getElementById("loading");
const historyList = document.getElementById("historyList");
const clearHistory = document.getElementById("clearHistory");


// Load history when the page opens
function loadHistory() {

    const history = JSON.parse(
        localStorage.getItem("urlHistory") || "[]"
    );

    if (history.length === 0) {
        historyList.innerHTML = "<p>No predictions yet.</p>";
        return;
    }

    historyList.innerHTML = "";

    history.forEach(item => {

        const historyItem = document.createElement("div");

        historyItem.className = "history-item";

        historyItem.innerHTML = `
            <strong>${item.prediction}</strong>
            <br>
            <span>${item.url}</span>
            <br>
            <small>
                Confidence: ${item.confidence}%
                | Risk: ${item.risk}
            </small>
        `;

        historyList.appendChild(historyItem);
    });
}


// Check URL
checkButton.addEventListener("click", async () => {

    const url = urlInput.value.trim();

    if (!url) {
        result.textContent = "⚠️ Please enter a URL.";
        return;
    }

    loading.style.display = "block";
    result.textContent = "";

    try {

        const response = await fetch(
            "http://127.0.0.1:5000/predict",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    url: url
                })
            }
        );

        const data = await response.json();

        loading.style.display = "none";

        let riskLevel;

        if (data.prediction === "PHISHING") {

            riskLevel =
                data.confidence >= 75 ? "HIGH" : "MEDIUM";

            result.innerHTML = `
                🔴 PHISHING URL
                <br>
                <span>Confidence: ${data.confidence}%</span>
                <br>
                <span>Risk Level: ${riskLevel}</span>
            `;

        } else {

            riskLevel =
                data.confidence >= 75 ? "LOW" : "MEDIUM";

            result.innerHTML = `
                🟢 LEGITIMATE URL
                <br>
                <span>Confidence: ${data.confidence}%</span>
                <br>
                <span>Risk Level: ${riskLevel}</span>
            `;
        }


        // Save prediction to browser history
        const history = JSON.parse(
            localStorage.getItem("urlHistory") || "[]"
        );

        history.unshift({
            url: url,
            prediction: data.prediction,
            confidence: data.confidence,
            risk: riskLevel
        });

        // Keep only the latest 10 predictions
        history.splice(10);

        localStorage.setItem(
            "urlHistory",
            JSON.stringify(history)
        );

        // Display updated history
        loadHistory();

    } catch (error) {

        loading.style.display = "none";

        result.textContent =
            "❌ Could not connect to the server.";

        console.error(error);
    }
});


// Clear history
clearHistory.addEventListener("click", () => {

    localStorage.removeItem("urlHistory");

    loadHistory();
});


// Load saved history
loadHistory();