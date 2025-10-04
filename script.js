let ws = new WebSocket("ws://localhost:6789");

ws.onopen = () => {
  document.getElementById("status").innerText = "Connected ✅";
};

ws.onclose = () => {
  document.getElementById("status").innerText = "Disconnected ❌";
};

ws.onmessage = (event) => {
  let chat = document.getElementById("chat");
  chat.innerHTML += `<div>${event.data}</div>`;
  chat.scrollTop = chat.scrollHeight;
};

function sendMessage() {
  let input = document.getElementById("input");
  if (input.value.trim() !== "") {
    ws.send(input.value);
    input.value = "";
  }
}
