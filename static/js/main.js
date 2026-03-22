function testURL(url) {
    document.getElementById("urlInput").value = url;
    checkURL();
}

async function checkURL() {
    const url = document.getElementById("urlInput").value.trim();
    if (!url) {
        alert("Please enter a URL!");
        return;
    }

    document.getElementById("loading").style.display = "block";
    document.getElementById("result").style.display  = "none";

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ url })
        });

        const data = await response.json();
        if (data.error) { alert(data.error); return; }

        const isPhish = data.prediction === "Phishing";

        const header = document.getElementById("result-header");
        header.className = "result-header " +
            (isPhish ? "result-phish" : "result-safe");
        document.getElementById("result-text").textContent =
            isPhish ? "PHISHING DETECTED" : "SAFE URL";

        document.getElementById("confidence-text").textContent =
            data.confidence + "%";
        const fill = document.getElementById("confidence-fill");
        fill.style.width = data.confidence + "%";
        fill.className   = "confidence-fill " +
            (isPhish ? "fill-phish" : "fill-safe");

        document.getElementById("legit-prob").textContent =
            data.legit_prob + "%";
        document.getElementById("phish-prob").textContent =
            data.phishing_prob + "%";

        const feats    = data.features;
        const featHTML = Object.entries(feats).map(([k, v]) => {
            let val;
            if (typeof v === "boolean") {
                val = v
                    ? "<span class='feat-yes'>Yes</span>"
                    : "<span class='feat-no'>No</span>";
            } else {
                val = v;
            }
            return `<div class="feature-item">
                        <span>${k}</span>
                        <span>${val}</span>
                    </div>`;
        }).join("");
        document.getElementById("features-list").innerHTML = featHTML;

        document.getElementById("url-text").textContent = data.url;

        document.getElementById("loading").style.display = "none";
        document.getElementById("result").style.display  = "block";

    } catch(e) {
        alert("Error connecting to server. Make sure Flask is running!");
        document.getElementById("loading").style.display = "none";
    }
}