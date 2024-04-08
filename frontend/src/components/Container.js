import {useLazyQuery, useQuery} from "@apollo/client";
import {GET_BRANCH_TYPES, GET_CLUSTERS, GET_LOCATIONS, SEARCH_BRANCHES} from "../query";
import {Col, Row} from "react-bootstrap";
import {BranchTypeSelect} from "./BranchTypeSelect";
import {Search} from "./Search";
import {CustomMapContainer} from "./CustomMapContainer";
import {PointDetail} from "./PointDetail";
import React, {useEffect, useState} from "react";
import {PointList} from "./PointList";

export const Container = (props) => {
    const [selectedPoint, setSelectedPoint] = useState(0);
    const [map, setMap] = useState(null);
    const [branchTypes, setBranchTypes] = useState([]);
    const [selectedBranchType, setSelectedBranchType] = useState(null);
    const [staticBranchType, setStaticBranchType] = useState(null);
    const [northWest, setNorthWest] = useState(null);
    const [southEast, setSouthEast] = useState(null);
    const [pointList, setPointList] = useState(null);
    const [searchTerm, setSearchTerm] = useState(null);

    const {data: branchTypesResponse} = useQuery(GET_BRANCH_TYPES);

    const [getPoints, {data: locationsData}] = useLazyQuery(GET_LOCATIONS);
    const [getSearchBranches, {data: searchBranchesData}] = useLazyQuery(SEARCH_BRANCHES);
    const [getClusters, {data: clustersData}] = useLazyQuery(GET_CLUSTERS);


    const updateBounds = (mapToUse) => {
        const bounds = mapToUse.getBounds();
        setNorthWest(bounds.getNorthWest());
        setSouthEast(bounds.getSouthEast());
    }

    const parseSetSelectedPoint = (data) => {
        setSelectedPoint(parseInt(data.id))
        map.flyTo([data.coordinates.latitude, data.coordinates.longitude], 17)
    }

    useEffect(() => {
        const urlParams = new URLSearchParams(window.location.search);
        const branchType = urlParams.get('delivery_type');
        if (branchType) {
            setStaticBranchType(branchType);
            setSelectedBranchType(branchType);
        }
    }, []);

    //save map bounds to state
    useEffect(() => {
        if (!map) return;
        map.on('moveend', () => updateBounds(map));
        return () => {
            map.off('moveend');
        };
    }, [map]);

    //reset point list when branch type changes
    useEffect(() => {
        if (selectedBranchType) {
            setPointList(null)
        }
    }, [selectedBranchType]);

    //save branch types to state
    useEffect(() => {
        if (branchTypesResponse && branchTypesResponse.branchTypes) {
            setBranchTypes(branchTypesResponse.branchTypes);
            if (!staticBranchType) {
                setSelectedBranchType(branchTypesResponse.branchTypes[0].id)
            }
        }
    }, [branchTypesResponse]);

    //get points visible on map
    useEffect(() => {
        if (northWest && southEast) {
            getPoints({
                variables: {
                    coordinatesA: {
                        latitude: northWest.lat, longitude: northWest.lng
                    }, coordinatesB: {
                        latitude: southEast.lat, longitude: southEast.lng
                    }, branchType: selectedBranchType ? parseInt(selectedBranchType) : null
                }
            });

            getClusters({
                variables: {
                    coordinatesA: {
                        latitude: northWest.lat, longitude: northWest.lng
                    }, coordinatesB: {
                        latitude: southEast.lat, longitude: southEast.lng
                    }, branchType: selectedBranchType ? parseInt(selectedBranchType) : null, zoom: map.getZoom()
                }
            })
        } // eslint-disable-next-line
    }, [southEast, northWest, selectedBranchType]);

    //set point list when data is loaded
    useEffect(() => {
        if (locationsData && !searchTerm) {
            setPointList(locationsData.branches);
        }
    }, [locationsData, searchTerm]);

    //search for branches
    useEffect(() => {
        if (searchTerm) {
            getSearchBranches({
                variables: {
                    search: searchTerm, branchType: selectedBranchType ? parseInt(selectedBranchType) : null
                }
            })
        }
        //set point list to currently visible points
        if (searchTerm === '' && locationsData) {
            setPointList(locationsData.branches)
        }
    }, [searchTerm, selectedBranchType, getSearchBranches, locationsData]);

    //set point list from search result
    useEffect(() => {
        if (searchBranchesData) {
            setPointList(searchBranchesData.branches)
        }
    }, [searchBranchesData]);


    const mapContainer = <CustomMapContainer position={props.position} setSelectedPoint={parseSetSelectedPoint}
                                             setMap={setMap} typesData={branchTypes}
                                             selectedBranchType={selectedBranchType} locationsData={clustersData}
                                             updateBounds={updateBounds}/>

    return (<Row className={'gx-0'}>
        <Col xs={12} md={3} className={'d-flex flex-column'} style={{height: '100vh'}}>
            <div>
                <BranchTypeSelect branchTypes={branchTypes} selectBranchType={setSelectedBranchType} staticBranchType={staticBranchType}/>
                <Search handleSearch={setSearchTerm}/>
            </div>
            <div className={'flex-grow-1 overflow-auto'}>
                <PointList points={pointList} setSelectedPoint={parseSetSelectedPoint}/>
            </div>
        </Col>
        <Col xs={12} md={9}>
            {branchTypes.length > 0 ? mapContainer : <h1>Loading...</h1>}
            <PointDetail id={selectedPoint} selectCallback={setSelectedPoint}/>
        </Col>
    </Row>);


}