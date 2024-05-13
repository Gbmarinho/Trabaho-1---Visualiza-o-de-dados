
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


```js
const correlations = FileAttachment("output.json").json({typed:true});
```