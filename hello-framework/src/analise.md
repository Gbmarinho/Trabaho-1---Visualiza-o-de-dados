# Análise dos dados - Questão 1 - Gráfico de Dispersão
Para esta análise, escolhemos um correlograma e gráficos de dispersão.

O correlograma mostra que existe maior grau de correlação entre streams e presença em playlists. Por isso, fizemos graficos de dispersão e conseguimos observar a seguinte tendência: 

 Quanto maior a presença em playlists, mais streams terá a música.

---
### 1- Existe alguma característica que faz uma música ter mais chance de se tornar popular?
---

 <div class="card" style="font-size: 16px">${
    resize((width) => Plot.plot({
  title: "Correlograma das colunas",   
  width: 1500,
  height: 600,
  marginLeft: 100,
  label: null,
  color: { scheme: "rdylbu", pivot: 0, legend: true, label: "correlation" },
  marks: [
    Plot.cell(correlations, { x: "a", y: "b", fill: "correlation", tip: true}),
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
  title: "Presença em playlists no Spotify",   
  inset: 8,
  grid: true,
  color: {
    legend: true,
  },
  marks: [
    Plot.dot(spotify, {x: "streams", y: "in_spotify_playlists", stroke: "streams", tip: true, channels:{nome: "track_name", artista: "artist(s)_name"}})
  ]
}) ) }</div> 
 <div class="card">${ resize((width) => Plot.plot({
  title: "Presença em playlists na Apple",   
  inset: 8,
  grid: true,
  color: {
    legend: true,
  },
  marks: [
    Plot.dot(spotify, {x: "streams", y: "in_apple_playlists", stroke: "streams", tip: true},)
  ]
}) ) }</div> 
 <div class="card">${ resize((width) => Plot.plot({
  title: "Presença em playlists no Deezer",
  inset: 8,
  grid: true,
  color: {
    legend: true,
  },
  marks: [
    Plot.dot(spotify, {x: "streams", y: "in_deezer_playlists", stroke: "streams", tip: true})
  ]
}) ) }</div> 
 
 ```js 
 const correlations = FileAttachment("output.json").json({typed:true}); 
 const spotify = FileAttachment("/data/spotify-2023.csv").csv({typed:true});
 ```