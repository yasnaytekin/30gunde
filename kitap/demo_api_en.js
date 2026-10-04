// 30 Days of JavaScript: the demo API (/demo-api/...).
// When you try the code on your own computer, paste this at the VERY TOP of your script:
// fetch("/demo-api/...") requests are answered with the data below, without going to the internet.
const DEMO_API = {
  cities: [
    { name: "London", region: "Europe", population: 8982000, temp: 11 },
    { name: "Paris", region: "Europe", population: 2161000, temp: 13 },
    { name: "Tokyo", region: "Asia", population: 13960000, temp: 16 },
    { name: "Cairo", region: "Africa", population: 9540000, temp: 27 },
    { name: "Sydney", region: "Oceania", population: 5312000, temp: 22 },
    { name: "New York", region: "North America", population: 8336000, temp: 14 },
    { name: "Rio de Janeiro", region: "South America", population: 6748000, temp: 25 },
    { name: "Mumbai", region: "Asia", population: 12440000, temp: 29 },
  ],
  questions: [
    { question: "Which planet is closest to the Sun?", options: ["Venus", "Mercury", "Mars"], answer: 1 },
    { question: "Which one is known as the red planet?", options: ["Mars", "Jupiter", "Neptune"], answer: 0 },
    { question: "Which planet is famous for its rings?", options: ["Uranus", "Saturn", "Earth"], answer: 1 },
    { question: "Which word declares a constant in JavaScript?", options: ["let", "var", "const"], answer: 2 },
    { question: "Is the Moon Earth's satellite?", options: ["Yes", "No"], answer: 0 },
  ],
  levels: {
    1: { level: 1, stars: 5, enemies: 1, speed: 2 },
    2: { level: 2, stars: 8, enemies: 3, speed: 3 },
    3: { level: 3, stars: 12, enemies: 5, speed: 4 },
  },
  tasks: [
    { id: 1, title: "Paint the rocket", done: true },
    { id: 2, title: "Get fuel", done: false },
    { id: 3, title: "Draw the map", done: true },
    { id: 4, title: "Pick the launch time", done: false },
  ],
  posts: [
    { id: 1, title: "My first code", summary: "I wrote my first message with console.log." },
    { id: 2, title: "I brought the page to life", summary: "With buttons, events and the DOM, the page reacts now." },
    { id: 3, title: "My game is ready", summary: "I finished Star Hunter with canvas and a game loop." },
  ],
};

const realFetch = window.fetch.bind(window);
window.fetch = async (address, ...rest) => {
  const url = new URL(String(address), location.href);
  if (!url.pathname.startsWith("/demo-api/")) return realFetch(address, ...rest);
  await new Promise((r) => setTimeout(r, 120)); // wait a little, like a real server
  const reply = (data, status = 200) =>
    new Response(JSON.stringify(data), { status, headers: { "Content-Type": "application/json" } });
  const [, , name, id] = url.pathname.split("/");
  if (name === "cities") {
    const region = url.searchParams.get("region") || "";
    return reply(DEMO_API.cities.filter((c) => c.region.includes(region)));
  }
  if (name === "levels") return DEMO_API.levels[id] ? reply(DEMO_API.levels[id]) : reply({ error: "no such level" }, 404);
  if (name === "error") return reply({ error: "server error" }, 500);
  if (name in DEMO_API && !id) return reply(DEMO_API[name]);
  return reply({ error: "not found" }, 404);
};
