
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

<div class="card">${
    resize((width) => Plot.plot({
    marginLeft: 90,
    x: { axis: null },
    y: { label: null }, 
    marks: [
      Plot.barX(spotify, {
        x: "streams",
        y: "artist(s)_name",
        sort: { y: "x", reverse: true, limit: 10 }
      }),
      Plot.text(spotify, {
        text: d => `${Math.floor(d.streams / 10000)} M`, 
        y: "artist(s)_name",
        x: "streams",
        textAnchor: "start",
        fill: "white",
        sort: { y: "x", reverse: true, limit: 10 }
      })
    ]
}))
  }</div>

```js
const correlations = FileAttachment("output.json").json({typed:true});

const spotify = FileAttachment("/data/spotify-2023.csv").csv({typed:true});
```