# Analise dos dados - Questão 2 - Gráfico de Barra

---
### 2- O conjunto das top 10 músicas e dos top 10 artistas varia muito se considerarmos apenas musicas lançadas no mesmo ano?

---

Para esta análise, escolhemos o uso de gráficos de barra.

Os gráficos mostram o top 10 de músicas e artistas mais ouvidos no ano de 2023, e mais ouvidos com lançamentos de 2023, respectivamente.

Assim, podemos perceber que existe uma variação considerável em ambos top 10 se considerarmos apenas musicas lançadas no ano 2023.

  <div class="card">${ 
    resize((width) => Plot.plot( {
        title: "Artistas mais ouvidos em 2023",
        marginLeft: 240,
        x: { axis: null},
        y: { label: null },
            marks: [
                    Plot.barX(topArtists, {
                        grid: true,
                        x: "streams",
                        y: "artist(s)_name",
                        sort: { y: "x", reverse: true, limit: 10},
                        tip: true,
                        fill: "streams"
                    }), 
                    Plot.text(topArtists, {
                        y: "streams",
                        x: "artist(s)_name",
                    })  
                ],
            color: {
                type: "Sequential",
                scheme: "Magma",} 
    })) }</div> 
  <div class="card">${ 
    resize((width) => Plot.plot( {
        title: "Artistas mais ouvidos com músicas lançadas em 2023",
        marginLeft: 240,
        x: { axis: null},
        y: { label: null },
            marks: [
                    Plot.barX(topArtists2023, {
                        grid: true,
                        x: "streams",
                        y: "artist(s)_name",
                        sort: { y: "x", reverse: true, limit: 10},
                        tip: true,
                        fill: "streams"
                    }), 
                    Plot.text(topArtists2023, {
                        y: "streams",
                        x: "artist(s)_name",
                    })  
                ],
            color: {
                type: "Sequential",
                scheme: "Magma",}
    })) }</div> 



  <div class="card">${ 
    resize((width) => Plot.plot( {
        title: "Músicas mais ouvidas em 2023",
        marginLeft: 240,
        x: { axis: null},
        y: { label: null },
            marks: [
                    Plot.barX(topStreams, {
                        x: "streams",
                        y: "track_name",
                        sort: { y: "x", reverse: true, limit: 10},
                        tip: true,
                        fill: "streams"
                    }), 
                    Plot.text(topStreams, {
                        y: "streams",
                        x: "track_name",
                    })  
                ],
            color: {
                type: "Sequential",
                scheme: "Plasma",}
    })) }</div> 
  <div class="card">${ 
    resize((width) => Plot.plot( {
        title: "Músicas mais ouvidas lançadas em 2023",
        marginLeft: 240,
        x: { axis: null},
        y: { label: null },
            marks: [
                    Plot.barX(topStreams2023, {
                        x: "streams",
                        y: "track_name",
                        sort: { y: "x", reverse: true, limit: 10},
                        tip: true,
                        fill: "streams"
                    }), 
                    Plot.text(topStreams2023, {
                        y: "streams",
                        x: "track_name",
                    })  
                ],
            color: {
                type: "Sequential",
                scheme: "Plasma",} 
    })) }</div> 

 ```js 
 const topArtists = FileAttachment("/data/top_10_artists.csv").csv({typed:true}); 
 const topStreams = FileAttachment("/data/top_10_streams.csv").csv({typed:true}); 
 const topArtists2023 = FileAttachment("/data/top_10_artists_2023.csv").csv({typed:true}); 
 const topStreams2023 = FileAttachment("/data/top_10_streams_2023.csv").csv({typed:true}); 
 ```
 