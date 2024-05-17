# Analise dos dados - Questão 3 - Gráfico de

<div class="card">${ 
    resize((width) => Plot.plot( {
        title: "Charts Spotify",
        marginLeft: 240,
        x: { axis: null},
        y: { label: null },
            marks: [
                    Plot.barX(topSpotify, {
                        grid: true,
                        x: "in_spotify_charts",
                        y: "track_name",
                        sort: { y: "x", reverse: true, limit: 10},
                        tip: true,
                        fill: "in_spotify_charts"
                    }), 
                    Plot.text(topSpotify, {
                        y: "in_spotify_charts",
                        x: "track_name",
                    })  
                ],
            color: {
                type: "categorical",
                scheme: "BuGn",} 
    })) }</div> 

<div class="card">${ 
    resize((width) => Plot.plot( {
        title: "Charts Shazam",
        marginLeft: 240,
        x: { axis: null},
        y: { label: null },
            marks: [
                    Plot.barX(topShazam, {
                        grid: true,
                        x: "in_shazam_charts",
                        y: "track_name",
                        sort: { y: "x", reverse: true, limit: 10},
                        tip: true,
                        fill: "in_shazam_charts"
                    }), 
                    Plot.text(topShazam, {
                        y: "in_shazamd_charts",
                        x: "track_name",
                    })  
                ],
            color: {
                type: "categorical",
                scheme: "PuBu",} 
    })) }</div> 

<div class="card">${ 
    resize((width) => Plot.plot( {
        title: "Charts Deezer",
        marginLeft: 240,
        x: { axis: null},
        y: { label: null },
            marks: [
                    Plot.barX(topDeezer, {
                        grid: true,
                        x: "in_deezer_charts",
                        y: "track_name",
                        sort: { y: "x", reverse: true, limit: 10},
                        tip: true,
                        fill: "in_deezer_charts"
                    }), 
                    Plot.text(topDeezer, {
                        y: "in_deezer_charts",
                        x: "track_name",
                    })  
                ],
            color: {
                type: "categorical",
                scheme: "PuRd",} 
    })) }</div>     

<div class="card">${ 
    resize((width) => Plot.plot( {
        title: "Charts Apple",
        marginLeft: 240,
        x: { axis: null},
        y: { label: null },
            marks: [
                    Plot.barX(topApple, {
                        grid: true,
                        x: "in_apple_charts",
                        y: "track_name",
                        sort: { y: "x", reverse: true, limit: 10},
                        tip: true,
                        fill: "in_apple_charts"
                    }), 
                    Plot.text(topDeezer, {
                        y: "in_apple_charts",
                        x: "track_name",
                    })  
                ],
            color: {
                type: "categorical",
                scheme: "RdPu",} 
    })) }</div>     

```js
 const topSpotify = FileAttachment("/data/top_10_spotify_charts_2023.csv").csv({typed:true}); 
 const topShazam = FileAttachment("/data/top_10_shazam_charts_2023.csv").csv({typed:true}); 
 const topDeezer = FileAttachment("/data/top_10_deezer_charts_2023.csv").csv({typed:true}); 
 const topApple = FileAttachment("/data/top_10_apple_charts_2023.csv").csv({typed:true}); 

```


---