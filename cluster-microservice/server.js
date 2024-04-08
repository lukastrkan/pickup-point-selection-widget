import express from 'express';
import Supercluster from "supercluster";

const app = express();
const port = 5000;

app.use(express.json({limit: '50mb'})); // Povolit zpracování JSON těl požadavků

app.post('/cluster', (req, res) => {
    const points = req.body.points;
    const zoom = req.body.zoom;

    const index = new Supercluster({radius: 240, maxZoom: 14});
    index.load(points)
    const clusters = index.getClusters([-180, -85, 180, 85], zoom)
    clusters.map((cluster) => {
        cluster.properties.zoom = index.getClusterExpansionZoom(cluster.properties.cluster_id)
    })
    res.json(clusters);
});

app.listen(port, '0.0.0.0', () => {
    console.log(`Server listening at http://0.0.0.0:${port}`);
});
