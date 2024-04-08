import {LayersControl, useMap} from "react-leaflet";
import React, {useEffect, useState} from "react";
import {MapTiles} from "./MapTiles";
import {Markers} from "./Markers";
import L from "leaflet";

export const Map = (props) => {
    const {typesData, locationsData, updateBounds, selectedBranchType} = props;
    const [markers, setMarkers] = useState([]);
    const map = useMap();
    const [iconsMapping, setIconsMapping] = useState({});

    useEffect(() => {
        if (locationsData) {
            setMarkers(locationsData.clusters)
        }

    }, [locationsData, map]);

    useEffect(() => {
        if (typesData.length > 0) {
            const newIconsMapping = typesData.reduce((acc, type) => {
                acc[type.id] = new L.Icon({
                    iconUrl: "/media/" + type.icon,
                    iconSize: new L.Point(40, 48),
                    iconAnchor: new L.Point(20, 48),
                    popupAnchor: new L.Point(0, -48)
                });
                return acc;
            }, {});
            setIconsMapping(newIconsMapping);
        }
    }, [typesData]);

    useEffect(() => {
        updateBounds(map); // eslint-disable-next-line
    }, []);

    return (<>
        <LayersControl position="topright">
            <MapTiles apiKey={null}/>
        </LayersControl>
        <Markers markers={markers} iconsMapping={iconsMapping} setSelectedPoint={props.setSelectedPoint}
                 selectedBranchType={selectedBranchType}/>
    </>);
}



