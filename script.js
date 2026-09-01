const btn = document.getElementById("generateBtn");
const loading = document.getElementById("loading");
const result = document.getElementById("result");
const image = document.getElementById("generatedImage");
const downloadBtn = document.getElementById("downloadBtn");

btn.addEventListener("click", async () => {

    const prompt = document.getElementById("prompt").value.trim();

    if (!prompt) {
        alert("Enter prompt!");
        return;
    }

    loading.classList.remove("hidden");
    result.classList.add("hidden");

    const res = await fetch("/generate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ prompt })
    });

    const data = await res.json();

    loading.classList.add("hidden");

    if (data.image) {
        image.src = data.image;
        downloadBtn.href = data.image;
        result.classList.remove("hidden");
    } else {
        alert("Error generating image");
    }
});