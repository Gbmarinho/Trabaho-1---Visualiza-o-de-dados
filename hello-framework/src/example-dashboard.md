# Analise dos dados - Questão 2 # Gráfico de
 <div class="card">${ resize((width) => Plot.barX(spotify, {marginLeft: 90, x: "streams", y: "artist(s)_name", sort: { y: "x", reverse: true, limit: 10 } }).plot() ) }</div> <div class="card">${ resize((width) => Plot.barX(spotify, {marginLeft: 90, x: "streams", y: "track_name", sort: { y: "x", reverse: true, limit: 10 } }).plot() ) }</div> 
 
 ```js 
 const correlations = FileAttachment("output.json").json({typed:true}); 
 const spotify = FileAttachment("/data/spotify-2023.csv").csv({typed:true}); 

 ```
 