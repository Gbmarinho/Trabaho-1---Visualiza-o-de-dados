# Analise dos dados - Questão 3 - Gráfico de Barras

---
### 3- Discuta as diferenças entre as plataformas (Spotify, Deezer, Apple Music e Shazam)?

---

Para esta análise, escolhemos o uso de gráficos de barras.

Os gráficos mostram os charts das plataformas: Spotify,
Shazam,
Deezer e
Apple.

Charts são um método de classificar canções de acordo com sua popularidade durante um determinado período de tempo. 

Nota-se que existe diferença clara entre os charts de cada plataforma, cada uma distinta em relação a outra. Logo, percebe-se que existe diversidade de público de acordo com a plataforma, que tem identidade refletida nas preferências dos usuários.

<style>
.button-group{
     display: flex;
    flex-direction: row;  
    gap: 4px     
}
.toggle-button{
     display: flex;
    flex-direction: row;
    justify-content:center;
    align-items:center;
    width: 70px;
    border: 1px solid grey;
    border-radius: 10px;
    padding: 4px 0;
    font-size: 14px;
}
.toggle-button:hover{
     background-color: #b3bbe031;
}
.selected {
    background-image: linear-gradient(147deg, #1E1E1E 0%, #161616 100%);
    color: grey; 
    transform: scale(0.95);
}


</style>

<div id="div1" class="card">${ 
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

<div id="div2" class="card">${ 
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

<div id="div3" class="card">${ 
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

<div id="div4" class="card">${ 
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
<p>Clique para escolher a plataforma:<p>
<div class="button-group">
            <div id="btn1" class="toggle-button">Spotify</div>    
            <div id="btn2" class="toggle-button">Shazam</div>    
            <div id="btn3" class="toggle-button">Deezer</div>    
            <div id="btn4" class="toggle-button">Apple</div>    
</div> 

```js
 const topSpotify = FileAttachment("/data/top_10_spotify_charts_2023.csv").csv({typed:true}); 
 const topShazam = FileAttachment("/data/top_10_shazam_charts_2023.csv").csv({typed:true}); 
 const topDeezer = FileAttachment("/data/top_10_deezer_charts_2023.csv").csv({typed:true}); 
 const topApple = FileAttachment("/data/top_10_apple_charts_2023.csv").csv({typed:true}); 

document.getElementById('div1').style.display = 'block';
document.getElementById('div2').style.display = 'none';
document.getElementById('div3').style.display = 'none';
document.getElementById('div4').style.display = 'none';

var selected = 1

var meuElemento1 = document.getElementById('btn1');
var meuElemento2 = document.getElementById('btn2');
var meuElemento3 = document.getElementById('btn3');
var meuElemento4 = document.getElementById('btn4');
// Define a função que será executada quando o elemento for clicado
meuElemento1.onclick = function(event) {
    if(selected != 1){
        selected = 1
        document.getElementById('div1').style.display = 'block';
        document.getElementById('div2').style.display = 'none';
        document.getElementById('div3').style.display = 'none';
        document.getElementById('div4').style.display = 'none';
    }
    console.log(selected)
};
meuElemento2.onclick = function(event) {
    if(selected != 2){
        selected = 2
        document.getElementById('div1').style.display = 'none';
        document.getElementById('div2').style.display = 'block';
        document.getElementById('div3').style.display = 'none';
        document.getElementById('div4').style.display = 'none';
    }
    console.log(selected)
};
meuElemento3.onclick = function(event) {
    if(selected != 3){
        selected = 3
        document.getElementById('div1').style.display = 'none';
        document.getElementById('div2').style.display = 'none';
        document.getElementById('div3').style.display = 'block';
        document.getElementById('div4').style.display = 'none';
    }
    console.log(selected)
};
meuElemento4.onclick = function(event) {
   if(selected != 4){
        selected = 4
        document.getElementById('div1').style.display = 'none';
        document.getElementById('div2').style.display = 'none';
        document.getElementById('div3').style.display = 'none';
        document.getElementById('div4').style.display = 'block';
    }
    console.log(selected)
};
function updateSelection(newSelected) {
    if(selected != newSelected){
        selected = newSelected;
        
        document.getElementById('div1').style.display = (selected == 1) ? 'block' : 'none';
        document.getElementById('div2').style.display = (selected == 2) ? 'block' : 'none';
        document.getElementById('div3').style.display = (selected == 3) ? 'block' : 'none';
        document.getElementById('div4').style.display = (selected == 4) ? 'block' : 'none';
        
        meuElemento1.classList.toggle('selected', selected == 1);
        meuElemento2.classList.toggle('selected', selected == 2);
        meuElemento3.classList.toggle('selected', selected == 3);
        meuElemento4.classList.toggle('selected', selected == 4);
    }
}

meuElemento1.onclick = function(event) {
    updateSelection(1);
};
meuElemento2.onclick = function(event) {
    updateSelection(2);
};
meuElemento3.onclick = function(event) {
    updateSelection(3);
};
meuElemento4.onclick = function(event) {
    updateSelection(4);
};
```


---