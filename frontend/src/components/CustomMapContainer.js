import {Map} from "./Map";
import {MapContainer} from "react-leaflet";
import {useMemo} from "react";

export const CustomMapContainer = ({
                                       position,
                                       setSelectedPoint,
                                       setMap,
                                       typesData,
                                       selectedBranchType,
                                       locationsData,
                                       updateBounds
                                   }) => {
    const mapMemo = useMemo(() => {
        return (<MapContainer center={position ? [position.coords.latitude, position.coords.longitude] : null}
                              zoom={12} ref={setMap}
                              style={{minHeight: '75vh', maxHeight: '85vh', width: '100%'}} minZoom={9}>
            <Map setSelectedPoint={setSelectedPoint} typesData={typesData} selectedBranchType={selectedBranchType}
                 locationsData={locationsData} updateBounds={updateBounds}/>
        </MapContainer>);
    }, [selectedBranchType, position, setSelectedPoint, setMap, typesData, locationsData, updateBounds]);

    return (mapMemo);
}