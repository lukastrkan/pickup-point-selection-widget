import {useEffect, useState} from "react";
import {useQuery} from "@apollo/client";
import {GET_BRANCH_INFO} from "../query";
import {Button, Col, Row} from "react-bootstrap";

export const PointDetail = ({id, selectCallback}) => {
    const [branch, setBranch] = useState(null);

    const {data: pointData} = useQuery(GET_BRANCH_INFO, {
        variables: {id: id}
    });

    useEffect(() => {
        if (pointData) {
            setBranch(pointData.branch);
        }
    }, [pointData]);


    return (
        <>
            {branch && (
                <>
                    <Row className={'gx-0'}>
                        <Col xs={12} md={6} className={'gx-1'}>
                            <h2>{branch.name}</h2>
                            <p>{branch.address}, {branch.city}, {branch.zip}, {branch.country}</p>
                            <p>Latitude: {branch.coordinates.latitude}, Longitude: {branch.coordinates.longitude}</p>
                        </Col>
                        <Col xs={12} md={6}>
                            <h4>Opening Hours:</h4>
                            <ul>
                                <li>Pondělí: {branch.openningHours.monday ? branch.openningHours.monday : 'ZAVŘENO'}</li>
                                <li>Úterý: {branch.openningHours.tuesday ? branch.openningHours.tuesday : 'ZAVŘENO'}</li>
                                <li>Středa: {branch.openningHours.wednesday ? branch.openningHours.wednesday : 'ZAVŘENO'}</li>
                                <li>Čtvrtek: {branch.openningHours.thursday ? branch.openningHours.thursday : 'ZAVŘENO'}</li>
                                <li>Pátek: {branch.openningHours.friday ? branch.openningHours.friday : 'ZAVŘENO'}</li>
                                <li>Sobota: {branch.openningHours.saturday ? branch.openningHours.saturday : 'ZAVŘENO'}</li>
                                <li>Neděle: {branch.openningHours.sunday ? branch.openningHours.sunday : 'ZAVŘENO'}</li>
                            </ul>
                        </Col>
                    </Row>
                    <Button variant={"outline-danger"} onClick={(e) => {
                        window.parent.postMessage({...pointData, type: 'delivery-widget'}, '*')
                    }}>
                        Vybrat pobočku
                    </Button>
                </>

            )}
            {!branch && (
                <h1>
                    Nejprve vyberte pobočku.
                </h1>
            )}
        </>
    );
}