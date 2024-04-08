import {Marker, useMap} from "react-leaflet";
import L from "leaflet";

export const Markers = (props) => {
    const {markers, setSelectedPoint, iconsMapping, selectedBranchType} = props;
    const map = useMap();
    return (<>
        {markers.map((marker, index) => {
            if (marker.cluster) {
                return (<LocalGroupedMarker key={index} marker={marker} map={map}/>)
            }
            return (<LocalMarker key={index} marker={marker} icon={iconsMapping[selectedBranchType]}
                                 setSelectedPoint={setSelectedPoint} map={map}/>)
        })}
    </>);
}

const LocalMarker = ({marker, icon, setSelectedPoint, map}) => {
    return (
        <Marker position={[marker.coordinates.latitude, marker.coordinates.longitude]} icon={icon} eventHandlers={{
            click: () => {
                if (setSelectedPoint && marker) {
                    setSelectedPoint(marker);
                }
            }
        }}/>
    )
}

const LocalGroupedMarker = ({marker, map}) => {
    const count = marker.pointCount;
    const size =
        count < 100 ? 'small' :
            count < 1000 ? 'medium' : 'large';

    const icon = L.divIcon({
        html: `<div><span>${count}</span></div>`,
        className: `marker-cluster marker-cluster-${size}`,
        iconSize: L.point(40, 40)
    });

    return (
        <Marker position={[marker.coordinates.latitude, marker.coordinates.longitude]} icon={icon} eventHandlers={{
            click: () => {
                console.log(marker)
                map.flyTo([marker.coordinates.latitude, marker.coordinates.longitude], marker.clusterZoom, {animate: true})
            }
        }}/>
    )
}