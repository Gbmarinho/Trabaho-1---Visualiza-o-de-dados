# Analise dos dados - Questão 2 # Gráfico de Barra
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
                        fill: "artist(s)_name"
                    }), 
                    Plot.text(topArtists, {
                        y: "streams",
                        x: "artist(s)_name",
                    })  
                ],
            color: {
                type: "categorical",
                scheme: "category10",} 
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
                        fill: "artist(s)_name"
                    }), 
                    Plot.text(topArtists2023, {
                        y: "streams",
                        x: "artist(s)_name",
                    })  
                ],
            color: {
                type: "categorical",
                scheme: "category10",} 
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
                        fill: "artist(s)_name"
                    }), 
                    Plot.text(topStreams, {
                        y: "streams",
                        x: "track_name",
                    })  
                ],
            color: {
                type: "categorical",
                scheme: "category10",} 
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
                        fill: "artist(s)_name"
                    }), 
                    Plot.text(topStreams2023, {
                        y: "streams",
                        x: "track_name",
                    })  
                ],
            color: {
                type: "categorical",
                scheme: "category10",} 
    })) }</div> 

 



 ```js 
 const topArtists = FileAttachment("/data/top_10_artists.csv").csv({typed:true}); 
 const topStreams = FileAttachment("/data/top_10_streams.csv").csv({typed:true}); 
 const topArtists2023 = FileAttachment("/data/top_10_artists_2023.csv").csv({typed:true}); 
 const topStreams2023 = FileAttachment("/data/top_10_streams_2023.csv").csv({typed:true}); 
 ```
 