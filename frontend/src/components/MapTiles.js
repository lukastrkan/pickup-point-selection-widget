import {LayerGroup, LayersControl, TileLayer} from "react-leaflet";
import React from "react";

const {BaseLayer} = LayersControl;

const urlOsm = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
export const MapTiles = ({apiKey = null}) => {
    return <>
        <BaseLayer checked name="OpenStreetMap">
            <TileLayer url={urlOsm}
                       attribution={'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'}/>;
        </BaseLayer>
        {apiKey &&
            <BaseLayer name="Mapy.cz">
                <LayerGroup>
                    <TileLayer url={`https://api.mapy.cz/v1/maptiles/aerial/256/{z}/{x}/{y}?lang=cs&apikey=${apiKey}`}/>
                    <TileLayer
                        url={`https://api.mapy.cz/v1/maptiles/names-overlay/256/{z}/{x}/{y}?lang=cs&apikey=${apiKey}`}/>
                </LayerGroup>
            </BaseLayer>
        }
    </>

}