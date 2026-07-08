(function () {
  function basename(path) {
    var parts = path.split("/");
    return parts[parts.length - 1] || path;
  }

  function formatSampleText(text) {
    try {
      return JSON.stringify(JSON.parse(text), null, 2);
    } catch (e) {
      return text;
    }
  }

  async function loadSampleBlock(block) {
    var pre = block.querySelector("[data-sample]");
    if (!pre) return;

    var path = pre.getAttribute("data-sample");
    var role = pre.getAttribute("data-role") || "";
    var nameEl = block.querySelector(".func-sample-filename");

    try {
      var res = await fetch(path);
      if (!res.ok) throw new Error("HTTP " + res.status);
      var text = await res.text();
      pre.textContent = formatSampleText(text);
      if (nameEl) nameEl.textContent = basename(path);
    } catch (e) {
      if (role === "result") {
        pre.textContent = "결과 샘플이 준비되지 않았습니다.";
      } else {
        pre.textContent = "샘플 JSON을 불러오지 못했습니다: " + path;
      }
      if (nameEl) nameEl.textContent = basename(path);
    }
  }

  async function loadFuncSamples() {
    var blocks = document.querySelectorAll(".func-sample-block");
    await Promise.all(Array.prototype.map.call(blocks, loadSampleBlock));
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", loadFuncSamples);
  } else {
    loadFuncSamples();
  }
})();
