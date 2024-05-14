# Analise dos dados - Questão 1 # Gráfico de Dispersão
 <div class="card" style="font-size: 16px">${
    resize((width) => Plot.plot({
  width: 1500,
  height: 600,
  marginLeft: 100,
  label: null,
  color: { scheme: "rdylbu", pivot: 0, legend: true, label: "correlation" },
  marks: [
    Plot.cell(correlations, { x: "a", y: "b", fill: "correlation" }),
    Plot.text(correlations, {
      x: "a",
      y: "b",
      text: (d) => d.correlation.toFixed(2),
      fill: (d) => (Math.abs(d.correlation) > 0.6 ? "white" : "black")
    })
  ]
}))
  }</div>
 
 <div class="card">${ resize((width) => Plot.plot({
  inset: 8,
  grid: true,
  color: {
    legend: true,
  },
  marks: [
    Plot.dot(spotify, {x: "streams", y: "in_spotify_playlists", stroke: "streams"})
  ]
}) ) }</div> 
 <div class="card">${ resize((width) => Plot.plot({
  inset: 8,
  grid: true,
  color: {
    legend: true,
  },
  marks: [
    Plot.dot(spotify, {x: "streams", y: "in_apple_playlists", stroke: "streams"})
  ]
}) ) }</div> 
 <div class="card">${ resize((width) => Plot.plot({
  inset: 8,
  grid: true,
  color: {
    legend: true,
  },
  marks: [
    Plot.dot(spotify, {x: "streams", y: "in_deezer_playlists", stroke: "streams"})
  ]
}) ) }</div> 
 
 ```js 
 const correlations = FileAttachment("output.json").json({typed:true}); 
 const spotify = FileAttachment("/data/spotify-2023.csv").csv({typed:true});
 ```