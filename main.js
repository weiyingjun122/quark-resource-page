const params = new URLSearchParams(location.search);
const id = params.get("id");

fetch("data.json")
  .then(res => res.json())
  .then(data => {
    const item = data[id];
    if (!item) {
      document.body.innerHTML = "资源不存在";
      return;
    }
    document.getElementById("title").innerText = item.title;
    document.getElementById("code").innerText = item.code;
  });

function copyCode() {
  const text = document.getElementById("code").innerText;
  navigator.clipboard.writeText(text).then(() => {
    alert("口令已复制，请打开夸克 App 粘贴转存");
  });
}
